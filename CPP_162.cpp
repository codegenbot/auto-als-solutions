```cpp
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
    for (int i = 0; i < 32; ++i) { 
        char temp[3] = {(char)(result[i >> 2]), (char)((i & 2) ? 0 : ((result[(i >> 2)] >> ((3 - i % 4) * 8)) & 0xFF)), '\0'};
        output += std::string(temp); 
    }

    return output;

}

int main() {
    std::cout << string_to_md5("password") << std::endl;
    return 0;
}