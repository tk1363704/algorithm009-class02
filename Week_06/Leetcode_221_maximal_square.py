class Solution:
    # @staticmethod
    # # Brute-force.
    # def maximalSquare(matrix) -> int:
    #     if len(matrix) == 0 or len(matrix[0]) == 0:
    #         return 0
    #     max_area = -1
    #     max_radius = -1
    #     rows, cols = len(matrix), len(matrix[0])
    #     for i in range(rows):
    #         for j in range(cols):
    #             if matrix[i][j] == "1":
    #                 # Note this!
    #                 max_radius = max(0, max_radius)
    #                 current_max_radius = min(rows - i, cols - j)
    #                 if current_max_radius <= max_radius:
    #                     continue
    #                 for k in range(1, current_max_radius):
    #                     flag = True
    #                     if matrix[i + k][j + k] != "1":
    #                         flag = False
    #                     else:
    #                         for index in range(k):
    #                             if matrix[i + k][j + index] != "1" or matrix[i + index][j + k] != "1":
    #                                 flag = False
    #                                 break
    #                     if not flag:
    #                         break
    #                     else:
    #                         max_radius = max(k, max_radius)
    #     return (max_radius + 1) * (max_radius + 1)
    #
    # # Dynamic programming.
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     if len(matrix) == 0 or len(matrix[0]) == 0:
    #         return 0
    #     max_radius = 0
    #     # First row and first column are regarded as the supplementary.
    #     dp = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix)+1)]
    #     for i in range(len(matrix)):
    #         for j in range(len(matrix[0])):
    #             if matrix[i][j] == "1":
    #                 dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
    #                 max_radius = max(max_radius, dp[i+1][j+1])
    #     return max_radius * max_radius

    # Dynamic programming: space optimization.
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        max_radius = 0
        row = len(matrix)
        col = len(matrix[0])
        # First element is regarded as the supplementary.
        dp = [0] * (col + 1)
        for i in range(row):
            northwest = 0
            for j in range(col):
                nextnorthwest = dp[j + 1]
                if matrix[i][j] == "1":
                    dp[j + 1] = min(dp[j], dp[j + 1], northwest) + 1
                    max_radius = max(max_radius, dp[j + 1])
                else:
                    dp[j + 1] = 0
                northwest = nextnorthwest
        return max_radius * max_radius

if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(Solution.maximalSquare(matrix))
    matrix = [["1"]]
    print(Solution.maximalSquare(matrix))