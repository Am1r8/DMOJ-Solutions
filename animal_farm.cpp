#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <queue>
#include <bits/stdc++.h>

typedef std::pair<int, int> ii;
using namespace std;

int m, e, temp[18], key[1002], x, y, cost;
const int INF = 9999999;
ii curr;
//Pen, weight
ii corners[1002][1002];
//Adjlist[pen i] -> penj, w
map<int, int> adjList[102];
bool connected[1002];

int prim(int start) {
  priority_queue<ii, vector<ii>, greater<ii>> pq;
  memset(connected, false, sizeof(connected));
  for (int i = start ; i < m+1; i++) key[i] = INF;
  key[start] = 0;
  int cost = 0;
  pq.push(make_pair(0, start));
  while (!pq.empty()) {
    curr = pq.top(); pq.pop();
    connected[curr.second] = true;
    for (ii e : adjList[curr.second]) {
      if (!connected[e.first] && e.second < key[e.first]) {
        key[e.first] = e.second;
        pq.push(make_pair(e.second, e.first));
      }
    }
  }
  for (int i = start; i < m+1; i++) {
    cost += key[i];
  }
  return cost;
}
int main() {
  scanf("%d", &m);

  for (int i = 1; i < m+1; i++) {
    scanf("%d", &e);
    //Scan line
    for (int j = 0 ; j < e*2; j++) scanf("%d", &temp[j]);

    for (int c = 0; c < e; c++) {
      x = temp[c]; y = temp[(c+1)%e]; cost = temp[c+e];
      if (corners[x][y].first == 0) {
        corners[x][y].first = i; 
        corners[x][y].second = cost;
        corners[y][x].first = i;
        corners[y][x].second = cost;
      }
      else {
        if (adjList[i].find(corners[x][y].first) == adjList[i].end()) {
          adjList[i][corners[x][y].first] = cost;
          adjList[corners[x][y].first][i] = cost;
        }
        else {
          adjList[i][corners[x][y].first] = min(adjList[i][corners[x][y].first],cost);
          adjList[corners[x][y].first][i] = min(adjList[i][corners[x][y].first],cost);
        }
        corners[x][y].first = 0; corners[y][x].first = 0;
      }
    }
  }
  int cost1 = prim(1);
  for (int i = 0; i < 1001; i++) {
    for (int j = 0 ; j < 1001; j++) {
      if (corners[i][j].first > 0) {
        if (adjList[0].find(corners[i][j].first) == adjList[0].end()) {
          adjList[0][corners[i][j].first] = corners[i][j].second;
          adjList[corners[i][j].first][0] = corners[i][j].second;
        }
        else {
          adjList[0][corners[i][j].first] = min(corners[i][j].second, adjList[0][corners[i][j].first]);
          adjList[corners[i][j].first][0] = min(corners[i][j].second, adjList[0][corners[i][j].first]);
        }
      }
    }
  }

  printf("%d", min(cost1, prim(0)));
}