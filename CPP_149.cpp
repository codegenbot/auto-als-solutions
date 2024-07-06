#include <iostream>
#include <vector>
#include <algorithm>

bool issame(vector<string>, vector<string>);

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

int main() {
    // Using the functions
    vector<string> list = {"Hello", "World", "abc", "xyz", "abcd"};
    vector<string> sortedList = sorted_list_sum(list);
    for (const string& str : sortedList) {
        cout << str << endl;
    }
    
    return 0;
}