#include <vector>
#include <string>

bool issame(vector<string> a,vector<string>b){
    if(a.size() != b.size())return false;
    for(int i=0;i<a.size();i++)if(a[i]!=b[i])return false;
    return true;
}

vector<string> split_words(string txt) {
    vector<string> result;
    size_t pos = 0;
    while ((pos = txt.find(' ')) != string::npos) {
        result.push_back(txt.substr(0, pos));
        txt.erase(0, pos + 1);
    }
    if (txt.empty()) {
        return result;
    }
    result.push_back(txt);
    return result;
}

int main() {
    assert (issame(split_words("") ,{"0"}));
    return 0;
}