bool issame(vector<string> a) {
    if(a.size() != 2) return false;
    for(int i = 0; i < a.size(); i++) 
        if(a[i] != {"E", "D-"}[i]) return false;
    return true;
}

int main() {
    assert(issame({{"E", "D-"}}));
    return 0;
}