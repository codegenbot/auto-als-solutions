```cpp
#include <string>
#include <algorithm>
using namespace std;

string anti_shuffle(string s){
    string result = "";
    int i = 0;
    while(i<s.size()){
        if(s[i] == ' '){
            result += ' ';
            i++;
            continue;
        }
        int j = i + 1;
        for(;j<=s.size() && s[j-1] != ' '; j++){
            
        }
        string word = s.substr(i, j - i);
        for(int k=0; k<word.size(); k++){
            result += word[k];
        }
        sort(word.rbegin(), word.rend());
        result += word;
        i = j;
    }
    return result;
}

int main(){
    string str;
    cout << "Enter a sentence: ";
    getline(cin, str);
    string output = anti_shuffle(str);
    cout << "Antishuffled sentence: " << output << endl;
    return 0;
}