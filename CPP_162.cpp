```
struct MD5_CTX {
    unsigned int bytes_processed;
    unsigned int bits_processed;
    unsigned char state[4];
    unsigned char buffer[64];
};

#include <string>
#include <sstream>
#include <cstring>

// Forward declarations for the MD5 functions
void MD5_Init_early(MD5_CTX* ctx);
void MD5_Update(MD5_CTX* ctx, const unsigned char* ptr, size_t len);
void MD5_Final(unsigned char result[16], MD5_CTX* ctx);

std::string string_to_md5(const char* text) {
    if (*text == '\0') return "";

    unsigned char result[16];
    MD5_CTX mdContext;
    MD5_Init_early(&mdContext);
    const char* ptr = text;
    size_t len = strlen(text);
    MD5_Update(&mdContext, reinterpret_cast<const unsigned char*>(ptr), len); 
    MD5_Final(result, &mdContext);

    std::ostringstream oss;
    oss << std::hex | std::ios::fill('0');
    for (int i = 0; i < 16; ++i) {
        oss.width(2);
        oss << (int)result[i];
    }

    return oss.str();
}