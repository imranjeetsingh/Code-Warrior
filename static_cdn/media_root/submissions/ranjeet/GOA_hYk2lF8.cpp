#include<bits/stdc++.h>
using namespace std;
struct ma
{
    int first,second;
};
int main()
{
    int n;
    cin>>n;
    // map<int,pair <long long, long long> > mp;
    long long a[n];
    ma mp[1000001];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
        mp[i].first=a[i];
        mp[i].second=a[i];
    }
    int q;
    cin>>q;
    while(q--)
    {
        int type;
        cin>>type;
        if(type==2)
        {
            int a;
            cin>>a;
            cout<<abs(mp[a-1].second-mp[a-1].first)<<endl;
            // cout<<mp[a].second<<' '<<mp[a].first<<endl;
        }
        else
        {
            int i, j;
            cin>>i>>j;
            i--;j--;
            // if(mp[i].first>a[j])
            mp[i].first = min(mp[j].first,mp[i].first);
            // else if(mp[i].second<a[j])
            mp[i].second=max(mp[j].second,mp[i].second);
            // if(mp[j].first>a[i])
            mp[j].first = mp[i].first;
            // else if(mp[j].second<a[i])
            mp[j].second = mp[i].second;

        }
        
    }
    return 0;
}