string match_parens(vector<string> lst){
    stack<char> st;
    for(string s : lst){
        for(char c : s){
            if(c == '(') st.push(c);
            else if(c == ')'){
                if(st.empty()) return "No";
                st.pop();
            }
        }
    }
    return st.empty() ? "Yes" : "No";
}