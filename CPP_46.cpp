#include <stdio.h>
using namespace std;

int fib4(int n) {
    if (n <= 0)
        return 0;
    int a = 0, b = 2, c = 0, d = 2;
    for (int i = 1; i < n; i++) {
        int temp = a + b + c + d;
        a = b;
        b = c;
        c = d;
        d = temp;
    }
    return d;
}

int main() {
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    printf("Fib4(%d) = %d\n", n, fib4(n));
    return 0;
}