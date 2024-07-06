#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tri(int n){
    vector<int> result(1);
    if(n == 0) return result;
    result.push_back(3);
    if(n == 1) return result;
    result.push_back(2);
    for(int i = 3; i <= n; i++){
        int val = (i % 2)? (result[i-1] + result[i-2] + (i+1)) : (int)((i/2.0)+1);
        result.push_back(val);
    }
    return result;
}