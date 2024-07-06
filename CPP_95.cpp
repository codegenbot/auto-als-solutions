Here is the completed code:

```cpp
bool check_dict_case(map<string, string> dict) {
    bool allUpper = true;
    bool allLower = true;

    for (auto &pair : dict) {
        if (!pair.first.empty() && !isupper(pair.first[0])) {
            allUpper = false;
            break;
        }
        if (!pair.first.empty() && !islower(pair.first[0])) {
            allLower = false;
            break;
        }
    }

    return (allUpper || allLower);
}