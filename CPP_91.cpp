```c++
#include <string>

int is_bored(std::string S) {
    int count = 0;
    size_t pos = 0;
    while ((pos = S.find("I", pos)) != std::string::npos) {
        if (S.find(".", pos) == std::string::npos && S.find("?", pos) == std::string::npos && S.find("!", pos) == std::string::npos)
            count++;
        pos = S.find(".", pos) + 1;
    }
    return count;
}

int main() {
    std::string input;
    std::cin >> input; // Read the string
    std::cin.ignore(); // Consume the newline character
    int result = is_bored(input);
    std::cout << "Count: " << result << std::endl;
    return 0;
}