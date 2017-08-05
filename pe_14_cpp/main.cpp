#include <iostream>
#include <vector>

typedef long long size_type;

int main() {
    const size_type MAX_SIZE = 1000000;
    size_type max_num_steps = 1;
    size_type max_step_loc = 2;
    size_type j = 0;
    size_type cur_num_steps = 0;

    for (size_type i = 3; i < MAX_SIZE; ++i) {
        j = i;
        cur_num_steps = 0;

        while (j > 1) {
            if (j % 2 == 0) {
                while (j % 2 == 0) {
                    ++cur_num_steps;
                    j = j/2;
                }
            }
            else {
                ++cur_num_steps;
                j = 3*j + 1;
            }
        }
        if (i == 837799) std::cout << cur_num_steps << std::endl;
        if (cur_num_steps > max_num_steps) {
            max_num_steps = cur_num_steps;
            max_step_loc = i;
        }
    }
    std::cout << max_num_steps << " " << max_step_loc << std::endl;
    return 0;
}

