#include <iostream>
#include <vector>

using namespace std;

vector<int> compare(vector<int> game, vector<int> guess) {
    vector<int> result;
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == guess[i]) {
            result.push_back(0);
        } else {
            result.push_back(abs(guess[i] - game[i]));
        }
    }
    return result;
}

vector<int> issame(vector<int> game, vector<int> guess) {
    vector<int> res;
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == guess[i])
            res.push_back(1);
        else
            res.push_back(2);
    }
    return res;
}

int main() {
    int n, m;
    cin >> n >> m;
    
    vector<int> g, gu;
    for(int i=0; i<n; i++){
        int x;
        cin>>x;
        g.push_back(x);
    }
    
    for(int i=0; i<m; i++){
        int y;
        cin>>y;
        gu.push_back(y);
    }
    
    vector<int> ans = compare(g,gu);
    
    // Write your code here.
    if (ans == issame(g, gu)) {
        cout << "Yes";
    } else {
        cout << "No";
    }
    
    return 0;
}