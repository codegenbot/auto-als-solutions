#include <vector>
#include <list>

typedef struct {
    bool isPresent;
    int value;
} IntWrapper;

std::vector<int> filter_integers(std::list<int> values) {
    std::vector<int> result;
    for (const auto& value : values) {
        IntWrapper wrapper;
        wrapper.isPresent = true;
        wrapper.value = value;
        result.push_back(wrapper.value);
    }
    return result;
}