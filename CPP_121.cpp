#include <iostream>
#include <vector>

int solutions(const std::vector<int>& lst) {
    int sum = 0;
    for (int i = 1; i < lst.size(); i++) {
        if (lst[i] % 2 != 0) {
            sum += lst[i];
        }
    }
    return sum;
}

int main() {
    std::vector<int> lst;
    int sum = 0;
    for (int i = 1; i <= 10; i++) { 
        int x;
        std::cin >> x;
        lst.push_back(x);
    }
    std::cout << solutions(lst) << std::endl;
}