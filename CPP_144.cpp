#include<string>
using namespace std;

bool simplify(string x, string n) {
    int a = stoi(split(x)[0]);
    int b = stoi(split(x)[2]);
    int c = stoi(split(n)[0]);
    int d = stoi(split(n)[2]);

    return (a*d) == (b*c);
}

string split(string s) {
    size_t found = s.find('/');
    return s.substr(0,found);
}