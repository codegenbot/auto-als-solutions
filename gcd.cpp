#include <iostream>
#include <vector>
#include <string>

using namespace std;

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

vector<int> findSubstringIndices(const string &text, const string &target) {
    vector<int> indices;
    size_t pos = text.find(target);
    while (pos != string::npos) {
        indices.push_back(pos);
        pos = text.find(target, pos + 1);
    }
    return indices;
}

int main() {
    int a, b;
    string text, target;
    
    // For gcd problem
    cin >> a >> b;
    cout << gcd(a, b) << endl;
    
    // For substring indices problem
    cin.ignore(); // To ignore the newline character after reading integers
    getline(cin, text);
    getline(cin, target);
    
    vector<int> indices = findSubstringIndices(text, target);
    for (int index : indices) {
        cout << index << " ";
    }
    cout << endl;
    
    return 0;
}