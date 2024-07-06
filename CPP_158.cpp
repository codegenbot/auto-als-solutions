```cpp
#include <algorithm>
#include <iostream>
using namespace std;

string find_max(vector<string> words){
    string result = *max_element(words.begin(), words.end(),
        [](const string& a, const string& b) {
            int unique_a = a.size() - (set<char>(a.begin(), a.end())).size();
            int unique_b = b.size() - (set<char>(b.begin(), b.end())).size();
            return unique_a > unique_b;
        });
    return result;
}

int main(){
    cout << find_max({"play", "play", "play"}) << endl;
}