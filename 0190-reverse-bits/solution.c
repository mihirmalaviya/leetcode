int reverseBits(int n) {
    int res=0;
    
    for (uint8_t i=0;i<32;i++){
        // printf("%d", n&1);
        res<<=1;
        res|=n&1;
        n>>=1;
    }
    
    return res;
}
