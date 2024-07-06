#include <algorithm>
#include <vector>
#include <string>

bool issame(vector<string>, vector<string>);
vector<string> sorted_list_sum(vector<string>);

int main() {
    // Your code here
    return 0;
}

bool issame(vector<string> v1, vector<string> v2) {
    // your logic here
    return true; // replace with actual logic
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