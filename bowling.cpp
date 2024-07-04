#include <iostream>
#include <string>

using namespace std;

int scoreBowling(const string& frames) {
    int score = 0, frame = 0, i = 0;
    while (frame < 10) {
        if (frames[i] == 'X') {
            score += 10 + (frames[i + 1] == 'X' ? 10 : (frames[i + 1] == '/' ? 10 - (frames[i] - '0') : frames[i + 1] - '0')) + (frames[i + 2] == 'X' ? 10 : (frames[i + 2] == '/' ? 10 - (frames[i + 1] - '0') : frames[i + 2] - '0'));
            i++;
        } else if (frames[i + 1] == '/') {
            score += 10 + (frames[i + 2] == 'X' ? 10 : frames[i + 2] - '0');
            i += 2;
        } else {
            score += (frames[i] - '0') + (frames[i + 1] - '0');
            i += 2;
        }
        frame++;
    }
    return score;
}

int main() {
    string input;
    cin >> input;
    cout << scoreBowling(input) << endl;
    return 0;
}