#include <string>
#include <sstream>

using namespace std;

bool valid_date(string date) {
    int day, month, year;
    string s = "";
    
    for (int i = 0; i < date.length(); i++) {
        if (isdigit(date[i])) {
            s += date[i];
        } else if (!s.empty()) {
            break;
        }
    }
    
    if (s.length() == 2) {
        month = stoi(s);
        day = 1;
        year = 0;
    } else if (s.length() == 8) {
        month = stoi(s.substr(0, 2));
        day = stoi(s.substr(3, 2));
        year = stoi(s.substr(6, 4));
    } else {
        return false;
    }
    
    if (month < 1 || month > 12)
        return false;
    
    if ((month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) && day > 31)
        return false;
    else if ((month == 4 || month == 6 || month == 9 || month == 11) && day > 30)
        return false;
    else if (month == 2) {
        if (day > 29)
            return false;
    }
    
    return true;
}