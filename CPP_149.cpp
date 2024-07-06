bool issame(vector<string> a,vector<string>b){
    return a==b;
}

int main() {
    vector<string> a = {"aaaa", "bbbb", "dd", "cc"};
    vector<string> b = {"cc", "dd", "aaaa", "bbbb"};
    sort(a.begin(),a.end());
    sort(b.begin(),b.end());
    assert(issame(a,b));
    vector<string> result = sorted_list_sum({"aaaa", "bbbb", "dd", "cc"});
    return 0;
}