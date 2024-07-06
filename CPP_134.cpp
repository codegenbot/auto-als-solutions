Here is the completed code:

bool check_if_last_char_is_a_letter(string txt){
    if(txt.length() == 0)
        return false;

    char lastChar = txt.back();

    if(!isalpha(lastChar))
        return true;

    for(int i=0; i<txt.length()-1; i++){
        if(isspace(txt[i]) && !ispunct(txt[i+1]))
            return false;
    }

    return true;
}