```cpp
#include <openssl/md5.h>
#include <string>

using namespace std;

string string_to_md5(string text) {
    if (text.empty()) return "";

    unsigned char buffer[MD5_DIGEST_LENGTH];
    MD5((const unsigned char *)text.c_str(), text.size(), buffer);

    ostringstream oss;
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
        oss << setfill('0') << setw(2) << hex << (int)buffer[i];
    }

    return oss.str();
}