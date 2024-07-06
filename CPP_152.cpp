vector<int> compare(vector<int> game, vector<int> guess) {
    vector<int> result(game.size()); 
    for (int x : game) { 
        if (x == guess[game.size()-1 -guess.size()+x]) 
            result.push_back(0);  
        else 
            result.push_back(abs(x-guess[game.size()-1 -guess.size()+x]));    
    }
    return result;
}