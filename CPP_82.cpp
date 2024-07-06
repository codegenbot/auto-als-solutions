#include<iostream>
using namespace std;

bool prime_length(string str) {
    int len = str.length();
    bool isPrime = true;

    for (int i = 2; i * i <= len && isPrime; i++) {
        if (len % i == 0)
            isPrime = false;
    }

    return isPrime;
}

int main() {
    string str;
    cout << "Enter a string: ";
    getline(cin, str);
    
    if(prime_length(str)) 
        cout << "The length of the string is prime." << endl; 
    else
        cout << "The length of the string is not prime." << endl;

    return 0;
}