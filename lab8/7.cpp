#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;
    int n = (int)s.size();

    int q;
    cin >> q;
    vector<pair<int,int>> queries(q);
    for (int i = 0; i < q; ++i) {
        int l, r; cin >> l >> r;
        --l; 
        queries[i] = {l, r};
    }


    const uint32_t MOD1 = 1000000007u, MOD2 = 1000000009u;
    const uint64_t  B1   = 911382323ull, B2   = 972663749ull;

    vector<uint32_t> p1(n+1, 1), p2(n+1, 1), h1(n+1, 0), h2(n+1, 0);
    for (int i = 1; i <= n; ++i) {
        p1[i] = (uint64_t)p1[i-1] * B1 % MOD1;
        p2[i] = (uint64_t)p2[i-1] * B2 % MOD2;
        h1[i] = ((uint64_t)h1[i-1] * B1 + (unsigned char)s[i-1]) % MOD1;
        h2[i] = ((uint64_t)h2[i-1] * B2 + (unsigned char)s[i-1]) % MOD2;
    }

    auto get_hash = [&](int l, int r) -> uint64_t {
        uint32_t x1 = (h1[r] + MOD1 - (uint64_t)h1[l] * p1[r-l] % MOD1) % MOD1;
        uint32_t x2 = (h2[r] + MOD2 - (uint64_t)h2[l] * p2[r-l] % MOD2) % MOD2;
        return (uint64_t)x1 << 32 | x2;
    };

    unordered_map<int, unordered_map<uint64_t,int>> cache;
    cache.reserve(1024);

    auto ensure_len = [&](int L) {
        if (cache.find(L) != cache.end()) return;
        unordered_map<uint64_t,int> cnt;
        if (L <= n) {
            cnt.reserve((size_t)max(0, n - L + 1) * 2);
            for (int i = 0; i + L <= n; ++i) {
                ++cnt[get_hash(i, i + L)];
            }
        }
        cache.emplace(L, move(cnt));
    };

    ostringstream out;
    for (auto [l, r] : queries) {
        int L = r - l;
        ensure_len(L);
        uint64_t key = get_hash(l, r);
        auto &cnt = cache[L];
        auto it = cnt.find(key);
        out << (it == cnt.end() ? 0 : it->second) << '\n';
    }

    cout << out.str();
    return 0;
}
