#include <cstring>

std::string string_to_md5(const char* text) {
    if (*text == '\0') return "";

    unsigned char result[16];
    MD5_CTX mdContext;
#ifndef OPENSSL_3_0_0_OR_LATER
    MD5_Init(&mdContext);
#endif
    const char* ptr = text;
    size_t len = strlen(text);
    #ifndef OPENSSL_3_0_0_OR_LATER
    MD5_Update(&mdContext, ptr, len);
    #endif
#ifndef OPENSSL_3_0_0_OR_LATER
    MD5_Final(result, &mdContext);
#else
    // Use new functions (not shown here)
#endif

    std::ostringstream oss;
    for (int i = 0; i < 16; ++i) {
        oss << std::setfill('0') << std::setw(2) << std::hex << (int)result[i];
    }

    return oss.str();
}