#include<stdio.h>
#include<vector>
#include<algorithm>
#include<set>
using namespace std;

vector<int> unique(vector<int> l){
    set<int> s(l.begin(), l.end());
    return vector<int>(s.begin(), s.end());
}