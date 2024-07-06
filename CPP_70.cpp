int main() {
    int v[] = {1, 1, 1, 1, 1};
    std::vector<int> input(v, v + 1);
    assert(issame(strange_sort_list(input) , input));
    return 0;
}