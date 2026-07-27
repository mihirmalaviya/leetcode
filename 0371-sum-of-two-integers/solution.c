int getSum(int a, int b) {

    unsigned int res=0;
    unsigned int cin=0;
    for (uint8_t i=0;i<32;i++){
        unsigned int ba=a&1;
        unsigned int bb=b&1;
        a>>=1;
        b>>=1;

        unsigned int ans=ba^bb^cin;
        cin=(ba&bb)|((ba^bb)&cin);
        res|=ans<<i;
        }
    return (int)res;
 
}
