#include <bits/stdc++.h>
using namespace std;

struct Node {
    int val;
    Node *left, *right;
    Node(int v): val(v), left(nullptr), right(nullptr) {}
};

Node* push(Node* node, int value) {
    if (!node) return new Node(value);
    if (value < node->val) node->left = push(node->left, value);
    else if (value > node->val) node->right = push(node->right, value);
    return node;
}

Node* trace(char letter, Node* node) {
    return (letter == 'R') ? (node->right ? node->right : nullptr)
                           : (node->left  ? node->left  : nullptr);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    Node* root = nullptr;
    for (int i = 0, x; i < n; ++i) {
        cin >> x;
        root = push(root, x);
    }

    for (int i = 0; i < q; ++i) {
        string path;
        cin >> path;
        Node* node = root;
        bool ok = true;
        for (char c : path) {
            node = trace(c, node);
            if (!node) { ok = false; break; }
        }
        cout << ((ok && node) ? "YES" : "NO") << "\n";
    }
    return 0;
}
