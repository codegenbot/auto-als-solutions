string exchange(vector<int> lst1, vector<int> lst2) {
    int even_count = 0;
    for (int num : lst1) {
        if (num % 2 == 0) {
            even_count++;
        } else {
            bool found_even = false;
            for (int num2 : lst2) {
                if (num2 % 2 == 0) {
                    swap(lst1[std::distance(lst1.begin(), find(lst1.begin(), lst1.end(), num))],
                         lst2[std::distance(lst2.begin(), find(lst2.begin(), lst2.end(), num2))]);
                    found_even = true;
                    break;
                }
            }
            if (!found_even) {
                return "NO";
            }
        }
    }
    return even_count == lst1.size() ? "YES" : "NO";
}