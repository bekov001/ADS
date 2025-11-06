#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
using i128 = __int128_t;

const int64 MOD1 = 1000000007LL, MOD2 = 1000000009LL;
const int64 B1   = 911382323LL,  B2   = 972663749LL;

static inline int64 mul_mod(int64 a, int64 b, int64 mod) {
    return (int64)((i128)a * b % mod);
}

static inline int64 add_mod(int64 a, int64 b, int64 mod) {
    int64 s = a + b;
    if (s >= mod) s -= mod;
    return s;
}

static inline int64 sub_mod(int64 a, int64 b, int64 mod) {
    int64 d = a - b;
    if (d < 0) d += mod;
    return d;
}

static string read_line() {
    string s;
    getline(cin, s);
    if (!s.empty() && s.back() == '\r') s.pop_back(); // strip CR if present
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s1 = read_line();
    string s2 = read_line();
    string w  = read_line();

    int n1 = (int)s1.size(), n2 = (int)s2.size(), m = (int)w.size();
    if (m == 0 || min(n1, n2) < m) {
        cout << 0 << '\n';
        return 0;
    }

    int N = max(n1, n2);
    vector<int64> p1(N + 1, 1), p2(N + 1, 1);
    for (int i = 1; i <= N; ++i) {
        p1[i] = mul_mod(p1[i - 1], B1, MOD1);
        p2[i] = mul_mod(p2[i - 1], B2, MOD2);
    }

    auto build_pref = [&](const string& s) {
        int L = (int)s.size();
        vector<int64> h1(L + 1, 0), h2(L + 1, 0);
        for (int i = 1; i <= L; ++i) {
            int o = (unsigned char)s[i - 1];
            h1[i] = add_mod(mul_mod(h1[i - 1], B1, MOD1), o % MOD1, MOD1);
            h2[i] = add_mod(mul_mod(h2[i - 1], B2, MOD2), o % MOD2, MOD2);
        }
        return pair<vector<int64>, vector<int64>>(move(h1), move(h2));
    };

    auto get_hash = [&](const vector<int64>& h1, const vector<int64>& h2, int l, int r) {
        // hash of s[l:r]
        int len = r - l;
        int64 x1 = sub_mod(h1[r], mul_mod(h1[l], p1[len], MOD1), MOD1);
        int64 x2 = sub_mod(h2[r], mul_mod(h2[l], p2[len], MOD2), MOD2);
        return pair<int64,int64>(x1, x2);
    };

    auto [h1a, h1b] = build_pref(s1);
    auto [h2a, h2b] = build_pref(s2);
    auto [hw1, hw2] = build_pref(w);
    auto target = get_hash(hw1, hw2, 0, m);

    int limit = min(n1, n2) - m + 1;
    int ans = 0;
    for (int i = 0; i < limit; ++i) {
        if (get_hash(h1a, h1b, i, i + m) == target &&
            get_hash(h2a, h2b, i, i + m) == target) {
            ++ans;
        }
    }

    cout << ans << '\n';
    return 0;
}
