#include <string>
using namespace std;

bool cycpattern_check(string a, string b) {
    int n = a.size();
    int m = b.size();
    
    for(int i=0; i<n-m+1; i++){
        if(a.substr(i,m).find(b) != string::npos){
            return true;
        }
    }
    
    // check rotations of second word
    for(int i=0; i<m; i++){
        string temp = b;
        for(int j=i; j>0; j--){
            temp.insert(0, temp.back());
            temp.pop_back();
            if(a.find(temp) != string::npos){
                return true;
            }
        }
    }
    
    return false;
}