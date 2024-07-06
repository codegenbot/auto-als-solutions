```c++
bool issame(std::vector<int>& a, std::vector<int>& b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i < a.size(); ++i)
        if (abs(a[i] - b[i]) > 1)
            return false;
    return true;
}