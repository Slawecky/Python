# program, ktory wypisze liczby (0 do 100) z ciagu Fibonacciego
# 0, 1, 1, 2, 3, 5, 8, 13, 21


def fibonacci(n):
    """Ciąg Fibonacciego (definicja rekurencyjna)."""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Ciąg Fibonaciego : ")
for fib in range(36):

    print(f"Liczba {fib}    :   {fibonacci(fib)}")