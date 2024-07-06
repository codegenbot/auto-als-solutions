#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;

vector<int> compare(vector<int> game, vector<int> guess) {
    vector<int> result(game.size()); // initialize with same size as game
    for (int x : game) { 
        if (x == guess[game.size()-1 -guess.size()+x]) 
            result.push_back(0);  
        else 
            result.push_back(abs(x-guess[game.size()-1 -guess.size()+x]));    
    }
    return result;
}