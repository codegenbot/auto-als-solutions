Here is the completed code:

int sum_of_digits(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int largest_prime(vector<int> lst) {
    for (int num : lst) {
        if (isPrime(num)) {
            return num;
        }
    }
    return -1; // or some default value if no prime is found
}

bool isPrime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int max_prime;
    // code to read input from user
    cin >> max_prime;

    return sum_of_digits(max_prime);
}