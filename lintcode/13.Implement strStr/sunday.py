class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if source == "":
            if target == "":
                return 0
            else:
                return -1

        # preprocess
        pre = {}
        for i in range(len(target)):
            if target[i] not in pre:
                pre[target[i]] = i
        
        t_i=0
        s_i=0

        start=0
        # match
        while(s_i < len(source) and t_i < len(target)):
            if t_i == len(target):
                return start
            
            s = source[s_i]
            t = target[t_i]

            if s == t:
                t_i+=1
                s_i+=1
            else:
                # skip
                if s_i + len(target) > len(source):
                    # not enough char
                    return -1
                else:
                    last = source[s_i + len(target) - 1]

                    if last == target[len(target) - 1]:   
                        t_i=0
                    else:
                        if last in pre:
                            s_i= s_i + len(target) - 1 - pre[last]
                            t_i= 0
                        else:
                            s_i+= len(target)
                            t_i=0 

                    start=s_i

        if t_i == len(target):
            return start
        else:
            return -1

s = Solution()

assert s.strStr("src", "sb") == -1
assert s.strStr("src", "c") == 2
assert s.strStr("tartarget", "target") == 3

assert s.strStr("abcdabcdefg", "bcd") == 1