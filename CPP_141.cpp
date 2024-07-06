#include <string>
using namespace std;

string file_name_check(string file_name) {
    bool has_dot = false;
    int dot_index = -1;
    int digit_count = 0;
    string before_dot = "";
    for (int i = 0; i < file_name.size(); i++) {
        char c = file_name[i];
        if (isdigit(c)) {
            digit_count++;
            if (digit_count > 3) {
                return "No";
            }
        } else if (c == '.') {
            has_dot = true;
            dot_index = i;
        } else if (!has_dot && !isalpha(c)) {
            return "No";
        } else if (has_dot) {
            string after_dot = file_name.substr(dot_index + 1);
            if (after_dot != "txt" && after_dot != "exe" && after_dot != "dll") {
                return "No";
            }
        }
    }
    if (!has_dot || before_dot.empty()) {
        return "No";
    }
    return "Yes";
}