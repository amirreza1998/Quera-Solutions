 // first approach
 #include <iostream>

 using namespace std;

 long long gcd(long long a, long long b)
 {
     return (b == 0LL ? a : gcd(b, a % b));
 }

 int main()
 {
     long long a, b;
     cin >> a >> b;
     cout << gcd(a, b) << '\n';
     return 0;
 }

 // second approach
#include <iostream>
using namespace std;

long long gcd(long long x, long long y){
    if(y == 0LL) return x;
    return gcd(y, x % y);
}
int main() {
    int y; int x;
    cin >> y >> x;
    cout << gcd(x, y) << '\n';
    return 0;
}
