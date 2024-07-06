```cpp
#include <openssl/ssl.h>
#include <openssl/x509v3.h>
#include <openssl/evp.h>
#include <sstream>
#include <string>

std::string string_to_md5(std::string text) {
    if (text.empty()) return "";

    unsigned char result[16];
    EVP_MD_CTX mdctx;
    EVP_MD *md = EVP_md5();
    EVP_SealInit(&mdctx, md, NULL, 0, &result[0], 16);
    EVP_SealFinal(&mdctx);
    std::stringstream ss;
    for (int i = 0; i < 16; i++) {
        ss << hex << setfill('0') << setw(2) << static_cast<int>(result[i]);
    }
    return ss.str();
}