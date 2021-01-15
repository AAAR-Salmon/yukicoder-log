#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		if (i % 3 == 0) {
			cout << "Fizz";
		}
		if (i % 5 == 0) {
			cout << "Buzz";
		}
		if (i % 3 != 0 && i % 5 != 0) {
			cout << i;
		}
		cout << "\n";
	}
	return 0;
}
