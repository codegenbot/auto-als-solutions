#include <iostream>
#include <vector>

int skjkasdkd(std::vector<int> lst){
    int maxPrime = 0;
    for(int i : lst){
        if(isPrime(i) && i > maxPrime)
            maxPrime = i;
    }
    return sumOfDigits(maxPrime);
}

bool isPrime(int n){
    if(n <= 1) 
        return false; 
    else {
        for (int i = 2; i * i <= n; i++) 
            if (n % i == 0) 
                return false;
        return true;
    }
}

int sumOfDigits(int n){
    int sum = 0;
    while(n > 0){
        sum += n%10;
        n /= 10;
    }
    return sum;
}

int main(){
    std::vector<int> lst;
    int num;
    
    // Read the numbers from user
    std::cout << "Enter a series of integers (enter 'q' to stop):" << std::endl;
    while(true){
        std::cin >> num;
        if(num == 'q')
            break;
        lst.push_back(num);
    }
    
    std::cout << "The sum of the digits of the maximum prime number is: " << skjkasdkd(lst) << std::endl;
    
    return 0;
}