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
    
    char* binary = new char[64]; // Allocate space for the binary string
    int pos = 0; // Initialize a pointer to keep track of the position in the array
    while (avg > 0) {
        if (avg >= 2) {
            avg -= 2;
            binary[pos] = '1';
            pos++;
        } else {
            avg = 0;
            binary[pos] = '0';
            pos++;
        }
    }
    
    // Add a null terminator at the end of the array
    binary[pos] = '\0';
    
    return binary;
}