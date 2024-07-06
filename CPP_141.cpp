string file_name_check(string file_name) {
    bool isValid = true;
    int dotCount = 0;
    int digitCount = 0;

    for (char c : file_name) {
        if (c == '.') {
            dotCount++;
            if (dotCount > 1) {
                isValid = false;
                break;
            }
        } else if (isdigit(c)) {
            digitCount++;
            if (digitCount > 3) {
                isValid = false;
                break;
            }
        } else if (!isalpha(c) && c != '.') {
            isValid = false;
            break;
        }
    }

    string extension = file_name.substr(file_name.find('.') + 1);
    if (extension.size() > 0) {
        if (extension != "txt" && extension != "exe" && extension != "dll") {
            isValid = false;
        }
    } else {
        isValid = false;
    }

    return isValid ? "Yes" : "No";
}