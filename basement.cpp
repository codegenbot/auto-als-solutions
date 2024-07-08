```cpp
int basement(const std::vector<int>& v) {
    int sum = 0;
    for (int i = 0; i < v.size(); i++) {
        sum = 0; 
        for (int j = 0; j <= i; j++) {
            sum += v[j];
            if (sum < 0)
                return j + 1;
        }
    }
    return -1;
}