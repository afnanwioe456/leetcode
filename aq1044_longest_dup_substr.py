class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        # bana | n a
        # bana anb a | na
        # 暴力: 向右扫描, 检查所有后缀之前是否有重复, O(n^3)
        n = len(s)

        def check_dup(l, r):
            for i in range(l):
                if s[i: i+r-l] == s[l: r]:
                    return True
            return False
        
        left = 0
        right = 0
        flag = False
        for i in range(n):
            for j in range(0, i + 1):
                if i - j < right - left:
                    break
                if check_dup(j, i + 1):
                    left = j
                    right = i
                    flag = True

        if not flag:
            return ''
        return s[left: right + 1]

    def longestDupSubstring(self, s):
        # 如果有两个后缀的前缀是一致的, 那我们就找到了一个匹配
        # banana suffix_1: anana  suffix_2: ana
        # Trie?
        # 更高效: 将所有的后缀排序, 寻找相邻后缀的最长公共前缀LCP O(n^2)
        # 如何高效判断LCP?
        def LCP(s1, s2):
            n = min(len(s1), len(s2))
            i = 0
            while i < n:
                if s1[i] != s2[i]:
                    break
                i += 1
            return s1[:i]
        
        sa = sorted(range(len(s)), key=lambda x: s[x:])  # 后缀数组
        subStr = ''
        for i in range(len(sa) - 1):
            lcpStr = LCP(s[sa[i]:], s[sa[i+1]:])
            if len(lcpStr) > len(subStr):
                subStr = lcpStr
        return subStr

    # def longestDupSubstring(self, s):
    #     # 使用Rabin-Karp指纹算法+二分查找长度
    
if __name__ == '__main__':
    s = Solution()
    string = ''
    assert s.longestDupSubstring(string) == ''
    string = 'a'
    assert s.longestDupSubstring(string) == ''
    string = 'aa'
    assert s.longestDupSubstring(string) == 'a'
    string = 'aba'
    assert s.longestDupSubstring(string) == 'a'
    string = 'banana'
    assert s.longestDupSubstring(string) == 'ana'
    string = 'banancana'
    assert s.longestDupSubstring(string) == 'ana'
    string = 'bananac'
    assert s.longestDupSubstring(string) == 'ana'
        