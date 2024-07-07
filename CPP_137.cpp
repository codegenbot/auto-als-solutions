#include <boost/any.hpp>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int num1, num2;
    cin >> num1 >> num2;

    boost::any a = boost::any(num1);
    boost::any b = boost::any(num2);

    boost::any result = compare_one(a, b);

    if (boost::any_cast<string>(result) == "None") {
        cout << "Error: Input types are incompatible for comparison." << endl;
    } else {
        cout << "The result is: " << boost::any_cast<int>(result) << endl;
    }

    return 0;
}