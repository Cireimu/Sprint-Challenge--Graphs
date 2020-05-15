from room import Room
from player import Player
from world import World
from util import Queue, explore_search, unexplored

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

our_map = {}
new_moves = Queue()

unexplored_room = {}
# loop through exits in the current room
# add all "?" exits to unexplored_room
for direction in player.current_room.get_exits():
    unexplored_room[direction] = "?"
# starting room is supposed to be an unxplored_room
our_map[world.starting_room.id] = unexplored_room

# call unexplored
unexplored(player, new_moves, our_map)

reverse_dir = {"n": "s", "s": "n", "e": "w", "w": "e"}

# run until new_moves is empty
# set the starting room to cur_room
# get the direction from new_moves
# move that direction
# add that move to the traversal path
# set the player's next room to a variable
# set the our_map dict entry for the move to next room
while new_moves.size() > 0:
    cur_room = player.current_room.id
    move = new_moves.dequeue()

    player.travel(move)
    traversal_path.append(move)
    next_room = player.current_room.id

    our_map[cur_room][move] = next_room

    # if it's not in the map
    # then loop for each exit found in the cur_room
    # and set unexplored exits to "?"
    if next_room not in our_map:
        our_map[next_room] = {}

        for exit in player.current_room.get_exits():
            our_map[next_room][exit] = "?"

    # set the reversed direction to the map, setting it to the cur_room
    # check to see if new_moves has anything left, if so then run unexplored once again
    our_map[next_room][reverse_dir[move]] = cur_room

    if new_moves.size() == 0:
        unexplored(player, new_moves, our_map)

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
