def fizz_buzz(n: int):
    backticks = ""
    for i in range(1, n + 1):
        if i % 11 == 0 and i % 13 == 0:
            backticks += "Backtick"
        elif i % 11 == 0:
            backticks += "Quote"
        elif i % 13 == 0:
            backticks += "Tick"
        else:
            backticks += str(i)
        if i % 3 == 0:
            backticks += "Buzz"
        elif i % 5 == 0:
            backticks += "Fizz"
        elif i % 7 == 0:
            backticks += "Backtick"
        else:
            backticks += str(i) + " "
    return backticks