```cpp
#include <vector>
#include <algorithm>
#include <initializer_list>

std::vector<int> generate_integers(int start, int end) {
    std::vector<int> numbers;
    for(int i = start; i <= end; ++i) {
        numbers.push_back(i);
    }
    return numbers;
}

bool issame(std::vector<int> a, std::vector<int> b) {
    return a == b;
}

int main_test() { 
    assert(issame(generate_integers(17, 89), generate_integers(17, 89)));
    return 0;
}