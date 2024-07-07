#include <iostream>
#include <string>
#include <openssl/ssl.h>
#include <openssl/sha.h>

using namespace std;

string string_to_md5(string text) {
    if (text.empty()) return "None";
    
    unsigned char result[16];
    MD5((unsigned char*)text.c_str(), text.size(), result);
    
    string output;
    for(int i = 0; i < 16; i++) {
        char temp[3];
        sprintf(temp, "%02x", result[i]);
        output += temp;
    }
    
    return output;
}