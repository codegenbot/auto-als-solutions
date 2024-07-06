#include<stdio.h>
#include<string>
using namespace std;

string file_name_check(string file_name) {
    int digitCount = 0;
    bool hasDot = false;
    int dotIndex = -1;
    
    for(int i = 0; i < file_name.length(); i++) {
        char c = file_name[i];
        
        if(c == '.') {
            hasDot = true;
            dotIndex = i;
        } else if(isdigit(c)) {
            digitCount++;
            if(digitCount > 3) return "No";
        }
    }
    
    if(!hasDot || dotIndex < 1 || !isalpha(file_name[0])) return "No";
    
    string extension = file_name.substr(dotIndex + 1);
    
    if(extension != "txt" && extension != "exe" && extension != "dll") return "No";
    
    return "Yes";
}