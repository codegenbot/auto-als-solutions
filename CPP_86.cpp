```cpp
#include <string>
#include <algorithm>
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
        string temp = word;
        sort(temp.begin(), temp.end());
        result += temp;
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