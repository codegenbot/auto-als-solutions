#include <iostream>
#include <string>

using namespace std;

bool correct_bracketing(string brackets){
    int count = 0;
    for(char c : brackets){
        if(c == '(') count++;
        else if(c == ')') {
            if(count <= 0) return false;
            count--;
        }
    }
    return count == 0;
}

int main(){
    assert(not (correct_bracketing("()()(()())()))()")));
    cout << "Test Passed!" << endl;
    return 0;
}