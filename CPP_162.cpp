```cpp
std::string string_to_md5(const char* text) {
    if (*text == '\0') return "";

    unsigned char result[16];
    MD5_CTX mdContext;
    MD5_init(&mdContext);
    const char* ptr = text;
    size_t len = strlen(text);
    MD5_update(&mdContext, (const unsigned char*)ptr, len); 
    MD5_final(&mdContext, result);

    std::ostringstream oss;
    for (int i = 0; i < 16; ++i) {
        oss << std::setfill('0') << std::setw(2) << std::hex << (int)result[i];
    }

    return oss.str();
}