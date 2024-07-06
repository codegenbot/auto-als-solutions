#include <string>
#include <vector>

using namespace std;

bool simplify(string x, string n) {
    int a = 0, b = 1, c = 0, d = 1;
    int numerator = 0, denominator = 0;
    
    // Convert the strings to integers
    string str = "";
    for(int i=1; i<x.size(); i++){
        if(x[i] == '/'){
            a = stoi(str);
            break;
        }
        str += x[i];
    }
    str = "";
    for(int i=x.size()-1; i>=0; i--){
        if(x[i] == '/'){
            break;
        }
        str = x[i] + str;
    }
    b = stoi(str);

    str = "";
    for(int i=1; i<n.size(); i++){
        if(n[i] == '/'){
            c = stoi(str);
            break;
        }
        str += n[i];
    }
    str = "";
    for(int i=n.size()-1; i>=0; i--){
        if(n[i] == '/'){
            break;
        }
        str = n[i] + str;
    }
    d = stoi(str);

    // Calculate the greatest common divisor
    numerator = a * d;
    denominator = b * c;

    // Check if the result is an integer
    int gcd = __gcd(numerator, denominator);
    return gcd == 1;
}