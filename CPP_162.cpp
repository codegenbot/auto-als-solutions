Here is the completed code:

#include <string>
#include <sstream>

std::string string_to_md5(std::string text) {
    if (text.empty()) return "";
    
    unsigned char md[16];
    MD5_CTX ctx;
    MD5_Init(&ctx);
    const char* txt = text.c_str();
    size_t len = text.length();
    MD5_Update(&ctx, txt, len);
    MD5_Final(md, &ctx);
    
    std::stringstream ss;
    for (int i = 0; i < 16; ++i) {
        ss << hex << (int)md[i];
    }
    return ss.str();
}