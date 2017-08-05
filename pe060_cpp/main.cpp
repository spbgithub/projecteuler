#include <iostream>
#include <cmath>
#include <vector>
#include <set>
#include <fstream>


//#include <boost/algorithm/string.hpp>
using namespace std;

long concat_nums(long m, long n) {
    int u = int(std::log10(m)) + 1;
    return 10^u * m + n;
}

std::vector<long> read_prime_list() {
    std::ifstream prime_list;
    prime_list.open("/home/sean/workspace/projecteuler/primes1.txt");

}

int main()
{
    cout << "Hello World!" << endl;
    return 0;
}

