#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, n;
    if (!(cin >> m >> n)) return 0;

    vector<vector<int>> grid(m, vector<int>(n));
    int mushrooms = 0;
    queue<array<int, 3>> q;   // {x, y, time}

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
            if (grid[i][j] == 2) {
                q.push({i, j, 0});
            } else if (grid[i][j] == 1) {
                mushrooms++;
            }
        }
    }

    if (mushrooms == 0) {
        cout << 0;
        return 0;
    }

    const int dx[4] = {-1, 1, 0, 0};
    const int dy[4] = {0, 0, -1, 1};

    int max_time = 0;

    while (!q.empty()) {
        auto cur = q.front(); q.pop();
        int x = cur[0], y = cur[1], t = cur[2];

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1) {
                grid[nx][ny] = 2;   // стало Марио
                mushrooms--;
                int nt = t + 1;
                max_time = max(max_time, nt);
                q.push({nx, ny, nt});
            }
        }
    }

    if (mushrooms > 0) cout << -1;
    else cout << max_time;

    return 0;
}
