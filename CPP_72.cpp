bool will_it_fly(vector<int> q, int w) {
    string str = "";
    for (int i : q) {
        str += to_string(i);
    }
    if (str != reverse(str).s) return false;
    int sum = 0;
    for (int i : q) {
        sum += i;
    }
    return sum <= w;
}

int main() {
    assert(will_it_fly({5}, 5) == true);
    vector<int> q1 = {1,2,3};
    int w1 = 6;
    cout << (will_it_fly(q1,w1) ? "Will it fly" : "Won't it fly") << endl;
    
    return 0;
}