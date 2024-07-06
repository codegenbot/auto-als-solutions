bool correct_bracketing(string brackets){
    int opening = 0;
    for(int i=0; i<brackets.length(); i++){
        if(brackets[i] == '<') opening++;
        else if(opening > 0) opening--;
        if(opening < 0) return false;
    }
    return opening == 0;
}