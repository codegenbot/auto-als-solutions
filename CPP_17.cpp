#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> parse_music(string music_string) {
    vector<int> beats;
    string note;
    int beat = 0;

    for (char c : music_string) {
        if (c == 'o' || c == '.') {
            if (c == 'o') beat = 4;
            else beat = 1;
            beats.push_back(beat);
        } else if (c == '|') {
            if (note == "o") beat = 2;
            else beat = 1;
            beats.push_back(beat);
            note = "";
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