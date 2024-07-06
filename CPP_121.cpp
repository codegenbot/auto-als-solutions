#include <vector>
#include <iostream>

int main() {
    std::vector<int> lst;
    int sum = 0;
    int num;
    for (int i = 1; ; i++) {
        std::cin >> num;
        if (!(num % 2 != 0)) {
            break;
        }
        lst.push_back(num);
    }

    for (int i = 1; i < lst.size(); i++) {
        if (lst[i] % 2 != 0) {
            sum += lst[i];
        }
    }
    return sum;
}