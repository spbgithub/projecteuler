#include <iostream>
#include <gmp.h>
#include <gmpxx.h>
#include <string>

const std::string Mpz_tToStr(const mpz_t& i)
{
  static char buffer[256];
  mpz_get_str(buffer,10,i);
  return std::string(buffer);
}

int main()
{
    mpz_t n;
    mpz_init_set_str(n, "3", 10);

    mpz_t d;
    mpz_init_set_str(d, "2", 10);

    mpz_t g;
    mpz_init_set_str(g, "1", 10);

    mpz_t work;
    mpz_init_set_str(work, "0", 10);

    int count = 0;
    for (int iter = 1; iter < 1000000; ++iter) {
        mpz_add(work, d, d);
        mpz_add(d, n, d);
        mpz_add(n, n, work);
        mpz_gcd(g, n, d);
        mpz_divexact(n, n, g);
        mpz_divexact(d, d, g);
        if (iter < 15) {
            std::cout << Mpz_tToStr(n) << " " << Mpz_tToStr(d) << std::endl;
        }
        if (mpz_sizeinbase(n,10) > mpz_sizeinbase(d, 10)) {
            ++count;
        }
    }
    std::cout << count << std::endl;
}

