#include <iostream>
#include <string>

struct Any {
    using type = void;

    template<typename T>
    struct retype { using type = T; };

    template<typename T>
    bool operator==(const T& t) const {
        return true;
    }

    template<typename T>
    bool operator<(const T& t) const {
        return false;
    }
};

template<typename A, typename B>
Any compare(const Any&A, const Any&B) {
    if (std::any_cast<int>(A) < std::any_cast<int>(B))
        return A;
    else if (std::any_cast<int>(A) > std::any_cast<int>(B))
        return B;
    else
        return A;

    if (std::any_cast<std::string>(A) > std::any_cast<std::string>(B)) {
        // Do some conversion to double
        double num1 = std::stod(std::any_cast<std::string>(A));
        double num2 = std::stod(std::any_cast<std::string>(B));
        if (num1 < num2)
            return A;
        else if (num1 > num2)
            return B;
    }

    return Any();
}