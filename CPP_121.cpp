#include <vector>
using namespace std;

int main() {
    vector<int> lst;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        lst.push_back(x);
    }
    int result = solution(lst);
    cout << result << endl;
    return 0;
}

int solution(vector<int> lst) {
    int sum = 0;
    for (int i = 0; i < lst.size(); i++) {
        if ((i % 2 == 0 && lst[i] % 2 != 0)) {
            sum += lst[i];
        }
    }
    return sum;
}