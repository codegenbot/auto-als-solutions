```cpp
#include <string>
#include <sstream>

string string_to_md5(string text) {
    if (text.empty()) return "None";

    stringstream ss;
    MD5_CTX ctx;
    unsigned char result[16];
    uint32_t len = strlen(text.c_str());
    uint32_t *p = (uint32_t *) &len;

    MD5_Init(&ctx);
    MD5_Update(&ctx, p, 4);
    MD5_Update(&ctx, text.c_str(), text.size());
    MD5_Final(&ctx, result);

    ostringstream oss;
    for (int i = 0; i < 16; ++i) {
        oss << setfill('0') << setw(2) << hex << (int)result[i];
    }

    return oss.str();
}