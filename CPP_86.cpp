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
        for(;j<=s.size() && s[j] != ''; j++){
            
        }
        string word = s.substr(i, j - i);
        char temp[word.length()+1];
        strcpy(temp,word.c_str());
        sort(temp,temp+word.length());
        result += temp;
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