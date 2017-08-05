#include <iostream>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

long long ssd(long long n, long long p) {
    long long div_sum = 0;
    long long i = 1;
    long long q = long(sqrt(n));
    while (i <= q) {
        div_sum = (div_sum + ((i % p) * (n / i)) % p) % p;
        i += 1;
    }
    i = 1;
    long long m;
    long long k = (q % p)*((q+1) % p) % p;
    while (i*i <= n) {
        m = n / i;
        div_sum = (div_sum + ((m % p)*((m+1) % p) - k)/2 % p) % p;
        i += 1;
    }
    return div_sum;
}





long long lattice_count(long long n, long long p) {
    long long n2 = n * n;
    cout << "Evaluating first sum" << flush;
    long long u = (8 * ssd(n2,p)) % p;
    cout << endl << "Evaluating second sum" << flush;
    long long v = (32 * ssd(n2/4,p)) % p;
    long long s = ((1 + u) % p - v) % p;
    while (s < 0) s = s + p;
    return s;
}

int main() {
    long long p      = 1000000007LL;
    long long radius = 100000000LL;
    cout << endl << "Result is " << lattice_count(radius, p) << endl;
    return 0;
}
