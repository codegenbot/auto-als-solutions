string match_parens(vector<string> lst){
    int open = 0, close = 0;
    for(int i=0; i<lst.size(); i++){
        string s = lst[i];
        for(int j=0; j<s.length(); j++){
            if(s[j] == '(') open++;
            else if(s[j] == ')') close++;
        }
    }
    return (open == close) ? "Yes" : "No";
}