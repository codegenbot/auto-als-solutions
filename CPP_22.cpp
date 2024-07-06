bool issame(vector<any> a, vector<any> b) {
    return std::equal(a.begin(), a.end(), b.begin(), [](const auto& x, const auto& y){return *x == *y;});
}

vector<int> filter_integers(vector<any> values) {
    vector<int> result;
    for (const auto& value : values) {
        if (any_cast<int>(value).has_value()) {
            result.push_back(any_cast<int>(value));
        }
    }
    return result;
}