```cpp
int basement(const std::vector<int>& v) {
    int sum = 0;
    for (int i = 0; i < v.size(); i++) {
        sum += v[i];
        if (sum < 0)
            return i + 1;
    }
    return -1;

}

int main() {
    std::vector<int> v = {1, 2, -3, 4};
    int result = basement(v);
    std::cout << "Basement at index: " << result << std::endl;
    return 0;
}