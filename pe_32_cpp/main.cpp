#include <vector>
#include <iostream>

int fact(int n) {
    if (n == 0) return 1;
    return n * fact(n-1);
}

std::vector<int> lex_perm(int sought_perm) {
    std::vector<int> ordered_digits = {1,2,3,4,5,6,7,8,9};
    //int div_size = fact(ordered_digits.size() - 1);
    int div_size = 40320;
    std::vector<int> perm_digits;
    while (ordered_digits.size() > 1) {
        int digit = sought_perm / div_size;
        sought_perm = sought_perm % div_size;
        perm_digits.push_back(ordered_digits[digit]);
        ordered_digits.erase(ordered_digits.begin() + digit);
        div_size = div_size / ordered_digits.size();
    }
    perm_digits.push_back(ordered_digits[0]);
    return perm_digits;
}

std::vector<int> lex_perm2(int sought_perm) {
    std::vector<int> digits = {1,2,3,4,5,6,7,8,9};
    int cur_index = 0;
    int div_size = 40320;
    while (cur_index < 8) {
        int digit = sought_perm / div_size;
        sought_perm = sought_perm % div_size;
        int swap = digits[cur_index + digit];
        for (int j = cur_index + digit; j > cur_index; --j) {
            digits[j] = digits[j-1];
        }
        digits[cur_index] = swap;
        div_size = div_size/(8 - cur_index);
        ++cur_index;
    }
    return digits;
}

int list_slice_to_int(std::vector<int>& int_list, int start, int finish) {
    int ret_val = 0;
    int power = 1;
    int j = finish - 1;

    while (j >= start) {
        ret_val += power * int_list[j];
        power *= 10;
        --j;
    }
    return ret_val;
}

int is_pandigital(std::vector<int>& dig_list, std::vector<int>& pattern) {
    int a = list_slice_to_int(dig_list, pattern[0], pattern[1]);
    int b = list_slice_to_int(dig_list, pattern[1], pattern[2]);
    if (a > b) return 0;
    int ab = list_slice_to_int(dig_list, pattern[2], pattern[3]);
    if (a * b == ab) return ab;
    return 0;
}

int main()
{
    int num_perms = fact(9);
    std::vector<int> prods;
    std::vector<std::vector<int> > pattern_list;
    pattern_list.push_back({0,1,5,9});
    pattern_list.push_back({0,2,5,9});
    pattern_list.push_back({0,3,6,9});

    for (int i = 0; i < num_perms; ++i) {
        std::vector<int> dig_list = lex_perm2(i);
        for (auto p: pattern_list) {
            int prod = is_pandigital(dig_list, p);
            if (prod > 0) prods.push_back(prod);
        }
    }

    for (auto z : prods) {
        std::cout << z << std::endl;
    }
    return 0;
}

