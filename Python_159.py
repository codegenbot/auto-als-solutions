if __name__ == "__main__":
    number = int(input("Enter number of carrots eaten so far: "))
    need = int(input("Enter total number of carrots needed: "))
    remaining = int(input("Enter number of carrots left: "))

    result = eat(number, need, remaining)
    print(f"Total eaten: {result[0]}, Carrots left: {result[1]}")