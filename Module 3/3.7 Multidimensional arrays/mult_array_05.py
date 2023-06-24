rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

"""
The first index (0 through 2) selects one of the buildings; 
the second (0 through 14) selects the floor, the third (0 through 19) selects the room number. 
All rooms are initially free.
"""

rooms[1][9][13] = True
rooms[0][4][1] = False

vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
