#include<iostream>
using namespace std;

int Sum(int n){
    if (n == 0){
        return 0;
    }
    
    int PrevSum = Sum(n-1);
    return n + PrevSum;
}


int main(){
    int n;
    cin>>n;

    cout<<Sum(n)<<endl;
    return 0;
}