answer = 0

for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        product = i*j
        str_prod = str(product)

        if str_prod == str_prod[::-1]:
            answer = max(answer, product)

print(answer)