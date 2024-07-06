int hex_key(string num) {
    int count = 0;
    for (char c : num) {
        if (c <= '9') {
            int decimal = c - '0';
        } else {
            switch (c) {
                case 'A':
                    decimal = 10;
                    break;
                case 'B':
                    decimal = 11;
                    break;
                case 'C':
                    decimal = 12;
                    break;
                case 'D':
                    decimal = 13;
                    break;
                case 'E':
                    decimal = 14;
                    break;
                case 'F':
                    decimal = 15;
                    break;
            }
        }
        if (decimal > 1 && isPrime(decimal)) {
            count++;
        }
    }
    return count;
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