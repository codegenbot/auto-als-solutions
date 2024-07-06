#include <bits/stdc++.h>

using namespace std;

int fibfib(int n) {
    if(n == 0 || n == 1)
        return 0;
    int a = 0, b = 1, c = 0;
    for(int i=2; i<=n; ++i){
        c = a+b+a;
        a=b;
        b=c;
    }
    return c;
}