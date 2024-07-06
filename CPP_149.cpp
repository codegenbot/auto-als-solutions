```cpp
#include <iostream>
#include <vector>
#include <algorithm>

bool issame(vector<string>, vector<string>);
vector<string> sorted_list_sum(vector<string>);

int main() {
    std::vector<std::string> lst1 = {"abc", "pqr", "def", "xyz"};
    std::vector<std::string> lst2 = {"xyz", "pqr", "abc", "def"};

    if (issame(lst1, lst2)) {
        std::cout << sorted_list_sum(lst1) << std::endl;
    }

    return 0;
}

bool issame(vector<string> v1, vector<string> v2) {
    if (v1.size() != v2.size()) {
        return false;
    }
    
    for (int i = 0; i < v1.size(); i++) {
        if (v1[i] != v2[i]) {
            return false;
        }
    }

    return true;
}

vector<string> sorted_list_sum(vector<string> lst) {
    vector<string> result;

    // Remove strings with odd lengths from the list
    for (const string& str : lst) {
        if (str.length() % 2 == 0) {
            result.push_back(str);
        }
    }

    // Sort the resulting list by length and then alphabetically
    sort(result.begin(), result.end(),
         [](const string& a, const string& b) {
             if (a.length() != b.length()) {
                 return a.length() < b.length();
             } else {
                 return a < b;
             }
         });

    return result;
}