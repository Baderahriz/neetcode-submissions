from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colmun = defaultdict(list)
        box = defaultdict(list)
        for i, ele in enumerate(board):
            row = set()
            for j, e in enumerate(ele):
                
                if i < 3:
                    a = 1
                elif i >= 3 and i < 6:
                    a = 2
                else:
                    a = 3 

                if j < 3:
                    b = 1
                elif j >= 3 and j < 6:
                    b = 2
                else:
                    b = 3 
                
                if e != ".":
                    
                    if e in row:
                        return False
                    row.add(e)
                    if e in colmun[j]:
                        return False
                    colmun[j].append(e)

                    if e in box[(a,b)]:
                        return False
                    box[(a, b)].append(e)
        return True