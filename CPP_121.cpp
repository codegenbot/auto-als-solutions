#include <vector>
#include <iostream>

int main() {
    std::vector<int> lst;
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;
    
    for (int i = 0; i < n; ++i) {
        int num;
        std::cout << "Enter element " << i + 1 << ": ";
        std::cin >> num;
        lst.push_back(num);
    }
    
    int result = solution(lst);
    std::cout << "The sum of odd elements is: " << result << std::endl;
    return 0;
}

int solution(vector<int> lst) {
    int sum = 0;
    for (int i = 0; i < lst.size(); i++) {
        if ((i % 2 == 0 && lst[i] % 2 != 0)) {
            sum += lst[i];
        }
    }
    return sum;
}