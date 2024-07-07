#include <vector>
using namespace std;

int calculateFuelCost(vector<int> v) {
    int sum = 0;
    for (int i : v) {
        int x = i / 3;  // divide by 3
        x = x - 2;      // subtract 2
        sum += x;       // add to the sum
    }
    return sum;
}

int main() {
    vector<int> v;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        v.push_back(a);
    }
    cout << calculateFuelCost(v) << endl;
    return 0;
}