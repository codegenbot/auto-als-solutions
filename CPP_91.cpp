```cpp
int count = 0;
size_t start = 0;
while ((start = S.find("I", start)) != string::npos) {
    size_t end = S.find_first_of(".!? ", start);
    if (end == string::npos || end == S.size() - 1)
        break;
    ++count;
    start = end + 1;
}
return count;