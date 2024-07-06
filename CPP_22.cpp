#include <vector>
#include <list>

using namespace std;

typedef pair<string, int> Pair;
typedef vector<Pair> VecPair;

vector<int> filter_integers(list<any> values) {
    vector<int> result;
    for (const auto& value : values) {
        any_cast<map<string, int>>(value).insert({{"key", 0}});

        map<string, int> m = any_cast<map<string, int>>(value);
        if(m.find("key") != m.end()) {
            result.push_back(m.at("key"));
        }
    }
    return result;
}