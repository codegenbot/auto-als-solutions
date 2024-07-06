#include <iostream>
#include <string>
#include <openssl/evp.h>
#include <sstream>

std::string string_to_md5(const std::string& text) {
    if (text.empty()) return "None";
    
    unsigned char result[MD5_DIGEST_LENGTH];
    MD5_CTX mdContext;
    MD5_Init(&mdContext);
    const char* ptr = text.c_str();
    while (*ptr) {
        MD5_Update(&mdContext, ptr, 1);
        ptr++;
    }
    MD5_Final(result, &mdContext);
    
    std::stringstream oss;
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
        oss << setfill('0') << setw(2) << hex << (int)result[i];
    }
    
    return oss.str();
}