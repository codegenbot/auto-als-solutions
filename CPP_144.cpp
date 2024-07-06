#include<string>
using namespace std;

bool simplify(string x, string n) {
    int a = stoi(strtok(x.substr(1).c_str(), "/"));
    int b = stoi(strtok(NULL, "/"));
    int c = stoi(strtok(n.substr(1).c_str(), "/"));
    int d = stoi(strtok(NULL, "/"));

    long long m = (long long) a * d;
    long long n2 = (long long) b * c;

    if(m%n2==0) return true;
    else return false;
}