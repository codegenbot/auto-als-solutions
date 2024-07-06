#include <cctype>
using namespace std;

string file_name_check(string file_name) {
    int dot_count = 0;
    bool has_letters = false;
    bool has_digits = false;
    string before_dot = "";
    for (char c : file_name) {
        if (c == '.') {
            dot_count++;
            if (dot_count > 1) return "No";
        } else if (isdigit(c)) {
            has_digits = true;
        } else if (isalpha(c)) {
            has_letters = true;
            before_dot += c;
        }
    }
    string after_dot = file_name.substr(file_name.find('.') + 1);
    if (has_digits && count(after_dot.begin(), after_dot.end(), '.') > 0) return "No";
    if (!has_letters || before_dot.empty()) return "No";
    vector<string> extensions = {"txt", "exe", "dll"};
    for (string ext : extensions) {
        if (after_dot == ext) return "Yes";
    }
    return "No";
}