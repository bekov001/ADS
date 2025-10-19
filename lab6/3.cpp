#include <bits/stdc++.h>
using namespace std;

vector<int> mergeSort(vector<int>& arr) {
    if (arr.size() <= 1) return arr;

    int mid = arr.size() / 2;
    vector<int> left(arr.begin(), arr.begin() + mid);
    vector<int> right(arr.begin() + mid, arr.end());

    left = mergeSort(left);
    right = mergeSort(right);

    vector<int> result;
    int i = 0, j = 0;
    while (i < (int)left.size() && j < (int)right.size()) {
        if (left[i] < right[j])
            result.push_back(left[i++]);
        else
            result.push_back(right[j++]);
    }

    while (i < (int)left.size()) result.push_back(left[i++]);
    while (j < (int)right.size()) result.push_back(right[j++]);

    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> data(n);
    for (int i = 0; i < n; i++) cin >> data[i];

    data = mergeSort(data);

    int minDiff = INT_MAX;
    vector<int> res;

    for (int i = 1; i < n; i++) {
        int diff = data[i] - data[i - 1];
        if (diff < minDiff) {
            minDiff = diff;
            res = {data[i - 1], data[i]};
        } else if (diff == minDiff) {
            res.push_back(data[i - 1]);
            res.push_back(data[i]);
        }
    }

    for (int i = 0; i < (int)res.size(); i++) {
        cout << res[i];
        if (i + 1 < (int)res.size()) cout << " ";
    }
    cout << "\n";

    return 0;
}