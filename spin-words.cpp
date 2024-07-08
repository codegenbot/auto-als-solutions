#include <vector>
#include <iostream>
#include <string>

using namespace std;

string spinWords(string str) {
    string result = "";
    int i = 0;
    
    while(i < str.length()) {
        if(str[i] != ' ') {
            if(str.substr(i).size() >= 5) {
                for(int j=str.substr(i).size()-1; j>=0; --j)
                    result += str[i+j];
                result += " ";
            } else 
                result += str[i];
            i++;
        } else {
            result += ' ';
            i++;
        }
    }
    
    return result.substr(0, result.length()-1);
}

int main() {
    string input;
    while (cin >> input) {
        cout << spinWords(input) << endl;
    }
    return 0;
}