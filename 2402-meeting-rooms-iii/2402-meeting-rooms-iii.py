class Solution:
    import heapq
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = list(range(n))  # [0, 1, 2, ..., n-1]
        heapq.heapify(available)
    
    # Min-heap of (end_time, room_number) for busy rooms
        busy = []
    
    # Count of meetings held in each room
        count = [0] * n
    
        for start, end in meetings:
            duration = end - start
        
        # Step 1: Free up rooms that have finished by 'start'
            while busy and busy[0][0] <= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)
            
            # Step 2: Assign a room
            if available:
                # Take the lowest-numbered available room
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                # Wait for the earliest room to free up
                earliest_end, room = heapq.heappop(busy)
                new_end = earliest_end + duration
                heapq.heappush(busy, (new_end, room))
            
            # Step 3: Increment count for this room
            count[room] += 1
        
        # Return room with most meetings (lowest number if tie)
        # max with key finds highest count; -i breaks ties by preferring lower room
        return max(range(n), key=lambda i: (count[i], -i))
            