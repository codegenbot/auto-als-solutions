#include <string>
#include <algorithm>

using namespace std;

bool same_chars(string s0, string s1) {
    auto comp = [](char a, char b){ return (int)a - (int)b; };
    vector<char> v0(s0.begin(), s0.end());
    vector<char> v1(s1.begin(), s1.end());

    stable_partition(v0.begin(), v0.end(), [&comp](char c) {return comp(c) < 0; });
    stable_partition(v1.begin(), v1.end(), [&comp](char c) {return comp(c) > 0; });

    return v0 == v1;
}