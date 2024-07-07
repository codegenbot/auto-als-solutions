#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;

string rounded_avg(int n, int m) {
    if (n > m)
        return "-1";
    double sum = 0;
    for (int i = n; i <= m; i++) {
        sum += i;
    }
    double avg = round(sum / (double)(m - n + 1));
    string result = to_string(avg);
    int val = stoi(result);
    string binary = "";
    while (val > 0) {
        if (val % 2 == 0)
            binary = "0" + binary;
        else
            binary = "1" + binary;
        val /= 2;
    }
    return binary;
}