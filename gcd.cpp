#include <iostream>
#include <vector>
#include <string>
#include <limits>

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
    // For gcd problem
    int a, b;
    cin >> a >> b;
    cout << gcd(a, b) << endl;
    
    // Clear input buffer before reading strings
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    
    // For substring indices problem
    string text, target;
    getline(cin, text);
    getline(cin, target);
    
    vector<int> indices = findSubstringIndices(text, target);
    for (int index : indices) {
        cout << index << " ";
    }
    cout << endl;
    
    return 0;
}