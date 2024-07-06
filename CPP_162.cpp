```cpp
#include <string>
#include <iomanip>
#include <sstream>

using namespace std;

string string_to_md5(const string& text) {
    if (text.empty()) return "";

    unsigned char result[16];
    MD5_CTX mdContext;
    MD5_Init(&mdContext);
    const char* ptr = text.c_str();
    size_t len = text.length();
    MD5_Update(&mdContext, ptr, len);
    MD5_Final(result, &mdContext);

    ostringstream oss;
    for (int i = 0; i < 16; ++i) {
        oss << setfill('0') << setw(2) << hex << (int)result[i];
    }

    return oss.str();
}