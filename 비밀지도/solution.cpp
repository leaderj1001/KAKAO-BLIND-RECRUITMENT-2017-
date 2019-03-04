#include <string>
#include <vector>

using namespace std;

int map[20][20];
int map2[20][20];
char re[20][20];

void changeMap(int n, int i, int num) {
	while (num > 1) {
		map[i][n - 1] = num % 2;
		num /= 2;
		n--;
	}
	map[i][n - 1] = num;
}

void changeMap2(int n, int i, int num) {
	while (num > 1) {
		map2[i][n - 1] = num % 2;
		num /= 2;
		n--;
	}
	map2[i][n - 1] = num;
}

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {

	for (int i = 0; i < arr1.size(); i++) {
		changeMap(n, i, arr1[i]);
	}

	for (int i = 0; i < arr2.size(); i++) {
		changeMap2(n, i, arr2[i]);
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (map[i][j] == 1 || map2[i][j] == 1)
				re[i][j] = '#';
			else if (map[i][j] == 0 && map2[i][j] == 0)
				re[i][j] = ' ';
		}
	}

	vector<string> answer;

	for (int i = 0; i < n; i++)
		answer.push_back(re[i]);

	return answer;
}