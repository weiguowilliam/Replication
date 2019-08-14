#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<cctype>
#include<queue>
#include<climits>
#include<bitset>
#include<set>
#include<map>
using namespace std;
#define pii pair<int,int>
#define pip pair<int,pii>

bitset<100000> vis;

int main(){
   int T; scanf("%d",&T);
   for(int cs=0; cs<T; cs++){
      int n; scanf("%d",&n);
	  int cap; scanf("%d",&cap);
	  priority_queue<int,vector<int>,greater<int> > pq;
	  map<int,int> S;
	  for(int i=0; i<n; i++){
	     int tmp; scanf("%d",&tmp);
		 if (S.find(tmp)==S.end()) S[tmp]=1;
		 else S[tmp]++;
	  }
	  vis.reset();
	  
	  int ctr=0;
	  while(!S.empty()){
	     ctr++;
		 int x=S.begin()->first;
		 
		 if (S.begin()->second==1) S.erase(S.begin());
		 else S.begin()->second--;
		 
		 map<int,int>::iterator it=S.upper_bound(cap-x);
		 if (it==S.begin()) continue;
		 it--;
		 
		 if ((it->second)==1) S.erase(it);
		 else (it->second)--;
	  }
	  printf("Case #%d: %d\n",cs+1,ctr);
   }
}