vector<string> split_words(string txt) {
    vector<string> result;
    size_t pos = 0, prev_pos = 0;

    while ((pos = txt.find(' ', pos)) != string::npos) {
        result.push_back(txt.substr(prev_pos, pos - prev_pos));
        prev_pos = pos + 1;
    }

    if (prev_pos < txt.length()) {
        result.push_back(txt.substr(prev_pos));
    } else if (txt.empty() || txt.find(',') == string::npos) {
        int count = 0;
        for (char c : txt) {
            if (c >= 'a' && c <= 'z' && (count & 1)) {
                count++;
            }
        }
        result.push_back(to_string(count));
    } else {
        vector<string> words;
        size_t pos = 0, prev_pos = 0;

        while ((pos = txt.find(',', pos)) != string::npos) {
            words.push_back(txt.substr(prev_pos, pos - prev_pos));
            prev_pos = pos + 1;
        }

        if (prev_pos < txt.length()) {
            words.push_back(txt.substr(prev_pos));
        }

        result = words;
    }

    return result;
}