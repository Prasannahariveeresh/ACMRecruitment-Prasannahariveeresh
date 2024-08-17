import os
import time
import random

class TicTacToe:

    def __init__(self):
        self.__current_player = ''
        self.__computer = ''
        self.__board = ['-' for i in range(9)]
        self.__entries = {'O': 0, 'X': 0}

        self.clear_screen()
    
    def make_move(self, idx):
        if (self.__board[idx - 1] not in self.__entries.keys()):
            self.__board[idx - 1] = self.__current_player
            self.__entries[self.__current_player] += 1

            self._print_board()
            return True

        else: return False

    def initialize_player(self):
        while True:
            self.__current_player = input('Enter the charecter you want ("X" or "O"): ').upper()

            if not self.__current_player in self.__entries.keys():
                self.clear_screen()
                print("INVALID CHARECTER !!!!")
                continue
            else: break

        self.__computer = "X" if self.__current_player == "O" else "O"

        return self.__current_player

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def _print_board(self):
        print("\n")
        print("\t      |      |")
        print("\t  {}   |  {}   |  {}".format(self.__board[0], self.__board[1], self.__board[2]))
        print('\t______|______|______')

        print("\t      |      |")
        print("\t  {}   |  {}   |  {}".format(self.__board[3], self.__board[4], self.__board[5]))
        print('\t______|______|______')

        print("\t      |      |")
        print("\t  {}   |  {}   |  {}".format(self.__board[6], self.__board[7], self.__board[8]))
        print("\t      |      |")
        print("\n")

        time.sleep(2)

    def think_move(self):
        print('Thinking...')
        move = random.randint(0, 8)
        while (self.__board[move] == self.__computer) or\
            (self.__board[move] == self.__current_player):

            move = random.randint(0, 8)

        self.__board[move] = self.__computer
        self.__entries[self.__computer] += 1
        self.clear_screen()

        print("COMPUTER")
        self._print_board()

    def validate_result(self):
        winning_pos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        win = False
        player = ''

        for i in winning_pos:
            user_win = all(self.__board[j-1] == self.__current_player for j in i)
            comp_win = all(self.__board[j-1] == self.__computer for j in i)

            if user_win:
                win = user_win
                player = self.__current_player
                break
            if comp_win:
                win = comp_win
                player = self.__computer
                break

        if '-' not in self.__board:
            win = True
            player = 'Tie'

        return win, player

if __name__ == '__main__':
    game_obj = TicTacToe()
    player = game_obj.initialize_player()

    while True:
        stat = False

        # Avoid position is overwriting
        while not stat:
            idx = int(input(f"Enter a number from 1-9: "))
            if not (idx >= 1 and idx <= 9):
                continue

            stat = game_obj.make_move(idx)
            if not stat:
                print("Invalid Move !!!")

        # Review answers after user input
        win, winner = game_obj.validate_result()
        if win:
            game_obj.clear_screen()
            print('YAYYYYY !!! User won !' if winner != "Tie" else "GAME TIED")
            break

        # Let computer think and review answers after computer's move
        game_obj.think_move()
        win, winner = game_obj.validate_result()
        if win:
            game_obj.clear_screen()
            print('OOOPPSSSS !!! Computer won !' if winner != "Tie" else "GAME TIED")
            break
