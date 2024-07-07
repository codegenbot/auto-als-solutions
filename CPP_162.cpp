```cpp
#include <string>
#include <openssl/md5.h>
#include <sstream>
#include <iomanip>

using namespace std;

string string_to_md5(string text) {
    if (text.empty()) return "";
    
    unsigned char md5[MD5_DIGEST_LENGTH];
    MD5((const unsigned char*)text.c_str(), text.size(), md5);
    
    stringstream ss;
    ss << hex;  // specify the base
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
        ss << setfill('0') << setw(2) << (int)md5[i];
    }
    
    return ss.str();
}