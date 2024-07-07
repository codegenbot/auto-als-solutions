Here is the solution:

int calculateFuelCost(vector<int> numbers) {
    int sum = 0;
    for (int num : numbers) {
        int result = (num / 3);
        result = result - 2;
        if (result < 0) {
            result = 0;
        }
        sum += result;
    }
    return sum;
}