#include <iostream>
#include <vector>
using namespace std;

int add_elements(vector<int> arr, int k) {
    int sum = 0;
    for (int i = 0; i < min(k, arr.size()); i++) {
        if (to_string(arr[i]).size() <= 2) {
            sum += arr[i];
        }
    }
    return sum;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    int k = 3;
    assert(add_elements(arr, k) == 6);
    return 0;
}