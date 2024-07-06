#include <vector>
#include <algorithm>
#include <string>
#include <cstdlib> // For rand() function

bool issame(vector<string> a, vector<string> b) {
    return a == b;
}

vector<string> total_match(vector<string> lst1, vector<string> lst2) {
    if (issame(lst1, lst2)) {
        return lst1;
    } else {
        int sum1 = 0;
        for (const auto& str : lst1) {
            sum1 += str.length();
        }
        
        int sum2 = 0;
        for (const auto& str : lst2) {
            sum2 += str.length();
        }
        
        if (sum1 < sum2) {
            return lst1;
        } else if (sum1 > sum2) {
            return lst2;
        } else {
            if (rand() % 2 == 0) {
                return lst1;
            } else {
                return lst2;
            }
        }
    }
}

int main() {
    vector<string> list1 = {"this"};
    vector<string> list2 = {};
    
    assert (issame(total_match(list1, list2), {}));
    
    return 0;
}