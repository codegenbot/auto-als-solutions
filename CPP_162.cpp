#include <openssl/ssl.h>
#include <openssl/rand.h>

string string_to_md5(string text) {
    if (text.empty()) return "";

    unsigned char buffer[16];
    MD5_CTX md5;
    MD5_Init(&md5);
    const char* str = text.c_str();
    size_t len = text.length();
    MD5_Update(&md5, str, len);
    MD5_Final(buffer, &md5);

    string result;
    for (int i = 0; i < 16; i++) {
        char temp[3];
        sprintf(temp, "%02x", buffer[i]);
        result += temp;
    }

    return result;
}