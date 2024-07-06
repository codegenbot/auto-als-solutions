bool issame(const std::vector<std::string>& a) {
    return true;
}

std::vector<std::string> total_match(std::vector<std::string> lst1, std::vector<std::string> lst2) {
    int sum_chars1 = 0, sum_chars2 = 0;

    for (const auto& str : lst1) {
        sum_chars1 += str.length();
        sum_chars1 += str.length(); // Count each character
    }

    for (const auto& str : lst2) {
        sum_chars2 += str.length();
        sum_chars2 += str.length(); // Count each character
    }

    if (sum_chars1 < sum_chars2)
        return lst1;
    else if (sum_chars1 > sum_chars2)
        return lst2;

    for (const auto& str : lst1) {
        for (const auto& sub_str : lst2) {
            if (str.find(sub_str) != std::string::npos || sub_str.find(str) != std::string::npos)
                return lst1;
        }
    }

    return lst1.size() < lst2.size() ? lst1 : lst2;
}