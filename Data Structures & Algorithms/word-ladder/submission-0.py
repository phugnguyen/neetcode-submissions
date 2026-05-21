class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # graph problem with adjency list
        # neighbors share wildcard pattern *og : [hog, log]
        # map to keep track of neighbors
        # bfs to traverse neighbors

        # in bfs we must find every wildcard pattern to find neighbors

        if endWord not in wordList:
            return 0

        neighbors = collections.defaultdict(list)

        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                neighbors[pattern].append(word)

        seen = set([beginWord])
        q = deque([beginWord])
        result = 1

        while q:
            lenq = len(q)
            for i in range(lenq):
                word = q.popleft()
                if word == endWord:
                    return result
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]
                    relatives = neighbors[pattern]
                    for item in relatives:
                        if item not in seen:
                            seen.add(item)
                            q.append(item)
            result += 1

        return 0

