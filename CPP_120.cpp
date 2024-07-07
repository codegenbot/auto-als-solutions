#include <iostream>
#include <vector>

bool issame(vector<int> a, vector<int> b) {
    if(a.size() != b.size()) 
        return false;
    for(int i = 0; i < a.size(); i++) {
        if(a[i] != b[i]) 
            return false;
    }
    return true;
}

int main() {
    int n, k;
    std::cout << "Enter the size of array: ";
    std::cin >> n;
    std::cout << "Enter the value of k: ";
    std::cin >> k;

    vector<int> arr(n);
    for(int i = 0; i < n; i++) {
        std::cout << "Enter element " << i+1 << ": ";
        std::cin >> arr[i];
    }

    vector<int> result;
    for (int i = 0; i < k; i++) {
        auto it = std::max_element(arr.begin(), arr.end());
        result.push_back(*it);
        arr.erase(it);
    }
    return 0;
}