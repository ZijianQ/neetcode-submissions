class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        if n == 0:
            return 0

        # 1. 先算出每辆车到达终点的时间，并和它的起始位置绑定在一起
        cars = []  # 每个元素形如 (position_i, time_i)
        for i in range(n):
            t = (target - position[i]) / speed[i]
            cars.append((position[i], t))

        # 2. 按位置从小到大排序（越靠右的车越接近终点）
        cars.sort(key=lambda x: x[0])

        # 3. 从最右边（离终点最近的车）开始往左扫
        fleets = 0
        max_time = 0.0  # 当前“最慢车队”的到达时间

        # 从右往左遍历
        for pos, t in reversed(cars):
            if t > max_time:
                # 说明这辆车追不上前面的任何车队，成为一个新的车队
                fleets += 1
                max_time = t
            # 如果 t <= max_time，说明它会在终点前追上前面的某个车队，
            # 所以不需要增加 fleets

        return fleets

        

        
            

        