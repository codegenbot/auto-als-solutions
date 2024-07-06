```cpp
std::vector<int> sortByDigitSum(std::vector<int> numbers) {
    std::stable_sort(numbers.begin(), numbers.end(), 
        [&](int x) { return abs(x); });
    return numbers;
}