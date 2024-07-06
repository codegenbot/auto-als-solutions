#include <cstdio>
#include <vector>

using namespace std;

int prime_fib(int n) {
    vector<int> fib(1);
    int a = 0, b = 1;
    
    for (int i = 2; ; i++) {
        int temp = a + b;
        if (temp > n) break;
        fib.push_back(temp);
        a = b;
        b = temp;
    }
    
    return fib[n-1];
}

int main() {
    printf("%d\n", prime_fib(1));
    printf("%d\n", prime_fib(2));
    printf("%d\n", prime_fib(3));
    printf("%d\n", prime_fib(4));
    printf("%d\n", prime_fib(5));
    
    return 0;
}