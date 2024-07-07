string fix_spaces(string text) {
    string result = "";
    bool prev_was_space = false;

    for (char c : text) {
        if (c == ' ') {
            if (!prev_was_space) {
                result += '_';
                prev_was_space = true;
            } else if (result.back() != '-') {
                result += '-';
                prev_was_space = true;
            }
        } else {
            if (prev_was_space) {
                result += c;
                prev_was_space = false;
            } else {
                result += c;
            }
        }
    }

    return result;
}