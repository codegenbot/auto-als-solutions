std::string string_sequence(int n) {
    std::ostringstream oss;
    for (int i = 1; i <= n; ++i) {
        if(i != 1)
            oss << " ";
        oss << i;
    }
    oss << std::endl; 
    return oss.stream();