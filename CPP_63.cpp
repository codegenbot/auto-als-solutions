```cpp
#include <stdio.h>

int fibfib(int n);  

int main() {
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("FibFib number at position %d is %d\n", n, fibfib(n));
    return 0;
}

int fibfib(int n) {
    if (n <= 1)
        return n;
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}