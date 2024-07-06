Here is the completed code:

```cpp
string encrypt(string s){
    string result = "";
    for(int i=0; i<s.length(); i++){
        if(s[i] >= 'a' && s[i] <= 'i'){
            result += (char)(((s[i]-'a'+26-2*2)%26)+'a');
        }
        else if(s[i] >= 'j' && s[i] <= 'm'){
            result += (char)(((s[i]-'j'+26-3*2)%26+'j'));
        }
        else if(s[i] >= 'n' && s[i] <= 'p'){
            result += (char)(((s[i]-'n'+26-4*2)%26+'n'));
        }
        else if(s[i] >= 'q' && s[i] <= 't'){
            result += (char)(((s[i]-'q'+26-5*2)%26+'q'));
        }
        else if(s[i] >= 'u' && s[i] <= 'x'){
            result += (char)(((s[i]-'u'+26-6*2)%26+'u'));
        }
        else if(s[i] >= 'y' && s[i] <= 'z'){
            result += (char)(((s[i]-'y'+26-7*2)%26+'y'));
        }
        else{
            result += s[i];
        }
    }
    return result;
}