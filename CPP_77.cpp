#include <cmath>
using namespace std;

bool iscuber(int a){
    int x = round(cbrt(a));
    return (x*x*x == a);
}

int main() {
    assert(iscuber(1729) == false);
    
}