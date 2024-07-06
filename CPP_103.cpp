#include <iostream>
#include<string>
#include <cmath>
#include <algorithm>

using namespace std;

string rounded_avg(int n,int m){
    if(n > m) return "-1";
    int sum = 0;
    for(int i=n; i<=m; i++){
        sum += i;
    }
    double avg = (double)sum / (m-n+1);
    int round_avg = floor(avg + 0.5);
    string res = "";
    while(round_avg > 0){
        if(round_avg & 1) res.push_back('1');
        else res.push_back('0');
        round_avg >>= 1;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    cout << rounded_avg(1,5) << endl; 
    cout << rounded_avg(7,5) << endl; 
    cout << rounded_avg(10,20) << endl; 
    cout << rounded_avg(20,33) << endl; 
    return 0;
}