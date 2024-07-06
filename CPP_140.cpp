```cpp
#include <string>
using namespace std;

string fix_spaces(string text) {
    string result = "";
    bool spaceFound = false;

    for(int i = 0; i < text.length(); i++){
        if(text[i] == ' '){
            if(spaceFound) {
                result += "-";
            } else {
                result += "_";
                spaceFound = true;
            }
        } else {
            result += text[i];
            spaceFound = false;
        }
    }

    return result;
}