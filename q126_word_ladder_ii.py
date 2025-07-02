from collections import defaultdict, deque

class Solution:
    def findLadders(self, begin_word: str, end_word: str, word_list: list[str]) -> list[list[str]]:
        word_list.append(begin_word)
        m = len(begin_word)
        map = defaultdict(list)
        for word in word_list:
            for i in range(m):
                mask = word[:i] + "*" + word[i + 1:]
                map[mask].append(word)
        
        prev = defaultdict(list)
        dist = {begin_word: 1}
        q = deque()
        q.append(begin_word)
        flag = False
        while not flag and q:
            for _ in range(len(q)):
                word = q.popleft()
                cur = dist[word]
                if word == end_word:
                    flag = True
                for i in range(m):
                    mask = word[:i] + "*" + word[i + 1:]
                    for nei in map[mask]:
                        if nei not in dist:
                            dist[nei] = cur + 1
                            q.append(nei)
                            prev[nei].append(word)
                        elif dist[nei] == cur + 1:  # 如果还存在其他前驱
                            prev[nei].append(word)
        
        res = []
        def path(cur):
            word = cur[-1]
            if word == begin_word:
                res.append(cur[::-1])
                return
            for p in prev[word]:
                path(cur + [p])

        path([end_word])
        return res

if __name__ == '__main__':
    sol = Solution()
    words = ["hit","hot","dot","dog","lot","cog","log"]
    print(sol.findLadders("hit", "cog", words))