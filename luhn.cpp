int luhnSum(const std::vector<int>& digits) {
    int sum = 0;
    bool doubleNext = false;

    for (int i = 0; i < digits.size(); i++) {
        if (!doubleNext) {
            sum += digits[i];
        } else {
            int digit = digits[i] * 2;
            if (digit > 9) {
                digit -= 9;
            }
            sum += digit;
        }

        doubleNext = !doubleNext;
    }

    return sum;
}