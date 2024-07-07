#include <vector>
using namespace std;

vector<int> indicesOfSubstring(string text, string target) {
    vector<int> result;
    int start = 0, end = 0;
    
    while ((end = text.find(target, start)) != string::npos) {
        result.push_back(end);
        start = end + 1;
    }
    
    return result;
}

int main() {
    // Example usage
    string text;
    int target_len;
    cin >> text >> target_len;
    string target(text.begin(), text.begin()+target_len);
    vector<int> indices = indicesOfSubstring(text, target);
    for(int i: indices) cout << i << " ";
    return 0;
}