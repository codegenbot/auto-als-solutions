#include<stdio.h>
#include<vector>
using namespace std;

bool move_one_ball(vector<int> arr){
    int n = arr.size();
    if(n == 0) return true; // If array is empty, it's possible to get sorted.
    
    for(int i = 1; i < n; i++){
        if(arr[i] <= arr[0]){
            break;
        }
    }
    else{
        return false;
    }
    return true;
}