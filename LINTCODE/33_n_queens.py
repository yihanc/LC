class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        def _dfs(candidate):
            dep = len(candidate)
            if dep > n: return
                
            if dep == n:
                res.append(candidate)
                return
            
            for j in xrange(n):
                if _isValidCell(candidate, j):
                    line = "." * j + "Q" + "." * (n - j - 1)
                    _dfs(candidate + [line])

            
        def _isValidCell(candidate, j):
            dep = len(candidate)
            
            for i in xrange(dep):
                if candidate[i][j] == "Q": return False
                diff = dep - i
                if j + diff < n and candidate[dep-diff][j+diff] == "Q":
                    return False
                if j - diff >= 0 and candidate[dep-diff][j-diff] == "Q":
                    return False
            return True                        
                    
                    
        if n <= 0 or n == 2 or n == 3: return []
        if n == 1: return [["Q"]]
        
        res = []
        _dfs([])
        return res

