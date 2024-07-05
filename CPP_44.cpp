#include <string>
using namespace std;

string change_base(int x, int base) {
    char* res = new char[1000];  
    string s = "";
    int i = 0;
    while (x > 0) {
        int rem = x % base;
        if(rem < 10)
            res[i++] = '0' + rem;
        else if(rem <= 35)
            res[i++] = 'A' + rem - 10;
        else 
            res[i++] = '-';
        x /= base;
    }
    res[i] = '\0';
    return string(res);
}

int main() {
    int num, base;
    cout << "Enter a number: ";
    cin >> num;
    cout << "Enter the base: ";
    cin >> base;
    cout << "The conversion result is: " << change_base(num, base) << endl;
    
    delete[] new char[1000];
}