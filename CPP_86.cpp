#include <algorithm>
using namespace std;

string anti_shuffle(string s) {
    string result = "";
    for(int i=0; i<s.size(); i++){
        if(s[i] == ' '){
            result += ' ';
            continue;
        }
        vector<char> word;
        for(int j=i; j<s.size() && s[j] != ' '; j++){
            word.push_back(s[j]);
        }
        i = j - 1;
        sort(word.begin(), word.end());
        result += string(word.begin(), word.end());
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