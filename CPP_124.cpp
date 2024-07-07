#include <string>
using namespace std;

bool valid_date(string date) {
    int day, month, year;
    char delimiter = '-';
    size_t pos = 0;
    
    // Split the string into three parts: month-day-year
    if ((pos = date.find(delimiter)) != string::npos) {
        string monthDay = date.substr(0, pos);
        string yearPart = date.substr(pos + 1);
        
        // Split the month-day part into two parts: month and day
        if ((pos = monthDay.find(delimiter)) != string::npos) {
            string monthStr = monthDay.substr(0, pos);
            day = stoi(monthDay.substr(pos + 1));
            
            // Check if the date is valid according to rules
            int mon = stoi(monthStr);
            if (mon < 1 || mon > 12)
                return false;
            
            if ((mon == 2 && day > 29) ||
                (mon == 4 || mon == 6 || mon == 9 || mon == 11) &&
                (day > 30))
                return false;
            
            // Check the day
            if ((mon == 1 || mon == 3 || mon == 5 || mon == 7 || 
                 mon == 8 || mon == 10 || mon == 12) && day > 31)
                return false;
        } else {
            return false; // Not in the correct format
        }
    } else {
        return false; // Not in the correct format
    }
    
    return true; // The date is valid
}