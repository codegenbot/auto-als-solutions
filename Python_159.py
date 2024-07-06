def eat(hungry, needed, remaining):
    eaten = min(min(needed, hungry), remaining)
    remaining_after_eat = remaining - eaten
    print("Eaten:", eaten, "Remaining:", remaining_after_eat)


if __name__ == "__main__":
    hungry = int(input("Enter how hungry you are (1-10): "))
    needed = int(input("Enter how much you need to eat (1-10): "))
    remaining = int(input("Enter how many bites left: "))
    eat(hungry, needed, remaining)