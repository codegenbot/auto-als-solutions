#include <sstream>
#include "md5.h"

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
    for (int i = 0; i < 16; ++i) {
        oss << std::hex << std::setfill('0') << std::setw(2) << (int)(result[i] & 0xFF);
    }

    return oss.str();
}