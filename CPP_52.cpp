#include <iostream>
#include <vector>
using namespace std;

bool below_threshold(vector<int> l, int t) {
    for (int i : l) {
        if (i >= t) {
            return false;
        }
    }
    return true;
}

int main() {
    vector<int> numbers;
    int threshold;

    cout << "Enter the number of elements: ";
    int n; cin >> n;
    
    cout << "Enter the elements: ";
    for(int i = 0; i < n; i++) {
        int num; cin >> num;
        numbers.push_back(num);
    }

    cout << "Enter the threshold value: ";
    cin >> threshold;

    if(below_threshold(numbers, threshold)) {
        cout << "All elements are below the threshold." << endl;
    } else {
        cout << "Not all elements are below the threshold." << endl;
    }
    
    return 0;
}