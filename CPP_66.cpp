int digitSum(string s){
    int sum = 0;
    for(char c : s){
        if(isdigit(c) || isupper(c))
            sum += (isdigit(c))? c - '0' : tolower(c);
    }
    return sum;
}