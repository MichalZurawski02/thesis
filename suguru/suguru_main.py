from suguru_ortools import suguru_solver_ortools
from suguru_ilog import suguru_solver_ilog
import time


def main():
#     grid4x4 = [
#     {(1, 1), (1, 2, 2), (2, 2)},
#     {(2, 1), (3, 1), (4, 1, 3), (4, 2)},
#     {(1, 3), (1, 4), (2, 3), (2, 4)},
#     {(3, 2), (3, 3), (3, 4, 2), (4, 3, 4), (4, 4, 1)}
# ]
    
#     suguru = suguru_solver_ortools(4, 4, grid4x4)
#     suguru.solve()

#     suguru = suguru_solver_ilog(4, 4, grid4x4)
#     suguru.solve()



#     grid6x6 = [
#     {(1, 1, 3), (1, 2), (2, 1), (2, 2), (2, 3)},
#     {(1, 3), (1, 4), (2, 4), (2, 5), (3, 5)},
#     {(1, 5), (1, 6, 1), (2, 6, 3), (3, 6), (4, 6)},
#     {(3, 1), (3, 2), (4, 2), (4, 3), (5, 3)},
#     {(3, 3), (3, 4), (4, 4), (4, 5, 5), (5, 5)},
#     {(5, 6)},
#     {(4, 1), (5, 1), (5, 2), (6, 1, 2), (6, 2)},
#     {(6, 3), (6, 4, 2), (5, 4), (6, 5, 4), (6, 6)}
# ]
    
#     suguru = suguru_solver_ortools(6, 6, grid6x6)
#     suguru.solve()

#     suguru = suguru_solver_ilog(6, 6, grid6x6)
#     suguru.solve()



#     grid8x8 = [
#     {(1, 1), (1, 2, 1), (1, 3), (2, 1)},
#     {(1, 4), (1, 5), (2, 4), (3, 4), (4, 4)},
#     {(1, 6), (1, 7), (2, 5), (2, 6, 3), (3, 5, 5)},
#     {(1, 8, 3), (2, 7, 5), (2, 8), (3, 7), (3, 8)},
#     {(3, 1, 2), (4, 1), (2, 2), (3, 2), (2, 3)},
#     {(3, 3)},
#     {(5, 1, 5), (6, 1), (4, 2), (5, 2), (4, 3)},
#     {(6, 2), (7, 2), (5, 3), (6, 3), (5, 4)},
#     {(6, 4), (6, 5), (5, 5), (7, 5)},
#     {(4, 5), (4, 6), (3, 6)},
#     {(4, 7), (4, 8), (5, 6), (6, 6, 4), (5, 7)},
#     {(7, 6), (7, 7, 1), (6, 7), (6, 8), (5, 8)},
#     {(8, 5), (8, 6), (8, 7), (8, 8), (7, 8, 4)},
#     {(7, 3), (7, 4)},
#     {(7, 1, 5), (8, 1), (8, 2), (8, 3), (8, 4)},
# ]
    
#     suguru = suguru_solver_ortools(8, 8, grid8x8)
#     suguru.solve()

#     suguru = suguru_solver_ilog(8, 8, grid8x8)
#     suguru.solve()



#     grid8x10 = [
#     {(1, 1, 1), (1, 2), (2, 1), (2, 2, 2), (3, 1, 4)},
#     {(1, 3), (1, 4, 1), (1, 5), (2, 3), (2, 4)},
#     {(1, 6), (1, 7), (2, 5), (2, 6), (3, 5)},
#     {(1, 8), (2, 7), (2, 8, 3), (3, 6), (3, 7)},
#     {(1, 9), (2, 9), (3, 9, 4), (4, 8), (4, 9)},
#     {(3, 8)},
#     {(5, 8)},
#     {(5, 9), (6, 8, 3), (6, 9), (7, 8), (7, 9, 5)},
#     {(4, 6), (4, 7), (5, 6), (5, 7, 5), (6, 7)},
#     {(5, 5, 4), (6, 5), (6, 6), (7, 4), (7, 5, 2)},
#     {(5, 2), (5, 3, 5), (6, 3), (6, 4), (7, 3)},
#     {(3, 3, 4), (3, 4), (4, 4, 1), (4, 5), (5, 4)},
#     {(3, 2), (4, 1), (4, 2), (4, 3), (5, 1, 4)},
#     {(6, 1), (6, 2), (7, 1), (7, 2)},
#     {(7, 6), (7, 7)}
# ]
    
#     suguru = suguru_solver_ortools(8, 10, grid8x10)
#     suguru.solve()

#     suguru = suguru_solver_ilog(8, 10, grid8x10)
#     suguru.solve()



#     grid10x15 = [
#     {(1,1), (1,2,6), (1,3), (2,2), (2,3,1), (3,2)},
#     {(1,4), (2,4), (2,5,6), (3,5), (4,4), (4,5)},
#     {(1,5), (1,6), (2,6,5), (3,6), (4,6), (4,7)},
#     {(1,7), (1,8), (1,9,3), (1,10), (2,8)},
#     {(1,11), (2,11), (2,12,2), (3,12), (4,12,4), (4,11)},
#     {(1,12), (1,13), (1,14,1), (1,15), (2,15,2), (3,15)},
#     {(2,1), (3,1), (4,1), (5,1,6), (6,1), (7,1)},
#     {(4,2,2), (5,2), (6,2,5), (3,3,4), (4,3), (3,4)},
#     {(2,7), (3,7), (3,8), (4,8), (5,8,3), (5,7)},
#     {(2,9,4), (2,10), (3,9,1), (3,10), (3,11), (4,10,2)},
#     {(2,13), (2,14), (3,13), (4,13), (5,13), (5,14)},
#     {(3,14), (4,14), (4,15), (5,15,2), (6,15,5), (6,14)},
#     {(6,13), (7,13,6), (7,14,2), (7,15), (8,14), (8,15)}, 
#     {(10,12), (10,13), (10,14), (10,15), (9,14,1), (9,15,5)},
#     {(7,12), (8,12), (8,13), (9,13)},
#     {(9,9), (10,9), (10,10), (10,11,1), (9,11,4), (9,12)},
#     {(10,8)},
#     {(8,8,5), (9,8), (8,9), (8,10), (9,10)},
#     {(8,1,4), (9,1), (10,1,2), (10,2,3), (10,3), (10,4,1)},
#     {(7,2), (7,3), (8,2), (9,2), (9,3)},
#     {(5,3), (6,3), (6,4), (7,4), (8,3), (8,4)},
#     {(7,5), (8,5), (9,4,4), (9,5,3), (9,6), (10,5)},
#     {(7,6), (8,6), (8,7), (9,7,6), (10,6,2), (10,7)},
#     {(5,4), (5,5), (5,6,1), (6,5), (6,6), (6,7)},
#     {(6,8,2), (6,9), (7,7), (7,8)},
#     {(4,9), (5,9), (5,10,1), (6,10,6), (7,9), (7,10)},
#     {(5,11), (5,12), (6,11), (6,12), (7,11,5), (8,11)}
# ]
    
#     suguru = suguru_solver_ortools(10, 15, grid10x15)
#     suguru.solve()

#     suguru = suguru_solver_ilog(10, 15, grid10x15)
#     suguru.solve()

    grid20x20 = [{(9, 12), (8, 12), (9, 10), (9, 11), (10, 12), (8, 11)}, {(12, 9), (12, 10)}, {(5, 10), (5, 11)}, {(12, 3), (11, 2), (10, 2), (11, 1), (10, 1), (12, 2), (11, 3), (12, 1)}, {(1, 2), (3, 1), (6, 2), (7, 1), (3, 2), (4, 1), (2, 1), (4, 2), (5, 1), (2, 2), (1, 1), (5, 2), (6, 1)}, {(7, 8), (8, 9), (8, 8), (8, 10), (7, 9)}, {(6, 8), (5, 9), (3, 8), (6, 9), (4, 8), (2, 8), (5, 7), (5, 8), (6, 7), (4, 9), (1, 8)}, {(3, 7), (1, 7), (3, 6), (1, 6), (4, 7), (5, 6), (4, 6), (6, 6), (2, 7), (2, 6)}, {(1, 10), (1, 11), (2, 10), (1, 12), (2, 11), (1, 9), (2, 12), (2, 9)}, {(12, 7), (12, 6), (11, 5), (12, 4), (12, 8), (12, 5), (11, 7), (11, 6), (10, 6)}, {(6, 10), (7, 10), (6, 11), (7, 11)}, {(8, 1), (8, 3), (7, 2), (6, 3), (7, 3), (8, 2)}, {(12, 12), (11, 10), (10, 10), (11, 11), (10, 11), (12, 11), (11, 12), (11, 9)}, {(5, 12), (4, 12)}, {(9, 6), (8, 7), (8, 6), (7, 7), (10, 7), (7, 6), (9, 7)}, {(3, 11), (4, 10), (4, 11), (3, 12), (3, 9), (3, 10)}, {(6, 12), (7, 12)}, {(4, 5), (2, 5), (1, 3), (1, 4), (6, 4), (5, 5), (3, 3), (3, 4), (1, 5), (6, 5), (4, 3), (2, 3), (4, 4), (3, 5), (2, 4), (5, 3), (5, 4)}, {(10, 5), (8, 4), (9, 2), (9, 3), (11, 4), (9, 4), (8, 5), (7, 4), (9, 5), (10, 3), (10, 4), (7, 5), (9, 1)}, {(10, 9), (9, 9), (11, 8), (10, 8), (9, 8)}]
    suguru = suguru_solver_ortools(20, 20, grid20x20)
    suguru.solve()

    start_time = time.time()
    suguru = suguru_solver_ilog(20, 20, grid20x20)
    suguru.solve()
    end_time = time.time()
    print(f"IBM ILOG: {end_time - start_time:.6f} seconds")

    # grid30x30 = [{(6, 2), (7, 2), (6, 1), (7, 1)}, {(6, 10), (7, 10), (5, 11), (6, 11), (7, 11), (8, 12), (6, 12), (7, 12), (8, 11)}, {(8, 1), (10, 2), (9, 2), (9, 1), (8, 2)}, {(9, 6), (8, 7), (8, 6), (9, 7)}, {(7, 4), (6, 5), (7, 5), (9, 5), (8, 5), (6, 6), (7, 6)}, {(1, 2), (3, 1), (1, 3), (1, 4), (3, 2), (2, 1), (1, 5), (2, 2), (2, 3), (2, 4), (1, 1)}, {(4, 5), (6, 3), (6, 4), (5, 5), (3, 3), (4, 1), (3, 4), (4, 2), (5, 1), (4, 3), (4, 4), (5, 2), (5, 3), (5, 4)}, {(4, 11), (1, 12), (3, 12), (5, 12), (4, 12), (2, 12)}, {(4, 8), (2, 8), (3, 8), (1, 8)}, {(2, 5), (1, 7), (3, 7), (3, 6), (1, 6), (4, 7), (4, 6), (2, 7), (3, 5), (2, 6)}, {(11, 4), (10, 4), (12, 6), (11, 5), (12, 4), (10, 5), (12, 5), (11, 3), (11, 6)}, {(12, 12), (11, 10), (11, 11), (12, 10), (10, 11), (9, 11), (12, 11), (10, 12), (11, 12), (9, 12)}, {(2, 9), (2, 11), (3, 10), (1, 9), (4, 10), (1, 11), (2, 10), (3, 9), (5, 10), (3, 11), (4, 9), (1, 10)}, {(9, 9), (8, 9), (9, 10), (8, 8), (8, 10), (6, 9), (7, 9)}, {(7, 3)}, {(10, 9), (11, 8), (9, 8), (10, 6), (12, 9), (10, 7), (11, 9), (10, 8), (10, 10), (12, 7), (12, 8), (11, 7)}, {(6, 8), (7, 8), (6, 7), (7, 7)}, {(12, 3), (11, 2), (11, 1), (10, 1), (12, 2), (12, 1)}, {(9, 3), (8, 3), (9, 4), (8, 4), (10, 3)}, {(5, 7), (5, 6), (5, 9), (5, 8)}]

    # suguru = suguru_solver_ortools(30, 30, grid30x30)
    # suguru.solve()

    # start_time = time.time()
    # suguru = suguru_solver_ilog(30, 30, grid30x30)
    # suguru.solve()
    # end_time = time.time()
    # print(f"IBM ILOG: {end_time - start_time:.6f} seconds")



    # suguru = suguru_solver_ortools(50, 50, grid50x50)
    # suguru.solve()

    # start_time = time.time()
    # suguru = suguru_solver_ilog(50, 50, grid50x50)
    # suguru.solve()
    # end_time = time.time()
    # print(f"IBM ILOG: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()