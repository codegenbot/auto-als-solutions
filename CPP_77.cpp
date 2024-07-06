Here is the completed code:

bool iscuber(int a){
    int i = 1;
    while (true) {
        int cube = pow(i,3);
        if(cube == a)
            return true;
        else if(cube > a)
            return false;
        i++;
    }
}