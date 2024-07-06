int count_open = 0, count_close = 0;

for (char c : str) {
    if (c == '[') {
        count_open++;
    } else if (c == ']') {
        if (count_open > 0) {
            count_open--;
        } else {
            count_close++;
        }
    }
}

return count_close % 2 != 0;