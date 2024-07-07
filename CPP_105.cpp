#include <string>
#include <vector>

bool issame(vector<string> a, vector<string>b) {
    // implement the logic for issame function
}

vector<string> by_length(vector<int> arr) {
    vector<string> temp;
    for (int i : arr) {
        if (i >= 1 && i <= 9) {
            temp.push_back(to_string(i));
        }
    }
    sort(temp.begin(), temp.end());
    reverse(temp.begin(), temp.end());
    return temp;
}