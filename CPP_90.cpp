vector<int>::iterator it = min_element(lst.begin(), lst.end());
if(it != lst.end() && ++it != lst.end()) {
    return *it;
}
return -1; // or return None if that's what you want