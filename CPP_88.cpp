int main() {
    std::vector<int> array1 = {21, 14, 23, 11};
    std::vector<int> array2 = {23, 21, 14, 11};
    assert(issame({21, 14, 23, 11}, sort_array({21, 14, 23, 11})));
    sort_array(array1);
}