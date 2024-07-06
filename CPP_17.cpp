#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> parse_music(string music_string) {
    vector<int> beats;
    int current_beat = 1;
    for (char c : music_string) {
        if (c == 'o') {
            beats.push_back(4);
            current_beat = 4;
        } else if (c == '|') {
            current_beat /= 2;
        }
    }
    return beats;
}

int main() {
    string s = "o o| .| o| o| .| .| .| .| o o";
    vector<int> result = parse_music(s);
    for (int i : result) {
        cout << i << " ";
    }
    return 0;
}