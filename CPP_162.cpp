#include <iostream>
#include <sstream>
#include <string>
#include <openssl/md5.h>

using namespace std;

string string_to_md5(string text) {
    if (text.empty()) {
        return "";
    }

    MD5_CTX ctx;
    unsigned char md[16];
    MD5_Init(&ctx);
    const char *data = text.c_str();
    size_t length = text.size();
    MD5_Update(&ctx, data, length);
    MD5_Final(md, &ctx);

    stringstream ss;
    for (size_t i = 0; i < 16; ++i) {
        ss << setfill(2) << setw(2) << hex << static_cast<int>(md[i]);
    }

    return ss.str();
}