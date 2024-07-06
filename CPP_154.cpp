#include<string>
using namespace std;

bool cycpattern_check(string a, string b) {
    for (int i = 0; i < a.length() - b.length() + 1; i++) { 
        if (a.substr(i).compare(b.substr(0, a.length()-i)) == 0)
            return true;
    }
    return false;
}