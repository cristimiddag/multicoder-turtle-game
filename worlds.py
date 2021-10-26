from World import World

WORLDS = [
    World(
        obstacle_positions=[
            (0, 7), (1, 7), (2, 1), (2, 2), (3, 2), (3, 6), (4, 6),
            (4, 9), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 9),
            (5, 10), (6, 9), (7, 3), (7, 4), (7, 5), (7, 6), (7, 9),
            (8, 6), (9, 0), (9, 1), (9, 4), (9, 6), (10, 6)
        ],
        portal_position=(10, 0),
        robot_start_position=(10, 10),
        key_position=(1, 10)
    ),
    World(
        obstacle_positions=[
            (0, 9), (1, 9), (2, 1), (2, 2), (2, 3), (2, 5), (2, 6),
            (3, 8), (4, 7), (4, 8), (5, 0), (5, 1), (5, 3), (5, 5),
            (5, 6), (5, 7), (6, 3), (6, 7), (6, 8), (6, 9), (6, 10),
            (7, 4), (8, 8), (9, 0), (9, 1), (9, 2), (9, 3), (9, 6),
            (9, 7), (9, 8), (10, 8)
        ],
        portal_position=(5, 8),
        robot_start_position=(0, 10),
        key_position=(0, 2)
    ),
    World(
        obstacle_positions=[
            (0, 1), (0, 7), (1, 7), (2, 2), (2, 7), (3, 2), (3, 7),
            (4, 2), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 1),
            (5, 5), (6, 4), (6, 5), (6, 7), (6, 8), (6, 9), (6, 10),
            (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 7), (9, 7),
            (10, 0), (10, 7)
        ],
        portal_position=(3, 1),
        robot_start_position=(7, 7),
        key_position=(9, 4)
    )
]
