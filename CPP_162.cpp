```c++
#include <string>
#include <openssl/md5.h>

using namespace std;

string string_to_md5(string text) {
    if (text.empty()) return "";

    unsigned char md5[16];
    MD5_CTX ctx;
    MD5_Init(&ctx);
    MD5_Update(&ctx, text.c_str(), text.size());
    MD5_Final(md5, &ctx);

    string result;
    for (int i = 0; i < 16; ++i) {
        char buff[3];
        sprintf(buff, "%02x", md5[i]);
        result += string(buff);
    }

    return result;
}

int main() {
    string text;
    cout << "Enter a string: ";
    getline(cin, text);
    cout << "MD5 of the input is: " << string_to_md5(text) << endl;
    return 0;
}