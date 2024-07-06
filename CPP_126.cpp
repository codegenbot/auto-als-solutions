vector<int>::iterator it = prev(lst.end());
for (auto i = lst.begin() + 1; i <= it; i++) {
    if (*i < *(i - 1)) return false;
}
return true;