bool issame(vector<string> a,vector<string>b){
    return a==b;
}

int main() {
    assert(issame({{"aaaa", "bbbb", "dd", "cc"}}, {{"cc", "dd", "aaaa", "bbbb"}}));
    vector<string> result = sorted_list_sum({"aaaa", "bbbb", "dd", "cc"});
    return 0;
}