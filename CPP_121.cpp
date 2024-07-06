```cpp
#include <vector>
int main() {
    int solutions = 0;
    std::vector<int> lst;
    int input;
    while (true) {
        std::cout << "Enter an integer (-1 to finish): ";
        std::cin >> input;
        if (input == -1) break;
        lst.push_back(input);
    }
    for (int i = 1; i < lst.size(); i++) {
        if (lst[i] % 2 != 0) {
            solutions += lst[i];
        }
    }
    std::cout << "Sum of odd integers: " << solutions << std::endl;
    return 0;
}