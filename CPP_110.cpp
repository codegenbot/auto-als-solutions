#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

std::string exchange(std::vector<int> lst1, std::vector<int> lst2) {
    for (int num : lst1) {
        if (num % 2 != 0) {
            bool found = false;
            for (int num2 : lst2) {
                if (num2 % 2 == 0) {
                    std::swap(lst1.back(), *std::find(lst2.begin(), lst2.end(), num2));
                    found = true;
                    break;
                }
            }
            if (!found) return "NO";
        }
    }
    return "YES";
}