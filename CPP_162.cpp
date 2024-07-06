#include <iostream>
#include <string>
#include <openssl/md5.h>

using namespace std;

string string_to_md5(string text) {
    if (text.empty()) return "";
    
    MD5_CTX ctx;
    unsigned char mdBuffer[16];
    MD5_Init(&ctx);
    const char *txt = text.c_str();
    MD5_Update(&ctx, txt, text.size());
    MD5_Final(mdBuffer, &ctx);
    string result;
    for (int i = 0; i < 16; i++) {
        stringstream ss;
        ss << hex << setfill('0') << setw(2) << (int)mdBuffer[i];
        result += ss.str();
    }
    return result;
}