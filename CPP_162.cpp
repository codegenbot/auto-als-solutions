#include <string>
#include <openssl/evp.h>

#include <iomanip>
#include <sstream>

std::string string_to_md5(std::string text) {
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
        std::stringstream buffer;
        buffer << std::hex << std::setw(2) << std::setfill('0') << (unsigned int)md[i];
        result += buffer.str();
    }

    return result;
}

int main() {
    assert(string_to_md5("password") == "5f4dcc3b5aa765d61d8327deb882cf99");
    return 0;
}