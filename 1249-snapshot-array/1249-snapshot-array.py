class SnapshotArray:
    def __init__(self, length: int):

        self.array = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0
    
    def set(self, index: int, val: int) -> None:
        if self.array[index][-1][0] == self.snap_id:
            self.array[index][-1][1] = val
        else:
            self.array[index].append([self.snap_id, val])
    
    def snap(self) -> int:
        current_snap = self.snap_id
        self.snap_id += 1  
        return current_snap
    
    def get(self, index: int, snap_id: int) -> int:
        history = self.array[index]
        left, right = 0, len(history) - 1
        
        while left < right:
            mid = (left + right + 1) // 2  
            if history[mid][0] <= snap_id:
                left = mid 
            else:
                right = mid - 1
        
        return history[left][1]