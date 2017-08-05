std::vector<int> lex_perm2(int sought_perm) {
    std::vector<int> digits = {1,2,3,4,5,6,7,8,9};
    int cur_index = 0;
    int div_size = 40320;
    while (cur_index < 8) {
        int digit = sought_perm / div_size;
        sought_perm /= div_size;
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

def lex_perm2(sought_perm):
    digits = [1,2,3,4,5,6,7,8,9]
    cur_index = 0
    div_size = 40320

    while (cur_index < 8):
        digit = sought_perm / div_size;
        sought_perm = sought_perm % div_size;
        swap = digits[cur_index + digit]
        j = cur_index + digit
        while j > cur_index:
            digits[j] = digits[j-1]
        digits[cur_index] = swap
        div_size = div_size/(8 - cur_index)
        cur_index += 1
    return digits
