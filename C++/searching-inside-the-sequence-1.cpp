#include <iostream>  

using namespace std;  

int main() {  
    int n, q;  
    cin >> n >> q;  
    
    int a[n];
    for(int i = 0; i < n; i++) {  
        cin >> a[i];
    }  
 
    for(int i = 0; i < q; i++) {  
        int x;  
        cin >> x; 
        
        int count = 0;
        for(int item : a) {  
            if(item < x) {  
                count++;
            }  
        }  
        cout << count << "\n";
    }  
    return 0;  
}  