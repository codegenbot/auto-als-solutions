```
int count = 0;
size_t pos = 0;
while ((pos = S.find(".", pos)) != string::npos || (pos = S.find("?", pos)) != string::npos || (pos = S.find("!", pos)) != string::npos) {
    size_t start = pos == string::npos ? pos : 1;
    if (S.substr(start, 2) == " I") {
        count++;
    }
    pos = ++start;
}
return count;