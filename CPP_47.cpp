```cpp
int main() {
    float numbers[] = {8, 1, 3, 9, 9, 2, 7};
    int n = sizeof(numbers) / sizeof(*numbers);
    assert (std::abs(median(std::vector<float>(numbers, numbers+n)) - 7)<1e-4 );
    return 0;
}