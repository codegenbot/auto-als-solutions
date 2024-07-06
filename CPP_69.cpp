int search(vector<int> lst) {
    int maxFreq = 0;
    for (int num : lst) {
        if (num > 0 && freq(num) >= num) {
            return num;
        }
        maxFreq = max(maxFreq, freq(num));
    }
    return -1;

}

int freq(int x) {
    int count = 0;
    for (int i : lst) {
        if (i == x) {
            count++;
        }
    }
    return count;
}