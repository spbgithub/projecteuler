#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>

using namespace std;

long long sumsq(long long n, long long p) {
    long long n2 = n + 1;
    long long n3 = 2*n + 1;

    if (n % 3 == 0) {
        n = n/3;
    }
    else if (n2 % 3 == 0) {
        n2 = n2/3;
    }
    else {
        n3 = n3/3;
    }
    if (n % 2 == 0) {
        n = n/2;
    }
    else {
        n2 = n2/2;
    }
    n = n % p; n2 = n2 % p; n3 = n3 % p;
    return (((n * n2) % p) * n3) % p;
}

long long sssd(long long n, long long p) {
    long long div_sum = 0;
    long long i = 1;
    long long q = sqrt(n);

    while (i <= q) {
        div_sum = (div_sum + (((i % p) * (i % p)) % p * ((n / i) % p)) % p) % p;
        i += 1;
    }
    i = 1;
    long long m;
    long long k = sumsq(q,p);

    while (i*i <= n) {
        m = n / i;
        div_sum = (div_sum + (sumsq(m,p) - k) % p) % p;

        i += 1;
    }
    while (div_sum < 0) div_sum += p;

    return div_sum;
}


int main() {
    long long n = pow(10, 15);
    long long p = pow(10, 9);

    cout << sssd(n,p) << endl;
    return 0;
}
