```cpp
#include <vector>
#include <algorithm>

bool same(const std::vector<int>& a, const std::vector<int>& b) {
    return a == b;
}

std::vector<int> extract(std::vector<int> arr) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 != 0) {
            return {};
        }
    }
    
    int result = arr[0];
    for (int i = 1; i < arr.size(); i++) {
        if ((arr[i]%2) != (result%2)) {
            return {};
        }
    }
    
    std::vector<int> resultVec;
    resultVec.push_back(result);
    
    return resultVec;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> arr(n);
    for (auto &i : arr)
        std::cin >> i;

    std::vector<int> result = extract(arr);

    if(result.empty())
        std::cout << "empty" << std::endl;
    else
        for(int i: result) 
            std::cout << i << " ";
}