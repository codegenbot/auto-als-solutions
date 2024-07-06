bool issame(vector<int> a, vector<int> b) {
    return a == b;
}

vector<int> filter_integers(vector<any> values) {
    vector<int> result;
    for (const auto& value : values) {
        if (any_cast<int>(value).good()) {
            result.push_back(any_cast<int>(value));
        }
    }
    return result;
}