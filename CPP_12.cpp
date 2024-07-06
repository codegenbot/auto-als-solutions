#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

string longest(vector<string> strings){
    if(strings.empty()) {
        return "";
    }
    string res = strings[0];
    for(int i=1; i<strings.size(); i++){
        if(res.length() < strings[i].length()){
            res = strings[i];
        } else if(res.length() == strings[i].length()){
            res = strings[i];
        }
    }
    return res;
}