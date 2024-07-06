#include <string>

bool is_palindrome(string text){
    int i = 0;
    int j = text.length() - 1;

    while(i < j){
        if(tolower(text[i]) != tolower(text[j]))
            return false;
        i++;
        j--;
    }

    return true;
}