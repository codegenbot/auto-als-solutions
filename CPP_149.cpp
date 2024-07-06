```cpp
bool issame(vector<string> a,vector<string>b){
    return a==b;
}

int main() {
    assert(issame({{"aaaa", "bbbb", "dd", "cc"}}, {{"cc", "dd", "aaaa", "bbbb"}}));
    // Call the function here
    vector<string> result = sorted_list_sum({"aaaa", "bbbb", "dd", "cc"});
    return 0;
}

vector<string> sorted_list_sum(vector<string> lst) {
    vector<string> result;

    // Remove strings with odd lengths from the list
    for (const string& str : lst) {
        if (str.length() % 2 == 0) {
            result.push_back(str);
        }
    }

    // Sort the resulting list by length and then alphabetically
    sort(result.begin(), result.end(),
         [](const string& a, const string& b) {
             if (a.length() != b.length()) {
                 return a.length() < b.length();
             } else {
                 return a < b;
             }
         });

    return result;
}