/*
Date:27/04/2021
1622. Fancy Sequence - Leetcode Hard

The following problem is solved using maths logic..+ modular inverse multiplication.

The concept used are:
1)modular arithetic assumes normal rules of arithmetic under modular operation,so operations are lossless..
2)Whenver (N/D)%mod is to performed,then always do N*mulinv(D)%mod,so that ans is lossless ,as many information are lost using N/D and ans is in float whereas %operation under N/D should always give interger.

3)We use the offset technique.While inserting we modify the input by first subtracting by addition upto that point and then result val is divided by product to be multiplied,This modified value is stored in Seq list.

One important point is that cpp does -ve modular result to +ve.You have to manually do it.

Hint:https://www.youtube.com/watch?v=Z0ymtF4dExU .. by erricto go to 39 mins

*/
class Fancy {
public:
    long long add=0;
    long long prod=1;
    long long mod=1000000007;
    vector<long long> seq;
    Fancy() {
        
    }
    
    long long powmod(long long a, long long b, long long m) {
        a %= m;
        long long res = 1;
        while (b > 0) {
            if (b & 1)
                res = res * a % m;
            a = a * a % m;
            b >>= 1;
        }
        return res;
    }
    
    
    void append(long long val) {
        //cout<<"add:"<<add<<", prod:"<<prod<<" , val:"<<val<<endl;
        val=val-add;
        long long mulinv=powmod(prod,mod-2,mod);
        //cout<<"mulinv:"<<mulinv<<endl;
        //cout<<"val:"<<val<<endl;
        //cout<<((long long)407142860 *(long long)((-205)%mod)%(long long)1000000007<<endl;
        val=val%mod;
        if(val<0) val+=mod;
        //cout<<"val:"<<val<<endl;
        long long ans=(val*mulinv)%mod;
        //cout<<"ans:"<<ans<<endl;
        seq.push_back(ans);
    }
    
    void addAll(long long  inc) {
        add=(add+inc)%mod;  
        //add%=mod;
    }
    
    void multAll(long long m) {
        add=(add*m)%mod;
        //add%=mod;
        //prod*=m;
        prod=(prod*m)%mod;
        //prod%=mod;
    }
    
    
    void printval(vector<long long>& vec){
        for(int a:vec){
            cout<<a<<" ";
        }
        cout<<endl;
    }
    
    int getIndex(int idx) {
        //cout<<"10*4:"<<powmod(10,4,mod)<<endl;
        //printval(seq);
        
        if(idx>=seq.size()) return -1;
        long long val=seq[idx];
        val*=prod;
        //val%=mod;
        val+=add;
        return val%mod;
    }
};

/**
 * Your Fancy object will be instantiated and called as such:
 * Fancy* obj = new Fancy();
 * obj->append(val);
 * obj->addAll(inc);
 * obj->multAll(m);
 * int param_4 = obj->getIndex(idx);
 */


/*

add:0 , prod:1 , val:3
val:3
mulinv:1
ans:3
add:0 , prod:1 , val:7
val:7
mulinv:1
ans:7
add:6 , prod:4 , val:7
val:1
mulinv:250000002
ans:250000002
add:6 , prod:4 , val:3
val:-3
mulinv:250000002
ans:250000001
[3, 7, 250000002, 250000001]
[3, 7, 250000002, 250000001]
[3, 7, 250000002, 250000001]
add:215 , prod:140 , val:8
val:-207
mulinv:407142860
ans:721428575
add:215 , prod:140 , val:10
val:-205
mulinv:407142860
ans:535714288
[3, 7, 250000002, 250000001, 721428575, 535714288]
[3, 7, 250000002, 250000001, 721428575, 535714288]


*/