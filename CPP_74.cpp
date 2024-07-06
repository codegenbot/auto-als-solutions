```cpp
#include <vector>
#include <string>

bool issame(const std::vector<std::string>& a,const std::vector<std::string>& b){
    return a == b;
}

std::vector<std::string> total_match(const std::vector<std::string>& lst1, const std::vector<std::string>& lst2) {
    int sum1 = 0;
    for (const auto& str : lst1) {
        sum1 += str.length();
    }
    
    int sum2 = 0;
    for (const auto& str : lst2) {
        sum2 += str.length();
    }
    
    if (sum1 < sum2) {
        return issame(lst1, lst2)?lst1:lst2;
    } else if (sum1 > sum2) {
        return issame(lst1, lst2)?lst2:lst1;
    } else {
        return issame(lst1, lst2)?lst1:lst2;
    }
}