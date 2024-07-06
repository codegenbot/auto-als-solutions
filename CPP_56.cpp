int stackSize = 0;
char top;

for(int i = 0; i < brackets.length(); i++) {
    if(brackets[i] == '<') {
        stackSize++;
        if(stackSize > 1) return false;
        top = '<';
    } else if(brackets[i] == '>') {
        if(stackSize == 0) return false;
        if(top != '<') return false;
        stackSize--;
    }
}

return (stackSize == 0);