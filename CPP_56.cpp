#include <string>
using namespace std;

bool correct_bracketing(string brackets){
    int opening = 0;
    for(char c : brackets) {
        if(c == '<' || c == '[') {
            opening++;
        } else if(c == '>' || c == ']') {
            if(opening <= 0)
                return false;
            opening--;
        }
    }
    return opening == 0;
}