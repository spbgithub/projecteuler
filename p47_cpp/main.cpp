#include <iostream>

#include <vector>

int prime_count(int num) {
    int ret_val = 0;
    int div = 2;
    while (num > 1) {
        if (num % div == 0) {
            ret_val += 1;
            while (num % div == 0) {
                num = num / div;
            }
        }
        if (div > 2) {
            div += 2;
        }
        else {
            div += 1;
        }
    }
    return ret_val;
}

int main()
{
    int cur_int = 4;
    std::vector<int> consecutive;

    while (true) {
        if (prime_count(cur_int) == 4) {
            consecutive.clear();
            consecutive.push_back(cur_int);
            int j = 1;
            while (prime_count(cur_int - j) == 4 && j < 4) {
                consecutive.insert(consecutive.begin(), cur_int - j);
                j++;
            }
            if (consecutive.size() == 4) break;
            j = 1;
            while (prime_count(cur_int + j) == 4 && j < 4) {
                consecutive.push_back(cur_int + j);
                j++;
            }
            if (consecutive.size() == 4) break;
        }

        cur_int +=4;
    }

    for (auto i: consecutive) {
        std::cout << i << std::endl;
    }
    return 0;
}

