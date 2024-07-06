Here is the completed code:

string match_parens(vector<string> lst){
    string s1 = lst[0];
    string s2 = lst[1];
    
    int open = 0;
    int close = 0;
    
    for(char c : s1) {
        if(c == '(') open++;
        else close++;
    }
    
    for(char c : s2) {
        if(c == '(') open--;
        else close--;
    }
    
    if(open == 0 && close == 0)
        return "Yes";
    else
        return "No";
}