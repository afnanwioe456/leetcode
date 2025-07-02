from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        n = len(wordList) + 1
        m = len(beginWord)

        def diff1(s1, s2):
            flag = False
            for i in range(m):
                if s1[i] != s2[i]:
                    if flag:
                        return False
                    flag = True
            return True
        
        adj = defaultdict(list)
        dst = -1
        for i in range(n):
            s1 = beginWord if i == 0 else wordList[i - 1]
            if s1 == endWord:
                dst = i
            for j in range(i + 1, n):
                s2 = wordList[j - 1]
                if diff1(s1, s2):
                    adj[i].append(j)
                    adj[j].append(i)
                    
        if dst < 0 or not adj[dst]:
            return 0
        
        dist = [0] * n
        q = deque()
        q.append(0)
        while q:
            node = q.popleft()
            cur = dist[node] + 1
            if node == dst:
                return cur
            for nei in adj[node]:
                if not dist[nei]:
                    dist[nei] = cur
                    q.append(nei)

        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordList.append(beginWord)
        m = len(beginWord)
        map = defaultdict(list)
        for word in wordList:
            for i in range(m):
                mask = word[:i] + "*" + word[i + 1:]
                map[mask].append(word)
        
        dist = {beginWord: 0}
        q = deque()
        q.append(beginWord)
        while q:
            word = q.popleft()
            cur = dist[word] + 1
            if word == endWord:
                return cur
            for i in range(m):
                mask = word[:i] + "*" + word[i + 1:]
                for nei in map[mask]:
                    if not nei in dist:
                        q.append(nei)
                        dist[nei] = cur
        
        return 0
        


if __name__ == '__main__':
    sol = Solution()
    words = ["hit","hot","dot","dog","lot","cog","log"]
    print(sol.ladderLength("hit", "cog", words))