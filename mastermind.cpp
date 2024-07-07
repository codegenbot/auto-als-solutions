#include <iostream>
#include <vector>
#include <string>

using namespace std;

int whitePegs(string code, string guess) {
    int count = 0;
    for (int i = 0; i < 4; i++) {
        if (code[i] == guess[i]) {
            count++;
        }
    }
    return count;
}

int blackPegs(string code, string guess) {
    int count = 0;
    vector<char> codeVec(code.begin(), code.end());
    for (int i = 0; i < 4; i++) {
        if (code[i] == guess[i]) {
            codeVec[i] = ' ';
        }
    }
    for (int i = 0; i < 4; i++) {
        bool found = false;
        for (int j = 0; j < 4; j++) {
            if (guess[j] == codeVec[i] && guess[j] != ' ') {
                found = true;
                break;
            }
        }
        if (!found) {
            count++;
        }
    }
    return count;
}

int main() {
    string code, guess;
    cin >> code >> guess;
    cout << blackPegs(code, guess) << endl;
    cout << whitePegs(code, guess) << endl;
    return 0;