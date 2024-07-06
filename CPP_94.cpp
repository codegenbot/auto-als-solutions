#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

int skjkasdkd(vector<int> lst){
    int max_prime = 0;
    for(int i : lst){
        if(i > 1 && isPrime(i)){
            max_prime = i;
            break;
        }
    }

    int sum_of_digits = 0;
    while(max_prime > 0){
        sum_of_digits += max_prime % 10;
        max_prime /= 10;
    }

    return sum_of_digits;
}

bool isPrime(int n) {
    if (n <= 1)
        return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}