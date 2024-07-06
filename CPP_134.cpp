bool check_if_last_char_is_a_letter(string txt){
    if(txt.empty()) return false;
    char last_char = txt.back();
    bool is_part_of_word = false;
    for(int i=0; i<txt.length(); i++){
        if(!isspace(txt[i])){
            is_part_of_word = true;
            break;
        }
    }
    return !isalpha(last_char) || is_part_of_word;
}