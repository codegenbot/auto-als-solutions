Here is the solution:

#include <vector>
using namespace std;

int basement(vector<int>& arr) {
    int sum = 0;
    for (int i = 0; i < arr.size(); i++) {
        sum += arr[i];
        if (sum < 0)
            return i;
    }
    return -1;
}

int main() {
    // Add your input data here
    vector<int> arr = {1, -1};
    cout << basement(arr) << endl;

    return 0;
}