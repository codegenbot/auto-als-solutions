string fix_spaces(string text){
    string result = "";
    for(int i=0; i < text.length(); i++){
        if(text[i] == ' ' && (i==0 || text[i-1] != ' ')){
            result += '_';
        } else if(text[i] == ' ' && (result.length() > 0) && (result[result.length()-1] != '_')){
            result = result.substr(0, result.length()-1);
            while(result.length() > 0 && result.back() == '_'){
                result.pop_back();
            }
            result += '-';
        } else {
            result += text[i];
        }
    }
    return result;
}