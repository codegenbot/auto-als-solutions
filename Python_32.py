def find_zero():
    xs = []
    while True:
        try:
            inp = input(
                "Enter coefficients (space-separated integers), or 'done' if finished: "
            )
            if inp.lower() == "done":
                break
            xs.extend(map(int, inp.split()))
        except ValueError as e:
            print(f"Invalid input: {e}. Try again.")
    return find_zero(xs)


print(find_zero())