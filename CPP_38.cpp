#include <stdio.h>
#include <string>
using namespace std;

string encode_cyclic(string s) {
    int l = s.length();
    int num = (l + 2) / 3;
    string x, output;
    int i;
    for (i = 0; i * 3 < l; i++) {
        // cycle elements in each group. Unless group has fewer elements than 3.
        x = s.substr(i * 3, 3);
        if (x.length() == 3) x = x.substr(1) + x[0];
        output += x;
    }
    return output;
}

string decode_cyclic(string s) {
    int l = s.length();
    string output;
    for (int i = 0; i < l; ) {
        if (i * 3 + 2 <= l)
            output += s.substr(i * 3, 3);
        else
            output += s.substr(i * 3) + s.substr(0, 3 - (l - i * 3));
        i++;
    }
    return output;
}