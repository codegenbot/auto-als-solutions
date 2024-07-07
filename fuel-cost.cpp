#include <vector>
using namespace std;

int solve(vector<int> v) {
    int sum = 0;
    for (int i : v) {
        int temp = (i / 3);
        temp = floor(temp);
        temp -= 2;
        sum += temp;
    }
    return sum;
}

int main() {
    int n;
    cin >> n;
    vector<int> vec(n);
    for (int i = 0; i < n; i++) {
        cin >> vec[i];
    }
    cout << solve(vec) << endl;
    return 0;
}