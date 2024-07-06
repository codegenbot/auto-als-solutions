#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> total_match(vector<string> lst1, vector<string> lst2) {
    int total_chars_lst1 = 0;
    for (const string& str : lst1) {
        total_chars_lst1 += str.length();
    }

    int total_chars_lst2 = 0;
    for (const string& str : lst2) {
        total_chars_lst2 += str.length();
    }

    if (total_chars_lst1 < total_chars_lst2)
        return lst1;
    else if (total_chars_lst1 > total_chars_lst2)
        return lst2;
    else
        return lst1;
}

int main() {
    vector<string> vec1 = {"hi", "admin"};
    vector<string> vec2 = {"hI", "Hi"};

    vector<string> result = total_match(vec1, vec2);

    for (const string& str : result) {
        cout << str << endl;
    }

    return 0;
}