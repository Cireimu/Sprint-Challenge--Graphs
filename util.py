import random


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def explore_search(player, moves, our_map):
    # bfs
    # initialize Queue and enqueue player's current room
    # initialize a visited tracker set
    # while the queue has item perform these tasks
    # initialize a path by  queue.dequeue
    # get the last visited room
    # check to see if cur_room has been visited
    # if not then add to visited and loop through all exits
    # check if an exit is "?", if so then return path
    # if not then create new_path and queue

    q = Queue()
    q.enqueue([player.current_room.id])

    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        current_room = path[-1]

        if current_room not in visited:
            visited.add(current_room)

            for exit in our_map[current_room]:

                if our_map[current_room][exit] == '?':
                    return path

                else:
                    new_path = list(path)
                    new_path.append(our_map[current_room][exit])
                    q.enqueue(new_path)
    return []


def unexplored(player, new_moves, our_map):
    # set exits, create an empty list for exits not used/tried yet for later
    # check the exits of the current_room for any unexplored areas
    # add to not_used
    # if there are no unused exits,
    # then keep moving/exploring until you find an area with unexplored exits
    # set new_room to the current player room
    # loop through each unexplored room
    # check for any unexplored exits, if there are then add them to new_moves
    exits = our_map[player.current_room.id]

    not_used = []

    for direction in exits:
        if exits[direction] == "?":
            not_used.append(direction)
    if len(not_used) == 0:
        not_explored = explore_search(player, new_moves, our_map)

        new_room = player.current_room.id
        for room in not_explored:
            for direction in our_map[new_room]:
                if our_map[new_room][direction] == room:
                    new_moves.enqueue(direction)
                    new_room = room
                    break
    else:
        new_moves.enqueue(not_used[random.randint(0, len(not_used) - 1)])
