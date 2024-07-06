#include <cstring>

std::string string_to_md5(const char* text) {
    if (*text == '\0') return "";

    unsigned char result[16];
    MD5_CTX mdContext;
    MD5_Init(&mdContext);
    const char* ptr = text;
    size_t len = strlen(text);