#include <iostream>
#include <vector>
#include <queue>
#include<cstring>
#include <algorithm>

using namespace std;

struct inform {
    int x,y;
    int point;
    int time;
};

int map[10][10];
int rec[10][10];

int N,M,K;
//route recored
int routex[10][10];
int routey[10][10];

//attack or not 
int checked[10][10];

int cnt=1;

//position
vector<inform> pos_vec;

bool cmp(inform a, inform b){
    if(a.point != b.point) return a.point < b.point;
    else if(a.time != b.time) return a.time > b.time;
    else if ((a.x+a.y) != b.x+b.y) return a.x+a.y > b.x+b.y;
    else return a.y > b.y;
}

void findTargets(){
    sort(pos_vec.begin(), pos_vec.end(), cmp);
    int ax = pos_vec[0].x; int ay = pos_vec[0].y;

    map[ay][ax]+=N+M;
    rec[ay][ax] = cnt;

    checked[ay][ax] = 1;

    pos_vec[0].point = map[ay][ax];
    pos_vec[0].time = cnt;

}



bool laser(){
    int dx[]={1,0,-1,0};
    int dy[]={0,-1,0,1};

    inform attacker = pos_vec[0];
    int ax = attacker.x; int ay = attacker.y;
    int attack_point = attacker.point;

    // target

    inform target = pos_vec[pos_vec.size()-1];
    int tar_x = target.x;
    int tar_y = target.y;
    checked[tar_y][tar_x] = 1;
    //laser or not
    bool usedLaser=false;
    
    std::queue<pair<int,int>> q;
    int visited[10][10];
    memcpy(visited,0,sizeof(visited));
    visited[ay][ax]=1; 

    q.push(make_pair(ay,ax));
    
    while(!q.empty()){
        pair<int,int>pos = q.front(); 
        // std::cout<<"laserCal: "<<recentInform.x<<recentInform.y<<std::endl;
       q.pop();
        int reX = pos.second; int reY = pos.first;
        if(reX==tar_x && reY == tar_y){
            std::cout<<"laserCheck";
            map[reY][reX]-=attack_point;
            
            int rx = routex[reY][reX];
            int ry = routey[reY][reX];

            while((rx!=ax) &&(ry!=ay)){
                map[ry][rx]-=attack_point/2;
                checked[ry][rx]=1;

                int nrx = routex[ry][rx];
                int nry = routey[ry][rx];
            }

            usedLaser=true;
            break;
            }
        for( int i=0; i<4; i++){
            int nx = reX+dx[i];
            int ny = reY+dy[i];
            // std::cout<<"nx: "<<nx<<std::endl;
            if(nx >= N) nx = 0;
            if(ny >=M) ny = 0;
            if(nx <0) nx=N-1;
            if(ny<0) ny=M-1;
            if(visited[ny][nx]) continue;
            if(map[ny][nx] < 1) continue;
            
            visited[ny][nx]=1;
            q.push(make_pair(ny,nx));
            routex[nx][ny]=reX;
            routey[nx][ny]=reY;
        }
    }
    return usedLaser;


}

void bomb(){
    inform attacker = pos_vec[0];
    int ax = attacker.x; int ay = attacker.y;
    int attack_point = attacker.point;

    inform target = pos_vec[pos_vec.size()-1];

    int tar_x = target.x; int tar_y = target.y;
    map[tar_y][tar_x]-=attack_point;
    
    int dx[]={1,1,1,-1,-1,-1,0,0};
    int dy[]={0,-1,1,0,-1,1,1,-1};

    for( int i=0; i<8; i++){
        int nx = dx[i]+tar_x;
        int ny = dy[i]+tar_y;

        if(nx >= N) nx = 0;
        if(ny >=M) ny = 0;
        if(nx <0) nx=N-1;
        if(ny<0) ny=M-1;

        if(map[ny][nx]<1) continue;

        map[ny][nx]-=(attack_point/2);
        checked[ny][nx]=1;
    }

}

void notUsed(){
   
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if(checked[i][j]>0) continue;
                
            else {
                if(map[i][j] < 1) continue;
                else map[i][j]++;
            }
        }
    }

}

int main() {
    
    std::cin>>N>>M>>K;
  
    bool flag;
    for(int n=0; n<N; n++){
        for(int m=0; m<M; m++){
            int value;
            std::cin>>value;
            map[n][m]=value;
            
        }
    }

   
    while(K){
    
        memcpy(checked , 0 , sizeof(checked));
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                if(map[i][j] > 0){
                    inform newPos ;
                    newPos.x = j; newPos.y = i;
                    newPos.point = map[i][j];
                    newPos.point=rec[i][j];

                    pos_vec.push_back(newPos);
                }
            }
        }
        if(pos_vec.size() <=1 ) break;
        findTargets();
        bool usedLaser = laser();

        if(!usedLaser) bomb();

        notUsed();
        K--;
        cnt++;
    }
    
    
    int max=0;
    for(int m=0; m<M; m++){
        for(int n=0; n<N; n++){
            if(map[m][n] > max) max = map[m][n];
        }
    }
    std::cout<<max;
    return 0;
}