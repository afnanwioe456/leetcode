class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        # 从原先的无向图构建状态转移有向图,
        # 每个状态是(老鼠的位置, 猫的位置, 谁的回合) = 结局
        # 其中有猫或老鼠赢的状态, 反向逐个标记父状态
        # 对于理智的猫/老鼠:
        #   如果有子状态老鼠赢且轮到老鼠走, 那么这个状态也是老鼠赢, 猫亦然;
        #   如果有子状态老鼠赢且轮到猫走:
        #       如果猫还有别的未解析的选择, 忽略这个状态(不会主动让老鼠赢)
        #       如果猫没有别的选择, 那么这个状态也是老鼠赢
        # 如果根状态没有被确定那么就是平局
        n = len(graph)
        states = [[[0] * n] * n] * 2

        # 从每个状态[i, i, 0/1]反向标记
        for i in range(n):
            self.markState(states, graph, i, 0)
            self.markState(states, graph, i, 1)

        return states[1][2][0]

    def markState(self, states, graph, i, t):
        queue = [(i, i, t)]
        while len(queue) > 0:
            m, c, t = queue.pop(0)
            for p in self.getParents(graph, m, c, t):
                if t:
                    p_state = states[p][c][0]
                else:
                    p_state = states[m][p][1]
                if p_state:  # 如果已经标记
                    continue
        # TODO
    
    def getParents(self, graph, m, c, t):
        if t:  # 这一步轮到猫走了
            return graph[m]
        return graph[c]

    def getChildren(self, graph, m, c, t):
        if t:
            return graph[c]
        return graph[m]
        