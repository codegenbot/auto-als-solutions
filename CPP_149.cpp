Here is the solution:

vector<string> sorted_list_sum(vector<string> lst) {
    // Remove strings with odd lengths from the vector
    lst.erase(std::remove_if(lst.begin(), lst.end(),
        [](const string& s) { return s.length() % 2 != 0; }),
        lst.end());

    // Sort the vector by length and then alphabetically
    std::stable_partition(lst.begin(), lst.end(),
        [this](const string& s) {
            if (s.length() % 2 == 0)
                return true;
            else
                return false;
        });
    std::sort(lst.begin(), lst.end());

    return lst;
}