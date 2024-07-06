std::vector<int> filter_integers(std::list<std::any> values) {
    std::vector<int> result;
    for (const auto& value : values) {
        if (value.type() == typeid(std::optional<int>)) {
            try {
                int num = std::any_cast<std::optional<int>>(value).value();
                result.push_back(num);
            } catch(const std::bad_any_cast&) {
                // Ignore non-integer values
            }
        }
    }
    return result;
}