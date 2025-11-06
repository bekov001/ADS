#include <bits/stdc++.h>
using namespace std;

using int64 = long long;

const int64 MOD1 = 1'000'000'007LL;
const int64 MOD2 = 1'000'000'009LL;
const int64 B1   = 911'382'323 % MOD1;
const int64 B2   = 972'663'749 % MOD2;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S;
    if (!(cin >> S)) return 0;
    int n = (int)S.size();

    int k;
    cin >> k;
    vector<string> pats(k);
    for (int i = 0; i < k; ++i) cin >> pats[i];

    // префиксные степени
    vector<int64> p1(n + 1, 1), p2(n + 1, 1);
    for (int i = 1; i <= n; ++i) {
        p1[i] = (p1[i - 1] * B1) % MOD1;
        p2[i] = (p2[i - 1] * B2) % MOD2;
    }

    // префиксные хеши строки S (1-индексация)
    vector<int64> h1(n + 1, 0), h2(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        int c = (S[i - 1] - 'a' + 1); // ord(ch)-96
        h1[i] = (h1[i - 1] * B1 + c) % MOD1;
        h2[i] = (h2[i - 1] * B2 + c) % MOD2;
    }

    auto get_hash = [&](int l, int r) {
        // l, r включительно, 0-индексация
        int L = l, R = r;
        int64 x1 = (h1[R + 1] - (h1[L] * p1[R - L + 1]) % MOD1 + MOD1) % MOD1;
        int64 x2 = (h2[R + 1] - (h2[L] * p2[R - L + 1]) % MOD2 + MOD2) % MOD2;
        return pair<int64,int64>{x1, x2};
    };

    auto hash_str = [&](const string& t) {
        int64 a1 = 0, a2 = 0;
        for (char ch : t) {
            int c = (ch - 'a' + 1);
            a1 = (a1 * B1 + c) % MOD1;
            a2 = (a2 * B2 + c) % MOD2;
        }
        return pair<int64,int64>{a1, a2};
    };

    vector<int> diff(n + 1, 0);

    for (const string& t : pats) {
        int m = (int)t.size();
        if (m == 0 || m > n) continue;
        auto ht = hash_str(t);
        int r = m - 1;
        for (int l = 0; l <= n - m; ++l, ++r) {
            if (get_hash(l, r) == ht) {
                diff[l] += 1;
                diff[r + 1] -= 1;
            }
        }
    }

    int cur = 0;
    bool ok = true;
    for (int i = 0; i < n; ++i) {
        cur += diff[i];
        if (cur == 0) { ok = false; break; }
    }

    cout << (ok ? "YES" : "NO") << '\n';
    return 0;
}
