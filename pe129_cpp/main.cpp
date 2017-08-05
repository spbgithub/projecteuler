#include <iostream>

using namespace std;

int period_n(int n) {
    int per = 0;
    int q = 1;
    while (q != 0) {
        q = q * 10 + 1;
        per += 1;
        q = q % n;
    }
    return per;
}

int power_mod(int a, int n, int m) {
    if (n == 0) return 1;
    if (n == 1) return a % m;
    int r = power_mod(a, n/2, m);
    if (n % 2 == 0) {
        return (r * r) % m;
    }
    else {
        return ( ( (r * r) % m) * a) % m;
    }
}

int main()
{
    int n = 1000001;
    while (1) {
        if (n % 5 != 0) {
            if (period_n(n) > 1000000) {
                std::cout << n << "," << period_n(n) << std::endl;
                break;
            }
        }
        n += 2;
        if (n % 10000 == 1) {
            std::cout << "mark" << std::endl;
        }
    }
}

