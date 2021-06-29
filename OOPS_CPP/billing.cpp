#include <iostream>
#include <map>
using namespace std;

class Billing{
    
    protected:
        map<string,int> product_rate;
        map<string,int> product_unit;
    public:
        
        bool defined;
    
        long long int mobile_no;
        string customer_name;
        map<string,pair<int,int>> cart;
        Billing(long long mobile_no,string customer_name){
            this->mobile_no = mobile_no;
            this->customer_name=customer_name;
            if (true){
                product_rate["shampoo"]=12;product_unit["shampoo"]=1;
                product_rate["oil"]=10;product_unit["oil"]=100;
                product_rate["rice"]=30;product_unit["rice"]=500;
                defined=true;
                //cout<<"product_rate size:"<<product_rate.size()<<endl;
            }
        
        }
        
        void addItem(string product,int quantity){
            //cout<<"product:"<<product<<",quantity:"<<quantity<<endl;
            if(product_rate.find(product)!=product_rate.end()){
                cart[product]={product_rate[product],quantity};
                cout<<"size of cart:"<<cart.size()<<endl;
            }
            else{
                cout<<"no such product here"<<endl;
            }
        }
        
        void getbill(){
            double amount;
            //cout<<"product name | quantity | rate | cost "<<endl;
            cout<<endl<<endl<<"Customer Name:"<<customer_name<<endl;
            cout<<"Mobile:"<<mobile_no<<endl;
            cout<<"cart size:"<<cart.size()<<endl;
            for(auto a:cart){
                string prod=a.first;
                int rate=a.second.first;
                //cout<<"units:"<<product_unit[prod]<<endl;
                double quantity=(double)a.second.second/product_unit[prod];
                amount+=rate*quantity;
                cout<<"name:"<<prod<<"  "<<"quantity:"<<a.second.second<<" "<<"rate:"<<rate<<" "<<"cost:"<<rate*quantity<<endl;
                
            }
            cout<<"total amount:"<<amount<<endl;
            
        }
        
        ~Billing(){
            cout<<"deleting the billing"<<endl;    
        
        }
        
        
        
    
};




int main(){
    
    
    while(true){
        cout<<"enter customer's name:";
        string customer_name;
        cin>>customer_name;
        cout<<"enter mobile number:";
        long long int mobile_no;
        cin>>mobile_no;
        Billing *B= new Billing(mobile_no,customer_name);
        bool flag=true;
        while(flag){
            string product;int quantity;
            cout<<"enter product name:";
            cin>>product;
            cout<<"enter quantity:";
            cin>>quantity;
            B->addItem(product,quantity);
            cout<<"Press 1 to add or 2 to bill"<<endl;
            int press;
            cin>>press;
            if(press==1) continue;
            else flag=false;
        }
        B->getbill();
        cout<<endl;
        delete B;
        
        
    }
    
    return 0;
}



























///part 2
#include <iostream>
#include <map>
using namespace std;

class Billing{
    
    protected:
        map<string,int> product_rate;
        map<string,int> product_unit;
    public:
        
        bool defined;
    
        long long int mobile_no;
        string customer_name;
        map<string,pair<int,int>> cart;
        Billing(long long mobile_no,string customer_name){
            this->mobile_no = mobile_no;
            this->customer_name=customer_name;
            if (true){
                product_rate["shampoo"]=12;product_unit["shampoo"]=1;
                product_rate["oil"]=10;product_unit["oil"]=100;
                product_rate["rice"]=30;product_unit["rice"]=500;
                defined=true;
                //cout<<"product_rate size:"<<product_rate.size()<<endl;
            }
        
        }
        
        void addItem(string product,int quantity){
            //cout<<"product:"<<product<<",quantity:"<<quantity<<endl;
            if(product_rate.find(product)!=product_rate.end()){
                cart[product]={product_rate[product],quantity};
                cout<<"size of cart:"<<cart.size()<<endl;
            }
            else{
                cout<<"no such product here"<<endl;
            }
        }
        
        void getbill(){
            double amount;
            //cout<<"product name | quantity | rate | cost "<<endl;
            cout<<endl<<endl<<"Customer Name:"<<customer_name<<endl;
            cout<<"Mobile:"<<mobile_no<<endl;
            cout<<"cart size:"<<cart.size()<<endl;
            for(map<string,pair<int,int>>::iterator a=cart.begin();a!=cart.end();a++){
                string prod=a->first;
                int rate=a->second.first;
                //cout<<"units:"<<product_unit[prod]<<endl;
                double quantity=(double)a->second.second/product_unit[prod];
                amount+=rate*quantity;
                cout<<"name:"<<prod<<"  "<<"quantity:"<<a->second.second<<" "<<"rate:"<<rate<<" "<<"cost:"<<rate*quantity<<endl;
                
            }
            cout<<"total amount:"<<amount<<endl;
            
        }
        
        ~Billing(){
            cout<<"deleting the billing"<<endl;    
        
        }
        
        
        
    
};




int main(){
    
    
    while(true){
        cout<<"enter customer's name:";
        string customer_name;
        cin>>customer_name;
        cout<<"enter mobile number:";
        long long int mobile_no;
        cin>>mobile_no;
        Billing *B= new Billing(mobile_no,customer_name);
        bool flag=true;
        while(flag){
            string product;int quantity;
            cout<<"enter product name:";
            cin>>product;
            cout<<"enter quantity:";
            cin>>quantity;
            B->addItem(product,quantity);
            cout<<"Press 1 to add or 2 to bill"<<endl;
            int press;
            cin>>press;
            if(press==1) continue;
            else flag=false;
        }
        B->getbill();
        cout<<endl;
        delete B;
        
        
    }
    
    return 0;
}

