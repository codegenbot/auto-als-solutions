Here is the completed code:

```cpp
#include <string>
#include <sstream>

using namespace std;

string string_sequence(int n) {
    ostringstream oss;
    for (int i = 0; i <= n; i++) {
        oss << i << " ";
    }
    return oss.str();
}