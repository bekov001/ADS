#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val;
    Node* left;
    Node* right;
    Node(int v): val(v), left(nullptr), right(nullptr) {}
};

Node* insertNode(Node* node, int value) {
    if (!node) return new Node(value);
    if (value < node->val) node->left = insertNode(node->left, value);
    else if (value > node->val) node->right = insertNode(node->right, value);
    // дубликаты игнорируем, как в исходном коде
    return node;
}

int ans = 0;

int dfs(Node* u) {
    if (!u) return 0;
    int hl = dfs(u->left);
    int hr = dfs(u->right);
    ans = max(ans, hl + hr + 1);
    return max(hl, hr) + 1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    Node* root = nullptr;
    for (int i = 0; i < n; ++i) {
        int v; cin >> v;
        root = insertNode(root, v);
    }
    dfs(root);
    cout << ans << "\n";
    return 0;
}
