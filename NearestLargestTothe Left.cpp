#include <bits/stdc++.h>
using namespace std;


vector<int> NLL(vector<int>a){
    int n=a.size();
    vector<int>v;

    stack<int>s;

    for(int i=0;i<n;i++){
        if(s.size()==0){
            v.push_back(-1);

        }
        else if (s.size()>0 && s.top()>a[i]){
            v.push_back(s.top());

        }else if(s.size()>0 && s.top()<=a[i]){
            while(s.size()>0 && s.top()<=a[i]){
                s.pop();
            }
            if(s.size()==0){
                v.push_back(-1);

            }else{
                v.push_back(s.top());

            }
        }
        s.push(a[i]);
    }
    // reverse(v.begin(),v.end());
    return v;
} 
int main() 
{
    // cout << "Hello, World!";
    vector<int>an={3,2,4,8};
    vector<int>ans=NLL(an);
    for(auto x:ans){
        cout<<x<<" ";
    }
    return 0;
}
