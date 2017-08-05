#include <iostream>

using namespace std;

int main()
{
    int p = 24;

    long a = 0;
    long b = 0;
    int ra = 0;
    int rb = 1;
    long astart = a;
    long bstart = b;

    long long n = 0;
    long long nmax = 1234567890123;
    long m = 1000000000;
    long c, r;
    while (n < nmax) {
        if (n % 1000000 == 0) cout << n << endl;
        c = (a + b) % m;
        r = ra + rb;
        if (r >= p) c = (c+1) % m;
        r = r % p;
        a = b;
        b = c;
        ra = rb;
        rb = r;
        n += 1;
        if (astart == a && bstart == b && n > 20) {
            cout << "Done at " << n << endl;
            break;
        }
    }
    return 0;
}
