#include <stdio.h>
using namespace std;

int fib4(int n) {
    if (n <= 3) return 0;
    int prev3[] = {0, 0, 2};
    for (int i = 4; i <= n; i++) {
        int sum = prev3[0] + prev3[1] + prev3[2];
        prev3[0] = prev3[1];
        prev3[1] = prev3[2];
        prev3[2] = sum;
    }
    return prev3[2];
}

int main() {
    int n;
    printf("Enter the position of the number in the sequence: ");
    scanf("%d", &n);
    printf("The %dth element is %d.\n", n, fib4(n));
    return 0;
}