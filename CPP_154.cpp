#include<string>
using namespace std;

bool cycpattern_check(string a, string b) {
    for(int i = 0; i < a.size(); i++) {
        for(int j = 0; j <= a.size() - b.size(); j++) {
            bool found = true;
            int k = 0;
            while (j + k < a.size() && j + k + b.size() <= a.size()) {
                if (a.substr(j + k, b.size()).compare(b) != 0) {
                    found = false;
                    break;
                }
                k++;
            }
            if(found) return true;
        }
    }
    return false;
}