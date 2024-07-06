#include <string>
#include <cctype>

string flip_case(string str){
    string result = "";
    for (int i = 0; i < str.length(); i++) {
        char c = str[i];
        if (islower(c)) 
            result += toupper(c);
        else if (isupper(c))
            result += tolower(c);
        else
            result += c;
    }
    return result;
}

int main() {
    string input;
    cout << "Enter a string: ";
    getline(cin, input);
    cout << flip_case(input) << endl;
    return 0;
}