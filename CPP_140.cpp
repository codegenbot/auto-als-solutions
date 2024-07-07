Here is the solution:

```cpp
string fix_spaces(string text){
    string result = "";
    for(int i=0; i<text.length();i++){
        if(text[i] == ' ' && (result.length() == 0 || result[result.length()-1] != ' ')){
            result += '_';
        } else {
            result += text[i];
        }
        if(i < text.length() - 1 && text[i] == ' ' && text[i+1] == ' '){
            int j = i + 1;
            while(j < text.length() && text[j] == ' ') j++;
            for(int k=i; k<j; k++) result += '-';
            i = j-1;
        }
    }
    return result;
}