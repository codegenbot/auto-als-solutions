#include <string>
#include <sstream>

struct MD5_CTX {
    unsigned char md5Variables[16];
};

void MD5_Init_early(MD5_CTX* ctx) {
    // implement this function
}

void MD5_Update(MD5_CTX* ctx, const unsigned char* ptr, size_t len) {
    // implement this function
}

void MD5_Final(unsigned char result[16], MD5_CTX* ctx) {
    // implement this function
}

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
    oss << std::hex;
    for (int i = 0; i < 16; ++i) {
        oss.fill('0');
        oss.width(2);
        oss << static_cast<int>(result[i]);
    }

    return oss.str();
}