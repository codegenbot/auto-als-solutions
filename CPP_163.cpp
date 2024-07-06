#include <array>

int main_test() {
    std::vector<int> result = generate_integers(17, 89);
    assert(result.size() == 73); // the difference between 89 and 17 is 72
    return 0;
}