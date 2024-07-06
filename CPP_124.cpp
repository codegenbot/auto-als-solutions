#include <string>
#include <vector>

using namespace std;

bool valid_date(string date) {
    vector<string> parts = split(date, '-');
    int month = stoi(parts[0]);
    int day = stoi(parts[1]);
    int year = stoi(parts[2]);

    if (month < 1 || month > 12)
        return false;
    else if ((month == 2 && day > 29) || 
             (month == 4 || month == 6 || month == 9 || month == 11) && day > 30 || 
             (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) && day > 31)
        return false;

    return true;
}

vector<string> split(const string& str, char ch) {
    vector<string> tokens;
    string token;
    for (char c : str) {
        if (c == ch) {
            tokens.push_back(token);
            token = "";
        } else {
            token += c;
        }
    }
    tokens.push_back(token);
    return tokens;
}