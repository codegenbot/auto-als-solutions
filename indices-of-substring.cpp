#include <vector>
using namespace std;

vector<int> indicesOfSubstring(string text, string target) {
    vector<int> result;
    size_t pos = 0;
    
    while ((pos = text.find(target, pos)) != string::npos) {
        result.push_back(pos);
        pos += target.length();
    }
    
    return result;
}

int main() {
    int n;
    cin >> n;
    string text;
    for (int i = 0; i < n; ++i) {
        string str;
        cin >> str;
        if (i == 0)
            text = str;
        else
            text += "\n" + str;
    }
    
    string target;
    cin >> target;
    vector<int> indices = indicesOfSubstring(text, target);
    
    for (int i: indices) {
        cout << i << endl;
    }

    return 0;
}