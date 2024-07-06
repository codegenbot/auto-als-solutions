#include <openssl/ssl.h>
#include <openssl/x509v3.h>
#include <openssl/evp.h>
#include <string>
#include <sstream>

std::string string_to_md5(std::string text) {
    if (text.empty()) return "";

    unsigned char result[16];
    EVP_MD_CTX mdctx;
    EVP_MD *md = EVP_md_md5();
    unsigned char *d;

    EVP_MD_CTX_init(&mdctx);
    EVP_DigestInit_ex(&mdctx, md, NULL);
    EVP_DigestUpdate(&mdctx, text.c_str(), text.size());
    EVP_DigestFinal_ex(&mdctx, result, &d);

    std::stringstream ss;
    for (int i = 0; i < 16; i++) {
        ss << hex << setfill('0') << setw(2) << (int)result[i];
    }
    return ss.str();
}