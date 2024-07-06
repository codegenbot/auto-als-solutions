#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> unique(vector<int> l){
    vector<int> result;
    for(int i=0; i<l.size(); i++){
        bool flag = true;
        for(int j=0; j<result.size(); j++){
            if(l[i] == result[j]){
                flag = false;
                break;
            }
        }
        if(flag) result.push_back(l[i]);
    }
    sort(result.begin(), result.end());
    return result;
}