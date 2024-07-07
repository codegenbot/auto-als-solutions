#include <vector>
using namespace std;

int calculateFuelCost(vector<int> costs) {
    int total = 0;
    for (int cost : costs) {
        cost /= 3;
        cost = floor(cost);
        cost -= 2;
        total += cost;
    }
    return total;
}

int main() {
    vector<int> costs;
    int n;
    cin >> n;
    while(n--) {
        int cost; 
        cin >> cost;
        costs.push_back(cost);
    }
    cout << calculateFuelCost(costs) << endl;
    return 0;
}