```cpp
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string anti_shuffle(string s){
    string result = "";
    for(int i=0; i<s.size(); i++){
        if(s[i] == ' '){
            result += ' ';
            continue;
        }
        string word = "";
        for(int j=i; j<s.size() && s[j] != ' '; j++){
            word += s[j];
        }
        i = j - 1;
        sort(word.begin(), word.end());
        result += word;
    }
    return result;
}

int main(){
    string input;
    cout << "Enter a sentence: ";
    cin >> input;
    cout << "Anti-shuffled sentence: " << anti_shuffle(input) << endl;
    return 0;
}