#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    map<int,char>mp;
    int count=1;
    for(int i=97;i<=122;i++)
    {
        mp[count]=char(i);
        count++;
    }
    // for(int =1;i<27;i++)
    // {
    //     cout<<mp[i]<<' ';
    // }
    // cout<<endl;
    while(t--)
    {
        int n;
        cin>>n;
        int a[n];
        for(int i=0;i<n;i++)
            cin>>a[i];
        string ans="";
        int flag=0;
        for(int i=0;i<n;i++)
        {
            if(i==0 && a[i]==1)
            {
                ans+="a";
            }
            else if(i==0 && a[i]>1)
            {
                flag=1;
                break;
            }
            else if(a[i]<=i+1 && a[i]>a[i-1] && a[i]<27)
            {
                ans+=mp[a[i]];
            }
            else if(a[i]<=i+1 && a[i]==a[i-1] && a[i]<27)
            {
                ans+="a";
            }
            else
            {
                flag=1;
                break;
            }
        }
        if(flag)
            cout<<"-1"<<endl;
        else
            cout<<ans<<endl;
    }
    return 0;
}