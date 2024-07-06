int sum_squares(vector<int> lst){
    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        if(i % 3 == 0 && i % 4 != 0) // index is multiple of 3, not 4
            sum += lst[i] * lst[i];
        else if(i % 4 == 0 && i % 3 != 0) // index is multiple of 4, not 3
            sum += pow(lst[i], 3);
    }
    return sum;
}