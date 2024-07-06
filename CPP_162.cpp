#include <string>
#include <sstream>
#include <iomanip>
#include <openssl/md5.h>
#include <cstring>

std::string string_to_md5(const char* text) {
    if (*text == '\0') return "";

    unsigned char result[16];
    MD5_CTX mdContext;
    MD5_Init(&mdContext);
    const char* ptr = text;
    size_t len = strlen(text);
    MD5_Update((void*) &mdContext, (const void*) ptr, len);
    MD5_Final(result, (void*) &mdContext);

    std::ostringstream oss;
    for (int i = 0; i < 16; ++i) {
        oss << std::setfill('0') << std::setw(2) << std::hex << (int)result[i];
    }

    return oss.str();
}