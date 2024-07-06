#include <string>
#include <sstream>

using namespace std;

int fruit_distribution(string s, int n) {
    stringstream ss(s);
    int apples = 0;
    int oranges = 0;
    
    string token;
    while (getline(ss, token, ' ') && !token.empty()) {
        if (token.find("apples") != string::npos || token.find("AppleS") != string::npos) {
            if (token.find("and") == string::npos) {
                apples = stoi(token.substr(0, token.length() - 8));
            } else {
                apples = stoi(token.substr(0, token.find("and")));
            }
        } else if (token.find("oranges") != string::npos || token.find("OrangeS") != string::npos) {
            if (token.find("and") == string::npos) {
                oranges = stoi(token.substr(0, token.length() - 7));
            } else {
                oranges = stoi(token.substr(0, token.find("and")));
            }
        }
    }

    return n - apples - oranges;
}