#include<string>
using namespace std;

bool simplify(string x, string n) {
    int a = stoi(strtok((x.substr(1, x.find('/'))).c_str(), "/"));
    int b = stoi(x.substr(x.find('/') + 1));
    int c = stoi(strtok((n.substr(1, n.find('/'))).c_str(), "/"));
    int d = stoi(n.substr(n.find('/') + 1));

    if (a * d == b * c) {
        return true;
    } else {
        return false;
    }
}