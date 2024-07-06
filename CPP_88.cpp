int main() {
    std::vector<int> array1 = {21, 14, 23, 11};
    std::vector<int> array2 = {23, 21, 14, 11};
    assert (issame(array1, array2));
    sort_array(array1);
}