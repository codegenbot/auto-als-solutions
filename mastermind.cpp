#include <vector>
#include <iostream>
#include <string>

int countBlackPegs(const std::string& code, const std::string& guess) {
    int blackPegs = 0;
    for (int i = 0; i < 4; ++i) {
        if (code[i] == guess[i]) {
            ++blackPegs;
        }
    }
    return blackPegs;
}

int countWhitePegs(const std::string& code, const std::string& guess) {
    int whitePegs = 0;
    std::map<char, int> codeCount;
    for (char c : code) {
        ++codeCount[c];
    }
    
    for (int i = 0; i < 4; ++i) {
        if (guess[i] == code[i]) {
            --codeCount[guess[i]];
        }
    }

    for (auto& pair : codeCount) {
        whitePegs += pair.second;
    }
    
    return whitePegs - blackPegs(countBlackPegs(code, guess), code);
}

int main() {
    std::string code, guess;
    std::cout << "Enter the Mastermind code: ";
    std::cin >> code;
    std::cout << "Enter a guess: ";
    std::cin >> guess;
    
    int blackPegs = countBlackPegs(code, guess);
    int whitePegs = countWhitePegs(code, guess);

    std::cout << whitePegs << '\n';
    std::cout << blackPegs << '\n';

    return 0;
}