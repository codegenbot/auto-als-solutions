#include <iostream>
#include <string>
#include <vector>

using namespace std;

int gcd(int a, int b) {
    if (b == 0)
        return a;
    else
        return gcd(b, a % b);
}

vector<int> indicesOfSubstring(string text, string target) {
    vector<int> result;
    int n = text.length();
    int m = target.length();

    for (int i = 0; ; i++) {
        if (i + m > n) break;

        int j = 0;
        while (j < m && text[i + j] == target[j]) j++;

        if (j == m) result.push_back(i);
    }

    return result;
}

int main() {
    cout << "GCD of two numbers: " << gcd(48, 18) << endl;

    string text = "ABCABC";
    string target = "BC";
    vector<int> indices = indicesOfSubstring(text, target);

    cout << "Indices where '" << target << "' appears in '" << text << "': ";
    for (int i : indices) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}