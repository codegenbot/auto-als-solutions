#include <iostream>
#include <sstream>

using namespace std;

string toCamelCase(const string& str) {
    stringstream ss(str);
    string token, result;
    bool firstWord = true;

    while (getline(ss, token, '-')) {
        if (firstWord) {
            result += token;
            firstWord = false;
        } else {
            token[0] = toupper(token[0]);
            result += token;
        }
    }
    return result;
}

int main() {
    string input;
    getline(cin, input);
    stringstream ss(input);
    string word, output;

    while (ss >> word) {
        if (!output.empty()) output += " ";
        output += toCamelCase(word);
    }

    cout << output << endl;
    return 0;
}