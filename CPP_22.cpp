#include <any>
#include <vector>
#include <list>

std::vector<int> filter_integers(std::list<std::any> values) {
    std::vector<int> result;
    for (auto& value : values) {
        if (value.type() == typeid(bool)) {
            bool val = boost::get<bool>(value);
            if (val) {
                try {
                    int num = boost::get<int>(value);
                    result.push_back(num);
                } catch (...) {}
            }
        }
    }
    return result;
}