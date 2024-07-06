````
std::string string_to_md5(const char* text) {
    if (*text == '\0') return "";

    MD5_CTX mdContext;
    MD5_Init(&mdContext);
    const char* ptr = text;
    size_t len = strlen(text);
    for (int i = 0; i < len; ++i) {
        MD5_Update(&mdContext, reinterpret_cast<const unsigned char*>(ptr + i), 1); 
    } 

    unsigned char result[16];
    MD5_Final(&mdContext, result);

    std::string output;
    for (int i = 0; i < 16; ++i) {
        output += sprintf("%02x", result[i]);
    }

    return output;
}