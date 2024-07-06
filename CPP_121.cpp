#include <vector>
#include <algorithm>

int main() {
    int solutions = 0;
    std::vector<int> lst;
    int input;
    
    while (std::cin >> input) {
        lst.push_back(input);
    }
    
    for (int i = 1; i < lst.size(); i++) {
        if (lst[i] % 2 != 0) {
            solutions += lst[i];
        }
    }
    
    return solutions;
}