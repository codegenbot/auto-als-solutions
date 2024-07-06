bool issame(vector<string> a,vector<string>b){
    return a==b;
}

int main() {
    vector<string> input = {"aaaa", "bbbb", "dd", "cc"};
    assert(issame(sorted({input.begin(), input.end()}), sorted({"cc", "dd", "aaaa", "bbbb"})));
    vector<string> result = sorted_list_sum(input);
    return 0;
}