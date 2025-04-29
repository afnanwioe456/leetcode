class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        dic = dict()
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - 97] += 1
            count = tuple(count)
            index = dic.get(count)
            if index is None:
                res.append([])
                index = len(res) - 1
                dic[count] = index
            res[index].append(s)
        return res

        
if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print(s.groupAnagrams(strs))