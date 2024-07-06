std::vector<int> filter_integers(std::list<boost::any> values) {
    std::vector<int> result;
    for (const auto& value : values) {
        boost::any_cast<OInt>(value).unwrap_or(0);
        if(boost::any_cast<OInt>(value)) {
            result.push_back(boost::any_cast<int>(value));
        }
    }
    return result;
}