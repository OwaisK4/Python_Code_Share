#include <iostream>
using namespace std;

int main() {
    string s;
    cout << "Enter a name: ";
    cin >> s;
    if (s[0] >= 'a' && s[0] <= 'z') {
        s[0] -= 32;
    }
    cout << s << "\n";
}