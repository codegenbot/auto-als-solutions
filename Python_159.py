if __name__ == "__main__":
    number = int(input("Enter number of carrots eaten so far: "))
    need = int(input("Enter total number of carrots needed: "))
    remaining = int(input("Enter number of carrots left: "))

    result = eat(number, need, remaining)
    print(f"Total eaten: {result[0]}, Carrots left: {result[1]}")


def eat(number, need, remaining):
    total_eaten = (
        number + (need - remaining) if remaining >= need else number + remaining
    )
    carrots_left = max(0, remaining - (need - remaining)) if remaining >= need else 0
    return [total_eaten, carrots_left]