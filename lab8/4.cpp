#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using i128 = __int128_t;

const ll MOD1 = 1'000'000'007LL;
const ll MOD2 = 1'000'000'009LL;
const ll B1 = 911'382'323 % MOD1;
const ll B2 = 972'663'749 % MOD2;

struct DH {
    vector<ll> p1, p2, h1, h2;
    void build(const string& s) {
        int n = (int)s.size();
        p1.assign(n+1, 1); p2.assign(n+1, 1);
        h1.assign(n+1, 0); h2.assign(n+1, 0);
        for (int i = 1; i <= n; ++i) {
            int c = s[i-1] - 'a' + 1;
            p1[i] = (i128)p1[i-1] * B1 % MOD1;
            p2[i] = (i128)p2[i-1] * B2 % MOD2;
            h1[i] = ((i128)h1[i-1] * B1 + c) % MOD1;
            h2[i] = ((i128)h2[i-1] * B2 + c) % MOD2;
        }
    }
    pair<ll,ll> get(int l, int r) const { // [l, r], 0-indexed
        ll x1 = (h1[r+1] - (i128)h1[l] * p1[r-l+1]) % MOD1; if (x1 < 0) x1 += MOD1;
        ll x2 = (h2[r+1] - (i128)h2[l] * p2[r-l+1]) % MOD2; if (x2 < 0) x2 += MOD2;
        return {x1, x2};
    }
};

pair<ll,ll> hash_str(const string& t) {
    ll a1 = 0, a2 = 0;
    for (char ch : t) {
        int c = ch - 'a' + 1;
        a1 = ((i128)a1 * B1 + c) % MOD1;
        a2 = ((i128)a2 * B2 + c) % MOD2;
    }
    return {a1, a2};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        int n;
        if (!(cin >> n)) return 0;
        if (n == 0) break;

        vector<string> pats(n);
        for (int i = 0; i < n; ++i) cin >> pats[i];
        string T; cin >> T;
        int N = (int)T.size();

        DH dh; dh.build(T);

        vector<int> freq(n, 0);
        int maxf = 0;

        for (int i = 0; i < n; ++i) {
            const string& p = pats[i];
            int m = (int)p.size();
            if (m == 0 || m > N) { freq[i] = 0; continue; }
            auto ht = hash_str(p);
            int cnt = 0;
            for (int l = 0; l + m <= N; ++l) {
                if (dh.get(l, l + m - 1) == ht) ++cnt;
            }
            freq[i] = cnt;
            if (cnt > maxf) maxf = cnt;
        }

        cout << maxf << '\n';
        for (int i = 0; i < n; ++i)
            if (freq[i] == maxf)
                cout << pats[i] << '\n';
    }
    return 0;
}
