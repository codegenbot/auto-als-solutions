def find_average_and_round_to_next_highest_perfect_square(input_number):
    total = 0
    for _ in range(int(input("Enter the number of scores: "))):
        score = float(input("Enter a score: "))
        total += score
    average = math.ceil(math.sqrt(total))
    return bin(average)[2:]