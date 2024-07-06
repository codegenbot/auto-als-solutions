#include<string>
using namespace std;

bool cycpattern_check(string a, string b) {
    int lenA = a.length();
    int lenB = b.length();
    
    for(int i = 0; i < lenA - lenB + 1; i++) {
        string subStr = a.substr(i, lenB);
        
        if(subStr == b || isRotation(a, b)) {
            return true;
        }
    }
    
    return false;

}

bool isRotation(string a, string b) {
    if(a.length() != b.length()) {
        return false;
    }
    
    string temp = a + a; // add the string with itself to create rotations
    return (temp.find(b) != std::string::npos);
}