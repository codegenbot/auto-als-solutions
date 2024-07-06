#include <string>

int is_bored(std::string S){
    int count = 0;
    size_t pos = 0;
    while ((pos = S.find("I", pos)) != std::string::npos) {
        if (S.find(".", pos) == std::string::npos && S.find("?", pos) == std::string::npos && S.find("!", pos) == std::string::npos)
            count++;
        pos = S.find(". ", pos) + 1; // update the position
    }
}

int main() {
    std::string input;
    std::cout << "Enter a sentence: ";
    std::getline(std::cin, input);
    int output = is_bored(input);
    std::cout << "The count of bored sentences is: " << output << std::endl;
    return 0;
}