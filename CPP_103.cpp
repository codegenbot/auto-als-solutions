```c++
#include <cmath>
#include <string> 
using namespace std;

char* rounded_avg(int n, int m) {
    if (n > m) return "-1";
    
    double sum = 0;
    for (int i = n; i <= m; i++) {
        sum += i;
    }
    
    double avg = round(sum / (m - n + 1));
    
    char* binary = new char[log2(abs(avg)) + 1];
    binary[0] = '\0';
    while (avg > 0) {
        if (avg >= 2) {
            avg -= 2;
            strcat(binary, "1");
        } else {
            avg = 0;
            strcat(binary, "0");
        }
    }
    
    return binary;
}