#include<iostream>
using namespace std;

class E{
    public:
        int val=0;
        E(int val){
            this->val=val;
            cout<<"calling E"<<endl;
        }
};

class D:public E{
    public:
        int val=0;
        D(int val):E(val*3){
            this->val=2*val;
            cout<<"initialized:"<<this->val<<endl;
        }
};



class A:public D{
    public:
        int val=0;
        A(int val):D(val){
            this->val=val;
            cout<<"initialized A:"<<this->val<<endl;
        }
};

class C{
    public:
        int val=0;
        C(int val){
            this->val=val;
            cout<<"initialized C:"<<this->val<<endl;
        }
};



class B:public A,public C{
    public:
        int val=0;
        B(int val1,int val2):A(val1),C(val1*val2){
            this->val=val2;
            //A=val1;
            cout<<"derived class"<<this->val<<endl;
        }
        void getAval(){
            cout<<A::val<<endl;
        }
        void getBval(){
            cout<<val<<endl;
        }
};

int main(){
    B b=B(12,13);
    b.getAval();
    b.getBval();
    cout<<b.A::val<<endl;
    cout<<b.A::D::val<<endl;
    cout<<b.A::D::E::val<<endl;
    return 0;
}