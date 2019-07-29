#include <cstdio>
#include <algorithm>

using namespace std;

#define For(i,a,b) for(int i = a; i < b; i++)
#define FOR(i,a,b) for(int i = b-1; i >= a; i--)

double nextDouble() {
	double x;
	scanf("%lf", &x);
	return x;
}

int nextInt() {
	int x;
	scanf("%d", &x);
	return x;
}

int n;
double a1[1001], a2[1001];

int main() {

	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small.out", "w", stdout);
	
	int tt = nextInt();
	For(t,1,tt+1) {
		int n = nextInt();
		For(i,0,n)
			a1[i] = nextDouble();
		For(i,0,n)
			a2[i] = nextDouble();
		sort(a1, a1+n);
		sort(a2, a2+n);
		
		int y = 0;
		int z = 0;
		
		int p1 = 0;
		int p2 = 0;
		
		while(p1 < n) {
			if(a1[p1] < a2[p2])
				p1++;
			else {
				p1++;
				p2++;
				y++;
			}
		}
		
		p1 = 0;
		p2 = 0;
		
		while(p2 < n) {
			if(a1[p1] > a2[p2])
				p2++;
			else {
				p1++;
				p2++;
				z++;
			}
		}
		z = n - z;
		printf("Case #%d: %d %d\n", t, y, z);
	}
}
