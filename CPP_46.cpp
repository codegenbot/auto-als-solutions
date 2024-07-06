#include <stdio.h>
using namespace std;

int fib4(int n) {
    if (n <= 3)
        return 0;
    int a = 0, b = 2, c = 0, d = 2, t;
    for (int i = 4; i <= n; i++) {
        t = a + b + c + d;
        a = b;
        b = c;
        c = d;
        d = t;
    }
    return d;
}

int main() {
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("Fib4(%d) is %d\n", n, fib4(n));
    return 0;
}