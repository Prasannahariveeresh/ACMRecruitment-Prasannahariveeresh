def PasswordValidator(passwd):
    has_upper = any(i.isupper() for i in passwd)
    has_lower = any(i.islower() for i in passwd)
    passwords = ["A1b#cD3e", "Xy4$Zz7!", "P@ssw0rd", "M!n3r4L^", "T7r$eN8f"]
    
    success = True

    if len(passwd) < 8:
        success = False
        print('Length of passwors is less than 8')
    if not (has_upper and has_lower):
        success = False
        print('Does not contain atleast one Capital Letter and one Small Letter ')
    if not passwd[0].isalnum() or passwd[0].isdigit():
        success = False
        print('Password starts with special charectar or a number')
    if passwd in passwords:
        success = False
        print('Admin hates this password !!!')

    return success

passwd = input('Enter your password: ')
res = PasswordValidator(passwd)
if res:
    print(f"Password: {passwd} is accepted !!!")
else:
    print(f"Password: {passwd} is rejected.")