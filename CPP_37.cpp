#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;

vector<float> sort_even(vector<float> l){
    vector<float> result(l.size());
    for(int i=0; i<l.size(); i++){
        if(i%2==0){
            // Sort the even indices
            vector<float> temp;
            for(int j=i;j<l.size() && j<=i+1;j++) {
                temp.push_back(l[j]);
            }
            sort(temp.begin(),temp.end());
            int k=0;
            for(int j=i;j<l.size() && j<=i+1;j++) {
                l[j]=temp[k++];
            }
        } else {
            // Copy the odd indices
            result[i] = l[i];
        }
    }
    return result;
}