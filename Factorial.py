# Factorial
num = int(input("Número para factorial: "))
factorial = 1
if num < 0:
    print("Factorial no definido para negativos")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("El factorial de", num, "es:", factorial)