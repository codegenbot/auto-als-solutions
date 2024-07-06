```cpp
#include <vector>
#include <algorithm>
#include <string>

bool issame(std::vector<std::string> a) {
    for (int i = 0; i < a.size() - 1; i++) {
        if (!(a[i] == a[i + 1])) return false;
    }
    return true;
}

std::vector<std::string> total_match(std::vector<std::string> lst1, std::vector<std::string> lst2) {
    int sum1 = 0;
    for (const auto& str : lst1) {
        sum1 += str.length();
    }
    
    int sum2 = 0;
    for (const auto& str : lst2) {
        sum2 += str.length();
    }

    if (lst1 == lst2) {
        return lst1;
    } else if (sum1 < sum2) {
        return lst1;
    } else if (sum1 > sum2) {
        return lst2;
    }
    
    int sum1lst = 0, sum2lst = 0;
    for (const auto& str : lst1) {
        sum1lst += str.length();
        for (char c : str) {
            sum1lst += 1;
        }
    }

    for (const auto& str : lst2) {
        sum2lst += str.length();
        for (char c : str) {
            sum2lst += 1;
        }
    }

    if (sum1lst < sum2lst) {
        return lst1;
    } else if (sum1lst > sum2lst) {
        return lst2;
    } else {
        for (const auto& str : lst1) {
            for (const auto& sub_str : lst2) {
                if (str.find(sub_str) != std::string::npos || sub_str.find(str) != std::string::npos) {
                    return lst1;
                }
            }
        }

        return lst1.size() < lst2.size() ? lst1 : lst2;
    }
}