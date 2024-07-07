int calculateFuelCost(vector<int> vec) {
    int total = 0;
    for (int num : vec) {
        int result = (num / 3) - 2;
        total += result;
    }
    return total;
}