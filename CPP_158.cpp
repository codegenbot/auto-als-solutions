Here is the solution:

vector<string> max_words;

for (auto &word : words) {
    set<char> s(word.begin(), word.end());
    if (s.size() > max_words.size()) {
        max_words = {word};
    } else if (s.size() == max_words.size())
        max_words.push_back(word);
}

sort(max_words.begin(), max_words.end());

return *max_words.begin();