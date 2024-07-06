#include <string>
#include <sstream>

using namespace std;

int fruit_distribution(string s, int n) {
    stringstream ss(s);
    string word;
    int total_apples = 0, total_oranges = 0;
    
    while (getline(ss, word, ' ')) {
        if (word.find("apples") != string::npos) {
            istringstream iss(word);
            iss >> word;
            total_apples = stoi(word);
        } else if (word.find("oranges") != string::npos) {
            istringstream iss(word);
            iss >> word;
            total_oranges = stoi(word);
        }
    }

    return n - total_apples - total_oranges;
}