#include <string>
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

cin >> w;
vector<int> q(5);
for(int i=0;i<5;i++)
{
    cin>>q[i];
}
if(will_it_fly(q,w))
cout<<"The airplane will fly";
else
cout<<"The airplane won't fly";