```cpp
bool is_nested(std::string str) {
    int count = 0;
    for (char c : str) {
        if (c == '[') count++;
        else if (c == ']') {
            if (count > 1) return false; 
            count--;
        }
    }
    return count > 0;
}