#include <vector>
#include <string>

bool issame(vector<string> a, vector<string> b){
    if(a.size() != b.size()) return false;
    for(auto str : a) {
        bool found = false;
        for(auto str2 : b) {
            if(str == str2) {
                found = true; break;
            }
        }
        if(!found) return false;
    }
    return true;
}

vector<string> filter_by_substring(vector<string> strings, string substring){
    vector<string> result;
    for(auto str : strings){
        if(str.find(substring) != string::npos){
            bool isSame = true;
            for(auto otherStr : result){
                if(!issame({str}, {otherStr})){
                    isSame = false; break;
                }
            }
            if(isSame) continue;
            result.push_back(str);
        }
    }
    return result;
}