#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!getline(cin, s)) return 0;
    int n = (int)s.size();

    const uint32_t MOD1 = 1000000007u, MOD2 = 1000000009u;
    const uint64_t B1 = 911382323ull, B2 = 972663749ull;

    vector<uint32_t> p1(n+1, 1), p2(n+1, 1);
    vector<uint32_t> h1(n+1, 0), h2(n+1, 0);

    for (int i = 1; i <= n; ++i) {
        p1[i] = (uint64_t)p1[i-1] * B1 % MOD1;
        p2[i] = (uint64_t)p2[i-1] * B2 % MOD2;
        h1[i] = ((uint64_t)h1[i-1] * B1 + (unsigned char)s[i-1]) % MOD1;
        h2[i] = ((uint64_t)h2[i-1] * B2 + (unsigned char)s[i-1]) % MOD2;
    }

    auto get_hash = [&](int l, int r) { 
        uint32_t x1 = (h1[r] + MOD1 - (uint64_t)h1[l] * p1[r-l] % MOD1) % MOD1;
        uint32_t x2 = (h2[r] + MOD2 - (uint64_t)h2[l] * p2[r-l] % MOD2) % MOD2;
        return (uint64_t)x1 << 32 | x2;
    };

    unordered_set<uint64_t> seen;
    seen.reserve((size_t)n * (n + 1) / 2);

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            seen.insert(get_hash(i, j));
        }
    }

    cout << seen.size() << '\n';
    return 0;
}
