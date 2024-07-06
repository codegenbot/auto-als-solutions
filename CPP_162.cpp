```cpp
#include <string>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <openssl/md5.h>

using namespace std;

string string_to_md5(const char* text) {
    if (*text == '\0') return "";

    unsigned char result[16];
    MD5_CTX mdContext;
    MD5_Init(&mdContext);
    const char* ptr = text;
    size_t len = strlen(text);
    MD5_Update(&mdContext, (unsigned char*)text, len);
    MD5_Final(result, &mdContext);

    ostringstream oss;
    for (int i = 0; i < 16; ++i) {
        oss << setfill('0') << setw(2) << hex << (int)result[i];
    }

    return oss.str();
}