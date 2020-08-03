#include<bits/stdc++.h>
using namespace  std;

class something
{
	private: 
	int n,s=0;
public:
	void nhap(){
		cin>>n;
	}
	void dao(){
		while(n){
			int t=n%10;
			s=s*10+t;
			n=n/10;
		}
	}
	void xuat(){
		cout<<s;
	}
};
int main()
{
	something sa;
	sa.nhap();
	sa.dao();
	sa.xuat();
}