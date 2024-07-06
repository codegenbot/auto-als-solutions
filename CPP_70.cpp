int main() {
    int v[] = {1, 1, 1, 1, 1};
    std::vector<int> original(v, v + 5);
    assert(issame(strange_sort_list(original) , original));
    return 0;
}