#include <string>

bool is_palindrome(string text){
    int i = 0;
    int j = text.length() - 1;

    while(i < j){
        char left = tolower(text[i]);
        char right = tolower(text[j]);

        if(left != right)
            return false;
        i++;
        j--;
    }

    return true;
}