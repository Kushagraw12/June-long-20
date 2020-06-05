#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++)
    {
        int n = 0, k = 0, s1 = 0, s2 = 0;
        cin >> n;
        cin >> k;
        int p[n] = {0};
        for (int j = 0; j <= (n - 1); j++)
        {
            cin >> p[j];
            if (p[j] >= k)
            {
                s2 = s2 + k;
            }
            else
            {
                s2 += p[j];
            }
            s1 = s1 + p[j];
        }
        int loss = 0;
        loss = s1 - s2;
        cout << loss << endl;
    }
    return 0;
}
