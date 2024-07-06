```cpp
#include <string>
#include <openssl/evp.h>

std::string string_to_md5(const std::string& text) {
    if (text.empty()) return "";

    unsigned char md[16];
    unsigned char* str = reinterpret_cast<unsigned char*>(text.c_str());
    int len = text.length();
    EVP_MD_CTX ctx;
    EVP_MD_CTX_init(&ctx);
    EVP_DigestInit_ex(&ctx, EVP_md5(), NULL);
    EVP_DigestUpdate(&ctx, str, len);
    EVP_DigestFinal_ex(&ctx, md, &len);
    EVP_MD_CTX_cleanup(&ctx);

    std::string result = "";
    for (int i = 0; i < 16; i++) {
        char buffer[3];
        sprintf(buffer, "%02x", md[i]);
        result += buffer;
    }

    return result;
}