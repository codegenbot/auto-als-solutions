Here is the completed code:

```cpp
bool has_digit = false;
int dot_count = 0;

for (char c : file_name) {
    if (c == '.') {
        dot_count++;
        if (dot_count > 1) {
            return "No";
        }
    } else if (isdigit(c)) {
        has_digit |= true;
    } else if (!has_digit && !isalpha(c)) {
        return "No";
    }
}

if (has_digit || dot_count != 1) {
    return "No";
}

string extension = file_name.substr(file_name.find('.') + 1);
return extension == "txt" || extension == "exe" || extension == "dll" ? "Yes" : "No";