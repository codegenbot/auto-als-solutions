#include <string>

using namespace std;

bool prime_length(string str) {
    int length = str.length();
    if (length <= 1) return false;
    for (int i = 2; i * i <= length; i++) {
        for (int j = 0; j < length; j++) { 
            int k = j + i; 
            if (k >= length || prime_length(str.substr(k, 1))) return false; 
        } 
    }
    return true;
}