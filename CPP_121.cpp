int sumOdd(std::string str) {
    int sum = 0;
    for (char c : str) { 
        int i = static_cast<int>(c);
        if (i % 2 != 0) {
            sum += i;
        }
    }
    return sum;
}