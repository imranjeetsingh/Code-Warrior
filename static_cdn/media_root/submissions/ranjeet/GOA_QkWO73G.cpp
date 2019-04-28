#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int m,n;
        cin>>m>>n;
        int p,k;
        cin>>p>>k;
        int x=m/p;
        x=p*x;
        if(m%p){
            x++;
        }
        int a=x;
        int ans=0;
        // cout<<x<<endl;
        while(a<=n){
            int y1=n/a;
            int y2=m/a;
            if(m%a){
                y2++;
            }
            ans+=y1-y2+1;
            a*=x;
        }
        cout<<ans*k<<endl;

    

    }



    return 0;
}