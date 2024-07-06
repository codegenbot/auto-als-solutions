int closest_integer(string value) {
    double num = stod(value);
    if (num - static_cast<int>(num) < static_cast<int>(num) - (num + 1)) {
        return static_cast<int>(num);
    } else {
        return static_cast<int>(num) + 1;
    }
}