```
#include <openssl/ssl.h>
#include <openssl/x509v3.h>
#include <openssl/evp.h>
#include <string>

std::string string_to_md5(std::string text) {
    if (text.empty()) return "";

    unsigned char result[16];
    MD5((unsigned const char*)text.c_str(), text.size(), result);
    std::stringstream ss;
    for (int i = 0; i < 16; i++) {
        ss << std::hex << std::setfill('0') << std::setw(2) << (int)result[i];
    }
    return ss.str();
}