#include <string>

using namespace std;

string solve(int N) {
    string result = "";
    while (N > 0) {
        int remainder = N % 2;
        if (remainder == 1)
            result = "1" + result;
        else
            result = "0" + result;
        N /= 2;
    }
    return result;
}