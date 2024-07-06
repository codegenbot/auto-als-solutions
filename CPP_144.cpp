bool simplify(string x, string n) {
    int a = 0, b = 0, c = 0, d = 0; 
    string s1, s2;
    
    // Split the strings into two numbers each
    for(int i = 0; i < x.length(); ++i) {
        if(x[i] == '/') break;
        if(x[i] != ' ') a = a*10 + (x[i]-'0');
    }
    for(int i = x.length()-1; i > 0; --i) {
        if(x[i] == '/') break;
        s1 += x[i];
    }
    
    for(int i = 0; i < n.length(); ++i) {
        if(n[i] == '/') break;
        if(n[i] != ' ') c = c*10 + (n[i]-'0');
    }
    for(int i = n.length()-1; i > 0; --i) {
        if(n[i] == '/') break;
        s2 += n[i];
    }
    
    // Calculate the gcd
    int temp;
    while(d != 0) {
        temp = d;
        d = a % d;
        a = temp;
    }
    temp = c;
    while(temp != 0) {
        d = c % d;
        c = temp;
        temp = d;
        d = a % d;
        a = temp;
    }
    
    // Check if the result is a whole number
    if(c/a == stoi(s1)/stoi(s2)) return true;
    else return false;
}