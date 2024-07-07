#include <vector>
using namespace std;

vector<int> indicesOfSubstring(string text, string target) {
    vector<int> result;
    int n = text.length(), m = target.length();
    for (int i = 0; ; i++) {
        if (i + m > n) break;
        int j = 0;
        while (j < m && text[i + j] == target[j]) j++;
        if (j == m) result.push_back(i);
    }
    return result;
}

int gcd(int a, int b) {
    if (b == 0)
        return a;
    else
        return gcd(b, a % b);
}

int main() {
    int num1, num2;
    cin >> num1 >> num2;

    // Output of GCD calculation
    cout << gcd(num1, num2) << endl;

    string text, target;
    cin >> text >> target;

    // Output of indices of substring
    vector<int> result = indicesOfSubstring(text, target);
    for (int i : result)
        cout << i << " ";
    cout << endl;

    return 0;
}