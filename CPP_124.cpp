#include <string>
using namespace std;

bool valid_date(string date) {
    int month, day, year;
    size_t pos = 0;
    pos = date.find('-');
    string mmdd = date.substr(0, pos);
    pos += 1;
    string yyyymmdd = date.substr(pos);
    pos = mmdd.find('-');
    month = stoi(mmdd.substr(0, pos));
    day = stoi(mmdd.substr(pos + 1));
    year = stoi(yyyymmdd);

    if (month < 1 || month > 12) {
        return false;
    }

    if ((month == 2 && day > 29) || 
        (month == 4 || month == 6 || month == 9 || month == 11) && day > 30 ||
        (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) && day > 31) {
        return false;
    }

    if (day < 1) {
        return false;
    }

    return true;
}