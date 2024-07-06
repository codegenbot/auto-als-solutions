Here is the completed code:

#include <bits/stdc++.h>

using namespace std;

int starts_one_ends(int n) {
    int count = 0;
    for (int i = 1; i <= 9; i++) {
        if (i == 1 || i % 10 == 1) count++;
        if (n > 1 && i == 1) count++;
        if (n > 1) {
            int num = i;
            for (int j = 2; j < n - 1; j++) {
                num = num * 10 + j;
            }
            if (num % 10 == 1 || num / pow(10, n-1) % 10 == 1) count++;
        }
    }
    return count;
}