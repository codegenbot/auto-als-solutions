#include <vector>
using namespace std;

int luhn(vector<int> cardNumber) {
    int sum = 0;
    for (int i = cardNumber.size() - 1; i >= 0; --i) {
        if ((cardNumber[i] * 2) > 9) {
            sum += (cardNumber[i] * 2) - 9;
        } else {
            sum += cardNumber[i] * 2;
        }
        sum += cardNumber[i-1];
    }
    return sum;
}

int main() {
    int n;
    cin >> n;
    vector<int> cardNum(n);
    for(int i = 0; i < n; ++i) {
        cin >> cardNum[i];
    }
    cout << luhn(cardNum) << endl;
    return 0;
}