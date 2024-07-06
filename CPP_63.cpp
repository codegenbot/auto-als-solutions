#include <iostream>
using namespace std;

// Function declaration
int fibfib(int n);

int main()
{
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("FibFib number at position %d is %d\n", n, fibfib(n));
    return 0;
}

int fibfib(int n) {
    if (n == 0)
        return 0;
    else if (n == 1)
        return 1;
    else
        return fibfib(n - 1) + fibfib(n - 2);
}