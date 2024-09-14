//Double Quotes "":
//Used for string literals, which are arrays of characters ending with a null terminator ('\0').
//For example, "A" is a string literal of type const char*, meaning it points to the first character of a null-terminated array of characters.
//Single Quotes '':
//Used for character literals, which represent a single character.
//For example, 'A' is a character literal of type char.

#include<bits/stdc++.h>

using namespace std;

int cnt = 1;
void hanoi(char from, char to, char help, int n)
{
    if (n == 1){
        cout << cnt++ << ' ' << from << ' ' << to << '\n';
        return;
    }

    hanoi(from, help, to, n - 1);
    cout << cnt++ << ' ' << from << ' ' << to << '\n';
    hanoi(help, to, from, n - 1);
}
int main(){
    int n;
    cin >> n;
    hanoi('A', 'B', 'C', n);
}


// second approach
#include <iostream>
using namespace std;
int num = 1;
void hanoi(char from, char rahbar, char to, int n) {
    if (n != 1) hanoi(from, to, rahbar, n - 1);
    cout << num << " " << from << " " << to << "\n";
    num++;
    if (n != 1) hanoi(rahbar, from, to, n - 1);
}
int main() {
    int n;
    cin >> n;
    hanoi('A', 'C', 'B', n);
    return 0;
}
C++