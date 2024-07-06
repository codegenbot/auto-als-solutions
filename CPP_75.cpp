bool is_multiply_prime(int a){
    for(long long int i=2;i*i<=a;++i){
        if(a%i==0){
            bool is_prime=true;
            for(long long int j=2;j*j<=i;++j){
                if(i%j==0)is_prime=false;break;
            }
            for(long long int k=a/i; k*k<=a;++k){
                if(k*i!=a)break;
                bool is_k_prime=true;
                for(int l=2;l*l<=k;++l){
                    if(k % l == 0)is_k_prime = false;break;
                }
                if(is_k_prime){
                    for(long long int m=a/(k*i);m*m<=a/i;++m){
                        if(m*i!=a/i)break;
                        bool is_m_prime=true;
                        for(int n=2;n*n<=m;++n){
                            if(m % n == 0)is_m_prime = false;break;
                        }
                        if(is_m_prime)return true;
                    }
                }
            }
        }
    }
    return false;
}