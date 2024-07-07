#include <string>

using namespace std;

string file_name_check(string file_name) {
    int dot_count = 0;
    int digit_count = 0;
    bool first_letter_valid = false;

    for (int i = 0; i < file_name.length(); i++) {
        if (file_name[i] == '.') {
            dot_count++;
            if (dot_count > 1) return "No";
        } else if (isdigit(file_name[i])) {
            digit_count++;
            if (digit_count > 3) return "No";
        } else if (!first_letter_valid && isalpha(file_name[i])) {
            first_letter_valid = true;
        }
    }

    string extension = file_name.substr(file_name.find('.') + 1);
    if (extension != "txt" && extension != "exe" && extension != "dll") return "No";

    return "Yes";
}