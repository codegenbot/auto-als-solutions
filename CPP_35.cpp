float max_element(vector<float> l){
    float m = l[0];
    for(float i : l) {
        if(i > m)
            m = i;
    }
    return m;
}