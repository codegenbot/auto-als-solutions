```cpp
#include <vector>
#include <algorithm>

std::vector<int> generate_integers(int a, int b) {
    std::vector<int> result;
    for (int i = std::min(a, b); i <= std::max(a, b); i++) {
        if (i % 2 == 0) {
            result.push_back(i);
        }
    }
    return result;
}

bool operator==(const std::vector<int>& a,const std::vector<int>&b){
    return (a==b);
}

int main() {
    assert(std::equal(generate_integers(1,20).begin(), generate_integers(1,20).end()));
    return 0;
}