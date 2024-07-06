def find_largest_palindrome(limit: int) -> int:
    def is_palindrome(n: int) -> bool:
        return str(n) == str(n)[::-1]

    largest_palindrome = 0
    for i in range(2, limit):
        if is_palindrome(i):
            if i > largest_palindrome:
                largest_palindrome = i
    return largest_palindrome