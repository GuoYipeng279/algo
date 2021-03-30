// n, w = map(int, input().split())
// inp = []
// for i in range(w):
//     inp.append(input().split())
// n = 3
// w = 2
// inp = [[2,1,2],[2,1,3]]
#include<iostream>
#include<vector>
#include<stdio.h>
using namespace std;
void Solution(int n, int w, vector<vector<int>> inp){
    vector<int> rec(n,0);
    vector<int> ran(1,1);
    vector<int> avg(n,0);
    vector<vector<int>>::iterator i;
    for(i=inp.begin(); i!=inp.end(); ++i){
        vector<int>::iterator j;
        for(j=i->begin()+1; j!=i->end(); ++j){
            // j = int(j)
            int ori = rec[*j-1];
            int neo = rec[*j-1]+1;
            rec[*j-1] += 1;
            ran[ori] += 1;
            if(ran.size() == neo){
                ran.push_back(1);
            }
        }
        for(int k=0; k<n; ++k){
            avg[k] += ran[rec[k]]/w;
        }
    }
    vector<int>::iterator ii;
    for(ii=avg.begin(); ii!=avg.end(); ++i){
        cout << *ii;
    }
}

int main(){
    return 0;
}