int sumOfDigits(int num) {
    int sum = 0;
    while (num > 0) {
        sum += num % 10;
        num /= 10;
    }
    return sum;
}

int largestPrime(vector<int> lst) {
    for (int i : lst) {
        if (isPrime(i)) {
            return i;
        }
    }
    return -1; // or any other default value you want
}

bool isPrime(int num) {
    if (num <= 1) {
        return false;
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

int skjkasdkd(vector<int> lst) {
    int largestPrimeNum = largestPrime(lst);
    if (largestPrimeNum != -1) {
        return sumOfDigits(largestPrimeNum);
    } else {
        return 0; // or any other default value you want
    }
}