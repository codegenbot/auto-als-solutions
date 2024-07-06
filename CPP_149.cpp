#include <iostream>
#include <vector>
#include <algorithm>

bool issame(vector<string>, vector<string>);
vector<string> sorted_list_sum(vector<string>);

int main() {
    std::vector<std::string> lst = {"hello", "world", "abc", "def"};
    std::vector<std::string> result = sorted_list_sum(lst);
    
    for (const auto& str : result) {
        std::cout << str << std::endl;
    }
    return 0;
}

bool issame(vector<string>, vector<string>) {
    // Your code here
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