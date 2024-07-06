#include <iostream>
#include <list>
#include <vector>
#include <type_traits>

using namespace std;

bool issame(vector<int> a, vector<int> b) {
    return a == b;
}

template<typename T>
vector<T> filter_integers(list<any> values) {
    vector<T> result;
    for (const auto& value : values) {
        if (holds_alternative<T>(value)) { 
            result.push_back(get<T>(value)); 
        }
    }
    return result;
}

int main() {
    list<any> values = {{3, true}, {'c', false}, {3, true}, {3, true}, {'a', false}, {'b', false}};
    assert(issame(filter_integers(values), vector<int>({3, 3, 3})); 
    return 0;
}