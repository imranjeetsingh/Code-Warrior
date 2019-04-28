#include<bits/stdc++.h>
using namespace std;


struct node{
    int a,b,c;
};

bool comp1(const node &G,const node &H){
    if(G.a>H.a){
        return true;
    }
    return false;
}
bool comp2(const node &G,const node &H){
    if(G.b>H.b){
        return true;
    }
    return false;
}
bool comp3(const node &G,const node &H){
    if(G.c>H.c){
        return true;
    }
    return false;
}


int main(){
    int n;
    cin>>n;
    node A[n], B[n], C[n];
    int x,y,z;
    cin>>x>>y>>z;
    map<node, int> mp;
    for(int i=0;i<n;i++){
        int jj,kk,ll;
        cin>>jj>>kk>>ll;
        A[i].a=jj;
        A[i].b=kk;
        A[i].c=ll;
        B[i].a=jj;
        B[i].b=kk;
        B[i].c=ll;
        C[i].a=jj;
        C[i].b=kk;
        C[i].c=ll;
        mp[A[i]]++;
    }
    sort(A,A+n,comp1);
    sort(B,B+n,comp2);
    sort(C,C+n,comp3);
    int i=0,j=0,k=0;
    int ans=0;
    for(int p=0;p<n;p++){
        int a1=INT_MIN, a2=INT_MIN, a3=INT_MIN;
        while(mp[A[i]]==0){
            i++;
        }
        while(mp[B[j]]==0){
            j++;
        }
        while(mp[C[k]]==0){
            k++;
        }
        
        
        
        if(x>0){
            a1=A[i].a;
        }
        if(y>0){
            a2=A[j].b;
        }
        if(z>0){
            a3=A[k].c;
        }
        int q=max(a1,max(a2,a3));
        ans+=q;
        if(a1!=INT_MIN && A[i].a==q){
            mp[A[i]]--;
            
            i++;
            x--;
        
        }
        if(a2!=INT_MIN && B[j].b==q){
            mp[B[j]]--;
            j++;
            y--;
            
        }
        if(a3!=INT_MIN && C[k].c==q){
            mp[C[k]]--;
            k++;
            z--;
        
        }
    }
    cout<<ans<<endl;
    
    
    
    
    return 0;
}