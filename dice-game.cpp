Here is the solution:

double calculateProbability(int n, int m) {
    double sum = 0;
    for (int i = 1; i <= n; ++i) {
        sum += 1.0 / m;
    }
    return sum - (n > m ? 1.0 : 0);
}
int main() {
    int n, m;
    cin >> n >> m;
    cout << setprecision(5) << fixed << calculateProbability(n, m) << endl;
    return 0;
}