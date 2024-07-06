#include <iomanip>
#include <iostream>

using namespace std;

string string_to_md5(string text) {
    if (text.empty()) return "None";

    MD5_CTX ctx;
    unsigned char mdValue[16];

    MD5_Init(&ctx);
    const char* ptr = text.c_str();
    size_t len = text.length();

    MD5_Update(&ctx, ptr, len);

    MD5_Final(mdValue, &ctx);

    string result;
    for (int i = 0; i < 16; ++i) {
        stringstream ss;
        ss << setfill('0') << setw(2) << hex << (int)mdValue[i];
        result += ss.str();
    }

    return result;
}