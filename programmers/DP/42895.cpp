// N으로 표현

#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <cmath>

using namespace std;
unordered_map<int, int> memo;

/*
23:15 시작
24:50 끝

==PRUNNING==
1. depth > 8: return
2. memo[X] <= 현 depth : return 
(X는 현 노드 값)


==효율성==
1. hash map 맞아?
-> hash map 시간복잡도?

==코너케이스==
1. number == NNNNN인 경우
*/

void dfs(bool first, int& N, int& number, int depth, int X){
    if (depth > 8) return;
    bool flag_X = memo.find(X) != memo.end();
    if (!first && flag_X && memo[X] <= depth) return;
    
    // std::cout << depth << ' ' << X << '\n';
    memo[X] = depth;
    
    int cnt = depth;
    int j = 0;
    
    for (int i=N; cnt<8; i=N*pow(10, j)+i){
        dfs(false, N, number, cnt+1, X/i);
        if (X!=0) dfs(false, N, number, cnt+1, i/X);
        dfs(false, N, number, cnt+1, X-i);
        dfs(false, N, number, cnt+1, i-X);
        dfs(false, N, number, cnt+1, X+i);
        dfs(false, N, number, cnt+1, X*i); 
        j++;
        cnt++;
    }
    // 55도 됨
    
}

int solution(int N, int number) {
    
    // std::cout << "hello world" << '\n';

    for (int i=N, j=0, cnt=1; cnt<=8; i=N*pow(10, j)+i){
        // cout << "i: " << i << '\n';
        if (i == number) return cnt;
        cnt++;
        j++;
    }
    
    dfs(true, N, number, 1, N);
    
    if (memo[number] == 0)
        // only when the minimum value is above depth=8
        return -1;
    else
        return memo[number];
    
}

int main(){
    cout << solution(5, 12) << '\n';
    cout << solution(5, 31168) << '\n';
    cout << solution(3, 3333) << '\n';
    cout << solution(5, 5) << '\n';
    cout << solution(9, 99999999) << '\n';
}
