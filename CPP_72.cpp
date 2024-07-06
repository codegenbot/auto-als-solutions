#include <iostream>
#include <vector>
using namespace std;

bool will_it_fly(vector<int> q, int w) {
    string str = "";
    for (int i : q) {
        str += to_string(i);
    }
    if (!isPalindrome(str)) return false;
    int sum = 0;
    for (int i : q) {
        sum += i;
    }
    return sum <= w;
}

bool isPalindrome(string s) {
    string rev = s;
    reverse(rev.begin(), rev.end());
    return s == rev;
}

int main() {
    vector<int> q;
    int w;
    cout << "Enter the number of questions (q): ";
    cin >> q.size();
    for(int i=0; i<q.size(); ++i){
        cout << "Enter question " << i+1 << ": ";
        cin >> q[i];
    }
    cout << "Enter weight (w): ";
    cin >> w;
    if(will_it_fly(q, w)) {
        cout << "The answer will fly.\n";
    } else {
        cout << "The answer will not fly.\n";
    }
    return 0;
}