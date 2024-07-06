#include <stdio.h>
using namespace std;

int modp(int n, int p) {
    if (n == 0)
        return 1;
    else if ((n & 1) == 0)
        return modp(n / 2, p) * modp(n / 2, p) % p;
    else
        return (n % p) * modp((n - 1) / 2, p) * modp((n - 1) / 2, p) % p;
}

int main() {
    int n, p;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("Enter the value of p: ");
    scanf("%d", &p);
    printf("2^%d mod %d is %d\n", n, p, modp(n, p));
    return 0;
}