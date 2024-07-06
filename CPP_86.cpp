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
        string word = "";
        for(int j=i; j<s.size() && s[j] != ' '; j++){
            word += s[j];
        }
        i = j;
        sort(word.begin(), word.end());
        result += s.substr(i, j - i);
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