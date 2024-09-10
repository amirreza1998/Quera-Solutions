#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int recursive(int x){
    if(x == 0) return 5;

    int recursive_result = recursive(x - 1);

    if(x % 2 == 0) return recursive_result - 21;
    else return recursive_result * recursive_result;
};
int main(){
    int x ;
    cin >> x;
    cout << recursive(x);
    return 0;
}