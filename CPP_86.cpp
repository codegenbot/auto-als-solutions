```cpp
#include <vector>
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
        for(;j<s.size() && s[j] != ''; j++){
            
        }
        vector<char> word(s.begin() + i, s.begin() + j);
        sort(word.begin(), word.end());
        result += string(word.begin(), word.end());
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