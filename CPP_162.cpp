#include <openssl/ssl.h>
#include <openssl/x509v3.h>
#include <openssl/evp.h>
#include <string>

std::string string_to_md5(std::string text) {
    if (text.empty()) return "";

    unsigned char result[16];
    EVP_MD_CTX md_ctx;
    EVP_MD *md = EVP_md5();
    EVP_MD_CTX_init(&md_ctx);
    EVP_DigestUpdate(&md_ctx, text.c_str(), text.size());
    EVP_DigestFinal_ex(&md_ctx, result, nullptr);
    EVP_MD_CTX_cleanup(&md_ctx);

    std::stringstream ss;
    for (int i = 0; i < 16; i++) {
        ss << hex << setfill('0') << setw(2) << (int)result[i];
    }
    return ss.str();
}