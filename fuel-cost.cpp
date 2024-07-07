int fuelCost(vector<int> prices) {
    int sum = 0;
    for (int price : prices) {
        int result = floor((double)price / 3) - 2;
        if (result < 0) {
            result = 0;
        }
        sum += result;
    }
    return sum;
}