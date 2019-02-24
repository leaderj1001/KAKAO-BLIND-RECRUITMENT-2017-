#include <string>
#include <vector>
#include <stack>
using namespace std;

int idx[] = { 1, 0, 1 };
int idy[] = { 0, 1, 1 };
char map[31][31];
int visited[31][31];

void printMatrix(int m, int n) {
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			printf("%d ", visited[i][j]);
		}
		printf("\n");
	}
}

int solution(int m, int n, vector<string> board) {
	int answer = 0;
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			map[i][j] = board[i][j];
		}
	}
	while (1) {
		int flag = 0;
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				visited[i][j] = 0;
			}
		}

		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if ((map[i][j] == map[i][j + 1]) && (map[i][j] == map[i + 1][j]) && (map[i][j] == map[i + 1][j + 1]) && map[i][j] != '.') {
					visited[i][j] = 1;
					visited[i + 1][j] = 1;
					visited[i][j + 1] = 1;
					visited[i + 1][j + 1] = 1;
					flag = 1;
				}
			}
		}

		if (!flag)
			break;

		stack<char> s;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (!visited[j][i]) {
					s.push(map[j][i]);
				}
				else
					answer += 1;
				map[j][i] = '.';
			}

			int size = s.size();
			for (int j = m - 1; j > m - size - 1; j--) {
				map[j][i] = s.top();
				s.pop();
			}
		}

	}


	return answer;
}

int main() {

	vector<string> board;

	board.push_back("CCBDE");
	board.push_back("AAADE");
	board.push_back("AAABF");
	board.push_back("CCBBF");

	printf("%d\n", solution(4, 5, board));
}