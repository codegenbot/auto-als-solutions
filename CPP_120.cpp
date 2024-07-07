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
    std::vector<int> arr;
    int k, n;

    std::cout << "Enter the size of array: ";
    std::cin >> n;
    
    for(int i = 0; i < n; i++) {
        int x;
        std::cout << "Enter element " << i+1 << ": ";
        std::cin >> x;
        arr.push_back(x);
    }

    std::cout << "Enter k: ";
    std::cin >> k;

    vector<int> result = maximum(arr, k);

    if(issame(result, arr)) {
        std::cout << "Array is sorted" << std::endl;
    } else {
        std::cout << "Array is not sorted" << std::endl;
    }

    return 0;
}

vector<int> maximum(vector<int> arr, int k) {
    vector<int> result;
    for (int i = 0; i < k; i++) {
        auto it = std::max_element(arr.begin(), arr.end());
        result.push_back(*it);
        arr.erase(it);
    }
    return result;
}