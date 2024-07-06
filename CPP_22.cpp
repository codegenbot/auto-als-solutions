```
#include <vector>
#include <list>

class Optional {
public:
    bool has_value;
    int value;

    Optional(int val = 0) : has_value(true), value(val) {}
    Optional() : has_value(false) {}

    template<typename T>
    T get() {
        if (!has_value)
            throw std::runtime_error("Optional does not have a value");
        return value;
    }
};

std::vector<int> filter_integers(std::list<Optional> values) {
    std::vector<int> result;
    for (const auto& value : values) {
        if (value.has_value) {
            result.push_back(value.get());
        }
    }
    return result;
}