#include <iostream>
#include <set>
#include <stack>

typedef unsigned long numsize;

using namespace std;

numsize digit_square_sum(numsize n) {
    numsize ret_val = 0;
    numsize digit = 0;
    while (n > 0) {
        digit = n % 10;
        ret_val += digit*digit;
        n = n / 10;
    }
    return ret_val;
}


int main()
{
    set<numsize> to1;
    to1.insert(1);

    set<numsize> to89;
    to89.insert(89);

    numsize k = 1;
    long total = 0;
    for (k = 1; k <= 10000000; ++k) {
        if (k % 1000 == 0) {
            cout << k << endl;
        }
        stack<numsize> s;
        s.push(k);
        //numsize num = k;
        while (true) {
            if (to1.find(s.top()) != to1.end()) {
                while (s.size() > 0) {
                    to1.insert(s.top());
                    s.pop();
                }
                break;
            }
            if (to89.find(s.top()) != to89.end()) {
                while (s.size() > 0) {
                    to89.insert(s.top());
                    s.pop();
                }
                total += 1;
                break;
            }

            s.push(digit_square_sum(s.top()));
            /*if (num == 1) {break;}
            if (num == 89) {
                total += 1;
                break;
            }
            num = digit_square_sum(num);*/
        }
    }
    cout << total << endl;
}

