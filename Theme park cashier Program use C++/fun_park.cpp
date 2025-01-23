#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;

class Khmer_dog_park{
    public:
        int package,i,ans;
        float price,amount;
        int sum=0;
        int bank500,bank100,bank50,bank20,sib,ha,song,one;
        float hight;
        Khmer_dog_park();
        void showMenu(){
            cout << "-----------\n   Menu\n-----------\n[1]package detail\n[2]check hight\n[3]choose package\n[4]pay\n[0]Exit" << endl;
        }
        int setPackage(int a)
        {   
            int pack = a;
            for(int i=1; i<=pack;i++){
                cout << "--------------\nchoose package\n--------------\n[1]Extream package 300 baht\n[2]Family package 250 baht\n[3]Other package 200 baht\n[4]All you can play package 400 baht\n[0]Exit" << endl;
                cout << "\n|member #" << i << "choose : ";
                cin >> ans;
                if(ans==1){
                    sum+=300;
                }
                if(ans==2){
                    sum+=250;
                }
                if(ans==3){
                    sum+=200;
                }
                if(ans==4){
                    sum+=400;
                }
                if(ans==0){
                    break;
                }
                if (ans<0 or ans>4){
                    cout << "!!Pls try again!!" << endl;
                    break;
                }
            }
            return sum;
        }
        //???? package ??? ????
        float getHigh(){
            cout << "------------------------\n#Tell me your hight#\n------------------------" << endl;
            cout << "Enter your hight :";
            cin >> hight;
            while (hight<=0){
                cout << "Please try again : ";
                cin >> hight;
            }
            return hight;
        }//?????????????
        int showPackage(){
            cout << "-------\npackage\n-------\n#Extream package# 300 baht#\n-Roller Coaster\n-Raptor\n-Falcon\n-Viking\n" << endl;
            cout << "#Family package# 250 baht#\n-bouncing castle\n-inflatable house\n-swan boat\n" << endl;
            cout << "#Other package# 200 baht#\n-carousel and giant house\n\n#All you can play package# 400 baht#\n-you can play anything you want in Khmerdogpark\n" << endl;
            
            return 1;
        }//????????????????? package???????
        //????????????????? package???????
};
class Rule:public Khmer_dog_park{
    public:
        void checkRule(float hight){
            if (hight>=131){
                cout << "\nyou can play #Extream-zone# #carousel and giant house#" << endl;
            }else{
                cout << "\nyou can play #Family-zone# #carousel and giant house#" << endl;
            }
        }//??????????????????????????
};
class customer:public Rule{
    public:
       customer();
       int chooseMenu(){
            cout << "choose : ";
            cin >> i;
            if (i==0){
                cout << "Thank you for using the service" << endl;
                i = -1;
            }
            return i;
       }
       void billCustomer(float p ,float a){
           price=p;
           amount=a;
           price = price - amount;
            //?????500
            cout << "change : " <<price << " bath" << endl;
            cout << "Thank you!!!" << endl;
            cout << fixed << setprecision(2) ;
       }
       void writBill(float p ,float a){
            price=p;
            amount=a;
            ofstream f("bill.txt");
            f << fixed << setprecision(2);
            f << "-------Bill-------" << endl;
            f << "|Price : " <<amount << " bath" << endl;
            f << "|Pay : " << price << endl;
            price = price - amount;
            //?????500
            f << "|change : " <<price << " bath" << endl;
            bank500 = price/500;
            if (bank500 >= 1)
            {
                f << "|500 baht bill = " << bank500 << endl;
            }
            price = price-bank500*500;
            //?????100
            bank100 = price/100;
            if (bank100 >= 1)
            {
                f << "|100 bath bill = " << bank100 << endl;
            }
            price = price-bank100*100;
            //?????50
            bank50 = price/50;
            if (bank50 >= 1)
            {
                f << "|50 bath bill = " << bank50 << endl;
            }
            price = price-bank50*50;
            //?????20
            bank20 = price/20;
            if (bank20 >= 1)
            {
                f << "|20 bath bill = " << bank20 << endl;
            }
            price = price-bank20*20;
            //?????? 10
            sib = price/10;
            if (sib >= 1)
            {
                f << "|10 bath coins = " << sib << endl;
            }
            price = price-sib*10;
            //?????? 5
            ha = price/5;
            if (ha >= 1)
            {
                f << "|5 bath coins = " << ha << endl;
            }
            price = price-ha*5;
            //?????? 2
            song = price/2;
            if (song >= 1)
            {
                f << "|2 bath coin = " << song << endl;
            }
            price = price-song*2;
            //?????? 1
            if (price >= 1)
            {
                f << "|1 bath coin = " << price << endl;
            }
            f << "!!!!!Thank you!!!!!" << endl;
            f.close();
       }
       void discount();
       double discount(double amount);
       double discount(double amount,const string &level);
};
Khmer_dog_park::Khmer_dog_park(){
    cout << "\n------------------------\nWelcome to Khmerdogpark\n------------------------" << endl;
    i=0;
}
customer::customer(){
    cout << "\nA group has been created\n" << endl;
}
void customer :: discount(){
    cout << "you don't get the discount" << endl;
}
double customer :: discount(double amount){
    return (amount)-(amount*0.05);
}
double customer :: discount(double amount,const string &level){
    double rate = 0;
           if (level == "Y" or "y"){
               rate = 0.2;
        }
            return (amount)-(amount*rate);
}



int main()
{
    customer player;
    int i=0;
    float amount,pp;
    float hight;
    long int member;
    float price;
    string check,check_card;
    double discount;
    cout << "How many poeple in your group : ";
    cin >> member;
    while (member<=0)
    {
            cout << "Please try again : ";
            cin >> member;
    }
    pp = member;
    while(i>=0)
    {
        player.showMenu();
        i = player.chooseMenu();
        if (i==1){
            player.showPackage();
        }
        if (i==2){
            hight=player.getHigh();
            player.checkRule(hight);
        }
        if (i==3){
            member = pp;
            amount = player.setPackage(member);
            discount= amount;
            cout << fixed << setprecision(2);
            cout << "PRICE : " <<amount << endl;
            cout << "Do you have a membership card? (Y/N) : ";
            cin >> check;
            if(check == "Y" or check == "y"){
             discount = player.discount(amount,"y");
             cout << "Price : " << discount << endl;
            }
            if(check == "N" or check == "n" and member >=5){
             discount = player.discount(amount);
                cout << "we are offering a special discount 5%."<< endl;
                cout << "Price : " << discount << endl;
            }else if(check == "N" or check == "n" and member <=5){
             player.discount();
      }
        }
        if (i==4){
            cout << fixed << setprecision(2);
            cout << "Price : " <<discount << " bath" << endl;
            cout << "Pay : ";
            cin >> price ;
            if (price>=discount){
                player.billCustomer(price,discount);
                player.writBill(price,discount);
                break;
            }else{
                cout << "\n!!!!!!Not enough money to pay!!!!!!\n" << endl;
            }
        }
        if (i==0){
            break;
        }
        if (i<0 or i>4){
            cout << "!!Pls try again!!" << endl;
        }
        
    };
    
    
}