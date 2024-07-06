#include <iostream>
#include <vector>
using namespace std;

vector<pair<int, int>> pluck(vector<int> arr) {
    vector<pair<int, int>> result;
    if (arr.empty()) {
        return {{}, 0};
    }
    
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0) {
            bool found = false;
            for (auto& p : result) {
                if (p.first == arr[i]) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                for (int j = 0; j < i; j++) {
                    if (arr[j] % 2 == 0 && arr[j] < arr[i]) {
                        result = {{arr[i], i}};
                        return result;
                    }
                }
                result = {{arr[i], i}};
                return result;
            }
        }
    }
    
    return {{}, 0};
}

int main() {
    vector<int> arr1 = {4,2,3};
    cout << "Output for input {" << arr1[0] << "," << arr1[1] << "," << arr1[2] << "} is: ";
    for (auto& p : pluck(arr1)) {
        cout << p.first << " " << p.second << endl;
    }
    
    vector<int> arr2 = {1,2,3};
    cout << "\nOutput for input {" << arr2[0] << "," << arr2[1] << "," << arr2[2] << "} is: ";
    for (auto& p : pluck(arr2)) {
        cout << p.first << " " << p.second << endl;
    }
    
    vector<int> arr3 = {};
    cout << "\nOutput for input {} is: ";
    for (auto& p : pluck(arr3)) {
        cout << p.first << " " << p.second << endl;
    }
    
    vector<int> arr4 = {5, 0, 3, 0, 4, 2};
    cout << "\nOutput for input {" << arr4[0] << "," << arr4[1] << "," << arr4[2] << "," << arr4[3] << "," << arr4[4] << "," << arr4[5] << "} is: ";
    for (auto& p : pluck(arr4)) {
        cout << p.first << " " << p.second << endl;
    }
    
    return 0;
}