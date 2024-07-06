#include <iostream>
#include <algorithm>
#include <cmath>

int maxAbsSum(int arr[], int n) {
    std::vector<int> l;
    for (int i = 0; i < n; i++) {
        l.push_back(arr[i]);
    }
    
    return std::abs(*std::max_element(l.begin(), l.end()));
}