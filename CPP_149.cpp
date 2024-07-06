#include <algorithm>
#include <vector>
#include <string>

vector<string> sorted_list_sum(vector<string> lst) {
    // Remove strings with odd lengths from the vector
    lst.erase(remove_if(lst.begin(), lst.end(),
        [](const string& str) { return str.length() % 2; }), lst.end());
    
    // Sort the remaining strings by length and then alphabetically
    std::stable_sort(lst.begin(), lst.end(),
        [](const string& str1, const string& str2) {
            if (str1.length() == str2.length())
                return str1 < str2;
            else
                return str1.length() < str2.length();
        });
    
    return lst;
}