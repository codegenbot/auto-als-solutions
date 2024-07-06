Here is the completed code:

```cpp
#include <openssl/ssl.h>
#include <openssl/rand.h>

string string_to_md5(string text) {
    unsigned char buffer[16];
    MD5_CTX ctx;
    MD5Init(&ctx);
    const char* str = text.c_str();
    size_t length = text.size();
    unsigned char data[length + 1];
    memcpy(data, str, length);
    data[length] = '\0';
    MD5Update(&ctx, (unsigned char*)data, length);
    MD5Final(buffer, &ctx);

    stringstream ss;
    for (int i = 0; i < 16; i++) {
        ss << hex << setfill('0') << fixed << setw(2) << (int)(buffer[i]);
    }

    return ss.str();
}