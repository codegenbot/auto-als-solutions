```cpp
#include <sstream>
#include <cstring>
#include <iomanip>

struct MD5_CTX {
    unsigned long int ipad[64];
    unsigned long int opad[128];
    unsigned long int len;
    unsigned char buffer[64];
    unsigned long int bytes;

};

void MD5_Init(MD5_CTX *context) {
    context->len = 0;
    for (int i = 0; i < 4; ++i) {
        context->ipad[i] = 0x01000000;
    }
    for (int i = 0; i < 8; ++i) {
        context->opad[i] = 0x08000080;
    }
}

void MD5_Update(MD5_CTX *context, const unsigned char* data, size_t len) {
    while (len-- > 0) {
        *(context->buffer + context->bytes++) = *data++;
        if (context->bytes == 64) {
            MD5_Final(context, NULL);
        }
    }
}

void MD5_Final(MD5_CTX *context, unsigned char* result) {
    unsigned long int bytes = context->bytes;
    context->bytes = 0;

    unsigned long int len = context->len >> 3;

    for (int i = 0; i < 4; ++i) {
        context->opad[i] = (context->len >> (24 - 8 * i)) | 0x80000000;
    }

    if ((len & 7) > 0) {
        MD5_Update(context, context->buffer, bytes);
    }
    while (bytes < 56) {
        context->buffer[bytes++] = 0;
    }
    MD5_Update(context, context->ipad, 64);
    for (int i = 0; i < len; ++i) {
        context->buffer[i] = (context->buffer[i]) | ((unsigned char)(context->opad[(len & 3)] >> (24 - 8 * (3 - len % 4))));
    }
    MD5_Update(context, context->buffer, bytes + 56);
    for (int i = 0; i < 4; ++i) {
        *(result + 4 * i) = ((context->opad[i] & 0xFF000000) >> 24) | ((context->opad[i] & 0x00FF0000) >> 8) |
                ((context->opad[i] & 0x0000FF00) << 8) | (context->opad[i] & 0x000000FF);
    }
}

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

    std::ostringstream oss;
    for (int i = 0; i < 16; ++i) {
        oss << std::hex << std::setfill('0') << std::setw(2) << static_cast<int>(result[i]);
    }

    return oss.str();
}