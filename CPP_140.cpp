string fix_spaces(string text){
    string result = "";
    for(int i=0; i<text.length(); i++){
        if(text[i] == ' ' && (result.empty() || (i > 0 && result[result.length()-1] != ' ') || i >= text.length()-2)){
            result += '_';
        }else{
            result += text[i];
        }
    }
    return result;
}