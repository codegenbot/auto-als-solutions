int calculateFuelCost(vector<int> &costs) {
    int total = 0;
    for (int cost : costs) {
        int new_cost = (cost / 3) - 2;
        total += new_cost;
    }
    return total;
}