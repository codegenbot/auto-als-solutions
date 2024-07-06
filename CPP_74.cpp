#include <vector>
#include <algorithm>
#include <string>

namespace std {
bool issame(vector<string> a, const vector<string>& b) {
    if (a.size() != b.size()) {
        return false;
    }
    
    for (size_t i = 0; i < a.size(); ++i) {
        if (a[i].compare(b[i]) != 0) {
            return false;
        }
    }

    return true;
}

vector<string> total_match(vector<string> lst1, vector<string> lst2) {
    int sum1 = 0;
    for (const auto& str : lst1) {
        sum1 += str.length();
    }
    
    int sum2 = 0;
    for (const auto& str : lst2) {
        sum2 += str.length();
    }

    if (issame(lst1, lst2)) {
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
                if (str.find(sub_str) != string::npos || sub_str.find(str) != string::npos) {
                    return lst1;
                }
            }
        }

        return lst1.size() < lst2.size() ? lst1 : lst2;
    }
}