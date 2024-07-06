#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string find_max(vector<string> words){
    string max_str = *max_element(words.begin(), words.end(),
        [](const string& a, const string& b) {
            return count(a.begin(), a.end(), a[0]) > count(b.begin(), b.end(), b[0]);
        });
    return max_str;
}

int main() {
    assert ((find_max({"play", "play", "play"}) == "play"));
    return 0;
}