#
# @lc app=leetcode.cn id=933 lang=python3
#
# [933] 最近的请求次数
#

# @lc code=start
class RecentCounter(object):
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

