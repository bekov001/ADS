#include <bits/stdc++.h>
using namespace std;

struct Student {
    string last;
    string first;
    double gpa;
};

// key: (gpa, last, first)
using Key = tuple<double, string, string>;

vector<Student> merge_vec(const vector<Student>& left, const vector<Student>& right,
                          const function<Key(const Student&)>& key) {
    int n = (int)left.size(), m = (int)right.size();
    vector<Key> kL(n), kR(m);
    for (int i = 0; i < n; ++i) kL[i] = key(left[i]);
    for (int j = 0; j < m; ++j) kR[j] = key(right[j]);

    int i = 0, j = 0;
    vector<Student> res;
    res.reserve(n + m);

    while (i < n && j < m) {
        if (kL[i] < kR[j]) {
            res.push_back(left[i]); ++i;
        } else {
            res.push_back(right[j]); ++j;
        }
    }
    while (i < n) { res.push_back(left[i]); ++i; }
    while (j < m) { res.push_back(right[j]); ++j; }
    return res;
}

vector<Student> mergesort_vec(const vector<Student>& arr,
                              const function<Key(const Student&)>& key) {
    if (arr.size() <= 1) return arr;
    size_t mid = arr.size() / 2;
    vector<Student> left(arr.begin(), arr.begin() + mid);
    vector<Student> right(arr.begin() + mid, arr.end());
    return merge_vec(mergesort_vec(left, key), mergesort_vec(right, key), key);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    unordered_map<string, double> GPA_MAP = {
        {"A+", 4.00}, {"A", 3.75}, {"B+", 3.50}, {"B", 3.00},
        {"C+", 2.50}, {"C", 2.00}, {"D+", 1.50}, {"D", 1.00}, {"F", 0.00}
    };

    auto mark_to_gpa = [&](const string& mark) -> double {
        auto it = GPA_MAP.find(mark);
        return (it == GPA_MAP.end()) ? 0.0 : it->second;
    };

    int n;
    if (!(cin >> n)) return 0;
    vector<Student> students;
    students.reserve(n);

    for (int _ = 0; _ < n; ++_) {
        string lastname, firstname;
        int k;
        cin >> lastname >> firstname >> k;

        int total_credits = 0;
        double weighted_sum = 0.0;
        for (int i = 0; i < k; ++i) {
            string mark;
            int credit;
            cin >> mark >> credit;
            double gpa = mark_to_gpa(mark);
            weighted_sum += gpa * credit;
            total_credits += credit;
        }
        double overall_gpa = (total_credits > 0) ? (weighted_sum / total_credits) : 0.0;
        students.push_back({lastname, firstname, overall_gpa});
    }

    auto key = [](const Student& s) -> Key {
        return make_tuple(s.gpa, s.last, s.first);
    };

    students = mergesort_vec(students, key);

    cout.setf(ios::fixed); cout << setprecision(3);
    for (const auto& s : students) {
        cout << s.last << ' ' << s.first << ' ' << s.gpa << "\n";
    }
    return 0;
}
