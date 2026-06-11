import numpy as np
def find_hotspots(array):
    center = array[1:-1, 1:-1]
    top_left     = array[:-2, :-2]
    top          = array[:-2, 1:-1]
    top_right    = array[:-2, 2:]

    left         = array[1:-1, :-2]
    right        = array[1:-1, 2:]

    bottom_left  = array[2:, :-2]
    bottom       = array[2:, 1:-1]
    bottom_right = array[2:, 2:]
    mask = (
    (center > top) &
    (center > bottom) &
    (center > left) &
    (center > right) &
    (center > top_left) &
    (center > top_right) &
    (center > bottom_left) &
    (center > bottom_right))
    row,col=np.where(mask)
    row+=1
    col+=1
    hotspots = [(int(r), int(c)) for r, c in zip(row, col)]
    return hotspots
def main():
     array = np.array([
        [1, 2, 3, 2, 1],
        [2, 9, 4, 5, 2],
        [1, 3, 8, 2, 1],
        [0, 2, 1, 7, 3],
        [1, 1, 0, 2, 1]
    ])
     print("available hotspots are",find_hotspots(array))
     
main()