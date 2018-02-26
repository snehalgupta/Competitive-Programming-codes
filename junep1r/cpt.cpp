#include <map>
#include <set>
#include <list>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std; 


struct Edge {
	int x;
	int y;
	int cost;
	Edge(int X, int Y, int Cost) 
	{ x = X; 
	  y = Y;
	  cost = Cost; }
	bool operator < (const Edge b) const {
		return cost != b.cost ? cost < b.cost : (x < b.x || (x == b.x && y < b.y));
	}
};

struct DSU {
	vector<int> p;
	vector<int> r;
	DSU(int size) {
		r.resize(size);
		p.resize(size);
		for (int i = 0; i < size; i++){
			p[i] = i;
			r[i]=1;}
	}
	DSU() {}

	int get(int x) 
	{ return p[x] == x ? x : (p[x] = get(p[x])); }

	bool unite(int x, int y) {
		x = get(x);
		y = get(y);
		if (y == x)
			return false;
		if (r[y] > r[x])
			swap(x,y);
		p[y] = x;
		r[x] =r[x]+ r[y];
		return true;
	}
};

vector<pair<Edge,int> > edges;
vector<string> answer;DSU dsu;
vector<vector<int> > g;
vector<int> u;
vector<int> d;
vector<int> l;
int n;
int m;
int globalCounter;

void dfs(int v, int p = -1, int depth = 0) {
	l[v]  = depth;
	d[v] = depth;
	u[v] = globalCounter+1;
	for (int i = 0; i < (int)g[v].size(); i++) {
		if (g[v][i] == p)
		continue;
		int id = g[v][i];
		int x = dsu.get(edges[id].first.x);
		int y = dsu.get(edges[id].first.y);
		int to;
		if(x == v)
		to=y;
		else{
		to=x;
		}

		if (u[to]>globalCounter)
			l[v] = l[v] < d[to] ? l[v] : d[to];
		else {
			dfs(to, g[v][i], depth+1);
			l[v] = l[v] < l[to] ? l[v] : l[to];
		}

		if (l[to] > d[v]) {
			answer[edges[g[v][i]].second] = "any";
		}
	}
}

void solve() {
	cin >> n ;
	cin >> m;
	d.resize(n); 
	l.resize(n); 
	u.resize(n);
	g.assign(n, vector<int> ());
	answer.assign(m, "at least ");

	dsu = DSU(n);
	int sdf=0;
	while (sdf < m) {
		int x;
		int y;
		int z;
		cin >> x ;
		cin>> y ;
		cin>> z;
		edges.push_back(make_pair(Edge(x-1,y-1,z),sdf));
		sdf++;
	}

	sort(edges.begin(), edges.end());
	for (int i = 0; i < m;) {
		int k = i;
		while (k < (int)edges.size() && edges[k].first.cost == edges[i].first.cost)
			k++;
		for (int j = i; j < k; j++) {
			int x;
			int y;
			x = dsu.get(edges[j].first.x);
			y = dsu.get(edges[j].first.y);

			if (y != x) {
				g[x].push_back(j);
				g[y].push_back(j);
			} else if(y == x)
				answer[edges[j].second] = "none";
		}

		for (int j = i; j < k; j++) {
			int x;
			int y;
			x = dsu.get(edges[j].first.x);
			y = dsu.get(edges[j].first.y);
			if (globalCounter>=u[x])
				dfs(x);
			if (globalCounter>=u[y])
				dfs(y);
		}
		for (int j = i; j < k; j++) {
			int x;
			int y;
			x = dsu.get(edges[j].first.x);
			y = dsu.get(edges[j].first.y);
			dsu.unite(x, y);
			g[x].clear();
			g[y].clear();
		}

		i = k;
		globalCounter++;
	}
	int count=0;
	int sdks=0;
	while( sdks< m){
		if(answer[sdks] == "none"){
			count=count+1;
		}
		sdks=sdks+1;
		}
	cout<<count;
}

int main() {
	ios_base::sync_with_stdio(0);
	solve();
	return 0;
}

