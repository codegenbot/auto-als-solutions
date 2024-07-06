```cpp
#include <iostream>
#include <vector>

bool issame(std::vector<int> a, std::vector<int> b) {
    if(a.size() != b.size())
        return false;
    for(int i=0; i<a.size(); i++)
        if(a[i] != b[i])
            return false;
    return true;
}

std::vector<int> compare(std::vector<int> game, std::vector<int> guess) {
    std::vector<int> result;
    for (int i = 0; i < game.size(); i++) {
        if (game[i] == guess[i]) {
            result.push_back(0);
        } else {
            result.push_back(abs(guess[i] - game[i]));
        }
    }
    return result;
}

int main() {
    std::vector<int> game, guess;
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;

    for(int i=0; i<n; i++) {
        std::cout << "Enter element " << (i+1) << ": ";
        std::cin >> game[i];
    }

    for(int i=0; i<n; i++) {
        std::cout << "Guess the number: ";
        std::cin >> guess[i];
    }

    if(issame(game, guess)) {
        std::cout << "Congratulations! You guessed correctly." << std::endl;
    } else {
        std::vector<int> result = compare(game, guess);
        for(int i=0; i<n; i++)
            std::cout << "Number " << (i+1) << ": ";
        if(result[0] == 0)
            std::cout << "Black\n";
        else {
            int j;
            for(j=n-2; j>=0 && result[j]>0; j--)
                if(abs(guess[j]-game[j])==result[j])
                    break;
            if(j<0) {
                for(int i=0; i<n; i++)
                    std::cout << "Number " << (i+1) << ": ";
                for(int i=n-2; i>=0 && result[i]>0; i--)
                    std::cout << "Black" << ((i==n-2)?"\n":"\n White");
            } else {
                int k;
                for(k=0; k<n && (result[k] == 0 || guess[k]==game[k]); k++);
                if(k==j)
                    std::cout << "White\n";
                else {
                    std::cout << "Number " << (k+1) << ": White, Number ";
                    std::cout << (k+2) << ": Black" << ((k+2<n)?"\n":"\n");
                }
            }
        }
    }

    return 0;
}