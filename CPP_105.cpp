#include <vector>
#include <string>

namespace {
bool issame(vector<string> a, vector<string> b) {
    if (a.size() != b.size()) return false;
    for (int i = 0; i < a.size(); ++i)
        if (a[i] != b[i]) return false;
    return true;
}
}

vector<string> by_length(vector<int> arr) {
    vector<string> numbers;
    for (int num : arr) {
        if (num >= 1 && num <= 9) {
            numbers.push_back(to_string(num));
        }
    }

    sort(numbers.begin(), numbers.end());
    reverse(numbers.begin(), numbers.end());

    vector<string> result;
    for (string str : numbers) {
        string newstr = "";
        switch (stoi(str)) {
            case 1:
                newstr = "One";
                break;
            case 2:
                newstr = "Two";
                break;
            case 3:
                newstr = "Three";
                break;
            case 4:
                newstr = "Four";
                break;
            case 5:
                newstr = "Five";
                break;
            case 6:
                newstr = "Six";
                break;
            case 7:
                newstr = "Seven";
                break;
            case 8:
                newstr = "Eight";
                break;
            case 9:
                newstr = "Nine";
                break;
        }
        result.push_back(newstr);
    }

    return result;
}