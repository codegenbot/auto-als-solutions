size_t lastSpace = txt.find_last_of(' ');
if (lastSpace == string::npos) {
    return isalpha(txt.back());
} else {
    char c = txt.back();
    if (!isalpha(c)) {
        return true;
    } else if (txt.size() - 1 > lastSpace) {
        for (size_t i = lastSpace + 1; i < txt.size(); ++i) {
            if (!isalpha(txt[i])) {
                return false;
            }
        }
        return true;
    }
    return false;
}