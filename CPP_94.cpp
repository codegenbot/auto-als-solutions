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
    
    std::cout << "Enter the numbers (space separated): ";
    while(std::cin >> num) {
        lst.push_back(num);
        if(std::cin.peek() == ' ') {
            std::cin.ignore();
        } else if(std::cin.peek() != '\n') {
            break;
        }
    }
    
    int result = skjkasdkd(lst);
    std::cout << "The sum of the digits of the maximum prime number is: " << result << std::endl;

    return 0;
}