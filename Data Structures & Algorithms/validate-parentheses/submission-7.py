class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2 or len(s) % 2:
            return False
        valid = {"(": ")", "[": "]", "{": "}"}
        helper = []
        flag = True
        for c in s:
            if c in valid.keys():
                helper.append(valid[c])
            else:
                
                flag = False
                if not helper:
                   
                    return False
                
                value = helper.pop()
                
                # print(value)
                if c != value:
                    
                    return False
        if flag or helper:
            return False
        return True


