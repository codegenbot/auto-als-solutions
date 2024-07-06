#include <vector>
#include <list>
#include <optional>

std::vector<int> filter_integers(std::list<std::any> values) {
    std::vector<int> result;
    for (const auto& value : values) {
        if (value.type() == typeid(int)) {
            try {
                int num = std::any_cast<int>(value);
                result.push_back(num);
            } catch(const std::bad_any_cast& e) {
                // Handle the case when the value is not an integer
                // For example, print an error message or ignore it
                std::cerr << "Error: " << e.what() << '\n';
            }
        }
    }
    return result;