#include<iostream>
using namespace std;

class E;
class F{
    public:
        void getval(E& e);
        
};

class E{
    private:
         int eval=12323;
         void findval();
             
     
    public:
        int val=0;
        E(int val){
            this->val=val;
            cout<<"calling E"<<endl;
        }
        friend void F::getval(E& e);
    
};


void F::getval(E& e){
            cout<<e.eval<<endl;
            e.findval();
            
}

void E::findval(){
             cout<<"finval..!!!"<<endl;
}

int main(){
    
    F f=F();
    E e=E(8765);
    f.getval(e);
    
    
    return 0;
}