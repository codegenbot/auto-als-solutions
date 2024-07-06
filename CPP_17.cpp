#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> parse_music(string music_string) {
    vector<int> beats;
    for (int i = 0; i < music_string.length(); i++) {
        if (music_string[i] == 'o') {
            beats.push_back(4);
        } else if (music_string[i] == '|') {
            if (i > 0 && music_string[i - 1] != '.') {
                beats.push_back(2);
            } else {
                beats.push_back(1);
            }
        }
    }
    return beats;
}

int main() {
    string music_string = "o o| .| o| o| .| .| .| .| o o";
    vector<int> result = parse_music(music_string);
    for (int beat : result) {
        cout << beat << " ";
    }
    cout << endl;
    return 0;
}