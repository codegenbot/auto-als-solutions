```
#include <vector>
#include <algorithm>

bool compare(const std::pair<int, int>& a, const std::pair<int, int>& b) {
    if (a.first != b.first) return a.first < b.first;
    return a.second < b.second;
}

int pluck(std::vector<int> arr) {
    int prev = -1;
    for (int i = 0; i < arr.size(); ++i) {
        if (arr[i] % 2 == 0 && (prev == -1 || i > prev)) {
            return arr[i];
        }
        prev = i;
    }
    return -1;
}

int main() {
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;
    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        int x;
        std::cout << "Enter element " << i+1 << ": ";
        std::cin >> x;
        arr[i] = x;
    }
    int result = pluck(arr);
    if(result != -1)
    {
        std::cout << "The output is: " << result << std::endl;
    }
    else
    {
        std::cout << "No output" << std::endl;
    }
    
    return 0;
}