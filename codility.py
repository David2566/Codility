def solution(A):
    A.sort()
    rooms = 0
    i = 0
    N = len(A)
    
    while i < N:
        rooms += 1
        # The number of people allowed in the current room is A[i]
        room_size = A[i]
        # Move the index i forward by room_size, as these people will be in one room
        i += room_size
    
    return rooms

# Example test cases
print(solution([1, 1, 1, 1, 1]))  # Output: 5