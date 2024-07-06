bool correct_bracketing(string brackets){
    int openCount = 0;
    for(int i=0; i<brackets.length(); i++){
        if(brackets[i] == '<') openCount++;
        else if(brackets[i] == '>'){
            if(openCount <= 0) return false;
            openCount--;
        }
    }
    return openCount == 0;
}