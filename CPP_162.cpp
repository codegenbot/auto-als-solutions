```cpp
#include <sstream>
#include <cstring>

std::string readInput() {
    std::string input;
    char buffer[256];
    while (true) {
        fgets(buffer, sizeof(buffer), stdin);
        input = buffer;
        if (input[input.size() - 1] == '\n') break;  // To handle the newline character
    }
    return input;
}

int main() {
    std::string text = readInput();
    std::cout << "MD5 of entered text: " << string_to_md5(text.c_str()) << std::endl;
    return 0;
}