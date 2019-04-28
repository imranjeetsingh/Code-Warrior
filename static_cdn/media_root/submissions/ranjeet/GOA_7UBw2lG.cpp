#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int>v;
    for(int i=0;i<5;i++)
        v.push_back(i);
    vector<int>ans(v.begin()+0,v.begin()+2);
    for(int i=0;i<ans.size();i++)
        cout<<ans[i]<<' ';
    return 0;
}