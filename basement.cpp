#include <vector>
#include <iostream>

int basement(const std::vector<int>& v) {
    int sum = 0;
    for (int i = 0; i < v.size(); i++) {
        if (sum < 0)
            return i + 1;
        sum += v[i];
    }
    return -1;
}

int main() {
    std::vector<int> v = {9, 12, -98, -78, 1, -73, -96, -3, -86, -50};
    int result = basement(v);
    std::cout << "The basement index is: " << result << std::endl;
    return 0;
}