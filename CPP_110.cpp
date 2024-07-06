```cpp
#include <iostream>
#include <vector>
#include <string>

bool hasOdd(std::vector<int>& vec) {
    for (int num : vec) {
        if (num % 2 != 0)
            return true;
    }
    return false;
}

std::string exchange(std::vector<int> lst1, std::vector<int> lst2) {
    while (!hasOdd(lst1)) {
        bool found = false;
        for (int i = 0; i < lst2.size(); i++) {
            if (lst2[i] % 2 != 0) {
                std::swap(lst1.back(), lst2[i]);
                found = true;
                break;
            }
        }
        if (!found)
            return "NO";
    }
    return "YES";
}

int main() {
    assert(exchange({100, 200}, {200, 200}) == "YES");
}