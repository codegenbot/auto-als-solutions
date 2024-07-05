#include <vector>
#include <initializer_list>

bool issame(std::vector<float> a, std::vector<float> b){
    if(a.size() != b.size())
        return false;
    for(int i = 0; i<a.size(); i++)
        if(abs(a[i] - b[i]) > 1e-9)
            return false;
    return true;
}

std::vector<float> get_positive(std::vector<float> l) {
    std::vector<float> result;
    for (float x : l) {
        if (x > 0)
            result.push_back(x);
    }
    return result;

}

int main_entry() {
    assert(issame(get_positive({}), {}));
    return 0;
}