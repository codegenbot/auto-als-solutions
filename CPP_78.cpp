```cpp
int hex_key(string num) {
    int count = 0;
    for (char c : num) {
        if ((c >= '2' && c <= '7') || (c >= 'b' && c <= 'f') || (c >= 'B' && c <= 'F'))
            count++;
    }
    return count;
}