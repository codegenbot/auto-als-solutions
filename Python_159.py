def eat(hungry, needed, remaining):
    eaten = min(min(needed, hungry), remaining)
    return [eaten, remaining - eaten]


if __name__ == "__main__":
    hungry = int(input("Enter how much you are hungry: "))
    needed = int(input("Enter how much food is needed: "))
    remaining = 10
    result = eat(hungry, needed, remaining)
    print(f"Eaten: {result[0]}, Remaining: {result[1]}")