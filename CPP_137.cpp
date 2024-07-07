#include <boost/any.hpp>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int num1, num2;
    cin >> num1 >> num2;
    
    boost::any a = num1;
    boost::any b = num2;
    
    boost::any result = compare_one(a, b);
    
    if (result.type() == typeid(string)) {
        cout << "None" << endl;
    } else {
        int val = boost::any_cast<int>(result);
        cout << val << endl;
    }
    
    return 0;
}