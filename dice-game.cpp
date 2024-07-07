#include <vector>
using namespace std;

double diceGame(int n, int m) {
    double total = (double)n * m;
    double p = 0.0;
    
    if(n > m) {
        p += (n - m) / total;
    }
    else if(m > n) {
        p += (m - n) / total;
    }
    
    return p;
}