```cpp
bool iscuber(int a){
    int i = 1;
    while (true) {
        long long value = pow(i, 3);
        if(value == a)
            return true;
        if(value > a)
            return false;
        i++;
    }
}