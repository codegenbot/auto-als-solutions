bool issame(vector<pair<float, float>> a,vector<pair<float, float>>b){
    if(a.size()!=b.size())return false;
    for(int i=0;i<a.size();i++){
        if(a[i].first!=b[i].first||a[i].second!=b[i].second)return false;
    }
    return true;
}

int main() {
    assert (issame(find_closest_elements({1.1, 2.2, 3.1, 4.1, 5.1}) , {2.2, 3.1}));
}