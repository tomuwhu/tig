#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

int main() {
	std::string str1;
	std::string str2;
	std::cin >> str1 >> str2;
	/*
	 * dp[i][j] is the minimum number of moves to change the first i letters
	 * of the string into the first j letters of result.
	 */
	vector<vector<int>> dp(str1.size() + 1,
	                       vector<int>(str2.size() + 1, INT32_MAX));
	dp[0][0] = 0;
	for (int i = 0; i <= str1.size(); i++) {
		for (int j = 0; j <= str2.size(); j++) {
			if (i != 0) {
				// Delete letter i - 1 from the string.
				dp[i][j] = std::min(dp[i][j], dp[i - 1][j] + 1);
			}
			if (j != 0) {
				// Add letter j - 1 of the result to the string.
				dp[i][j] = std::min(dp[i][j], dp[i][j - 1] + 1);
			}

			// Make letter i - 1 equal to letter j - 1 of the result.
			if (i != 0 && j != 0) {
				int new_cost = dp[i - 1][j - 1] + (str1[i - 1] != str2[j - 1]);
				dp[i][j] = std::min(dp[i][j], new_cost);
			}
		}
	}
	cout << dp[str1.size()][str2.size()] << endl;
}