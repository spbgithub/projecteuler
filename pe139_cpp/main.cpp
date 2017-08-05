#include <iostream>
#include <vector>
#include <ctime>
#include <queue>
#include <string>

using namespace std;
const int MAX_PER = 100000000;

inline int t1a(int a, int b, int c) {
    return a - 2*b + 2*c;
}

inline int t1b(int a, int b, int c) {
    return 2*a - b + 2*c;
}

inline int t1c(int a, int b, int c) {
    return 2*a - 2*b + 3*c;
}

inline int t2a(int a, int b, int c) {
    return a + 2*b + 2*c;
}

inline int t2b(int a, int b, int c) {
    return 2*a + b + 2*c;
}

inline int t2c(int a, int b, int c) {
    return 2*a + 2*b + 3*c;
}

inline int t3a(int a, int b, int c) {
    return -a + 2*b + 2*c;
}

inline int t3b(int a, int b, int c) {
    return -2*a + b + 2*c;
}

inline int t3c(int a, int b, int c) {
    return -2*a + 2*b + 3*c;
}

int new_triple(int a, int b, int c, string s) {
    if (a + b + c >= MAX_PER) {
        return 0;
    }
    int ret_val = 0;
    if (c % (b - a) == 0) {
        ret_val = MAX_PER / (a + b + c);
        cout << a << "," << b << "," << c << ":" << s << endl;
        //return MAX_PER / (a + b + c) + new_triple(t1a(a,b,c),t1b(a,b,c),t1c(a,b,c)) + new_triple(t2a(a,b,c),t2b(a,b,c),t2c(a,b,c)) + new_triple(t3a(a,b,c),t3b(a,b,c),t3c(a,b,c));
    }
    return ret_val + new_triple(t1a(a,b,c),t1b(a,b,c),t1c(a,b,c),s+"1") + new_triple(t2a(a,b,c),t2b(a,b,c),t2c(a,b,c),s+"2") + new_triple(t3a(a,b,c),t3b(a,b,c),t3c(a,b,c),s+"3");
    return 0;
}



int main()
{
    double T = clock();

    cout << new_triple(3,4,5,"") << endl;
    cout << (clock() - T) / CLOCKS_PER_SEC << endl;

    return 0;
}

