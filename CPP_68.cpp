#include <vector>
#include <algorithm>

using namespace std;

bool issame(vector<int> a, vector<int> b) {
    if (a.size() != b.size()) {
        return false;
    }
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) {
            return false;
        }
    }
    return true;
}

vector<int> pluck(vector<int> arr) {
    vector<int> result = {};
    int minEvenValue = INT_MAX;

    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0 && arr[i] < minEvenValue) {
            minEvenValue = arr[i];
            result = {minEvenValue, i};
        }
    }

    return result;
}

int main() {
    vector<int> a = {1, 2, 3, 4, 5};
    vector<int> b = {1, 2, 3, 4, 5};
    
    if (issame(a, b)) {
        cout << "Vectors are same." << endl;
    } else {
        cout << "Vectors are not same." << endl;
    }
    
    return 0;
}