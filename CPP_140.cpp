Here is the completed code:

string fix_spaces(string text){
    string result = "";
    bool wasSpace = false;

    for(int i = 0; i < text.length(); i++){
        if(text[i] == ' '){
            if(wasSpace || i == text.length() - 1) {
                result += "-";
            } else {
                wasSpace = true;
                result += '_';
            }
        }else{
            wasSpace = false;
            result += text[i];
        }
    }

    return result;
}