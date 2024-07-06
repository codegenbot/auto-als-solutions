bool issame(vector<string> a,vector<string>b){
    return a==b;
}

int main() {
    vector<string> result = sorted_list_sum({"aaaa", "bbbb", "dd", "cc"});
    assert(issame(sort(result.begin(), result.end()), sort({"aaaa", "bbbb", "dd", "cc"}.begin(), {"aaaa", "bbbb", "dd", "cc"}.end())));
    return 0;
}