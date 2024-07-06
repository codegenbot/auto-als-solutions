#include <string>
#include <cctype>

string flip_case(string str){
    string result = "";
    for (int i = 0; i < str.length(); i++) {
        char c = str[i];
        if (c >= 'a' && c <= 'z') 
            result += toupper(c);
        else if (c >= 'A' && c <= 'Z')
            result += tolower(c);
        else
            result += c;
    }
    return result;
}

int main() {
    string str;
    cout << "Enter a sentence: ";
    getline(cin, str);
    cout << flip_case(str) << endl;
    return 0;
}