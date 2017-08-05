#include <iostream>
#include <map>
#include <cmath>
#include <functional>
#include <numeric>

void compute_divisors(int n, std::map<int, int>& divisors) {
    divisors.clear();
    int ns = static_cast<int>(std::sqrt(n)+1);
    if (n % 2 == 0) {
        int counter = 0;
        while (n % 2 == 0) {
            n = n/2;
            ++counter;
        }
        divisors[2] = counter - 1;
    }
    int cd = 3;
    while (n > ns) {
        if (n % cd == 0) {
            int counter = 0;
            while (n % cd == 0) {
                n = n / cd;
                ++counter;
            }
            divisors[cd] = counter;
        }
        cd +=2;
    }
    if (n > 1) divisors[n] = 1;
    return;
}

int num_divisors(std::map<int, int>& divisors) {

    int ret_val = 1;
    for (auto iter: divisors) {
        ret_val *= (1 + iter.second);
    }
    return ret_val;
}

int tri(int n) {
    return reinterpret_cast<int> (n*(n+1)/2);
}



int main()
{
    std::map<int, int> even_div;
    std::map<int, int> odd_div;
    int i = 2;
    compute_divisors(i, even_div);
    compute_divisors(i+1, odd_div);
    int num_even_div = num_divisors(even_div);
    int num_odd_div = num_divisors(odd_div);

    while (num_even_div * num_odd_div < 501) {
        i += 1;
        if ((i + 1) % 2 == 0) {
          compute_divisors(i + 1, even_div);
          num_even_div = num_divisors(even_div);
        }
        else {
          compute_divisors(i + 1, odd_div);
          num_odd_div = num_divisors(odd_div);
        }
    }
    std::cout << tri(i) << " " << num_even_div * num_odd_div << std::endl;
    return 0;
}

