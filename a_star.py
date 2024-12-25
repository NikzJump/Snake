class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def calculate_H(node1, node2):
    result = ((node1.position[0] - node2.position[0]) ** 2 + (node1.position[1] - node2.position[1]) ** 2)

    return result


def a_star(maze, start, end, obst, head):
    start_node = Node(None, start)
    start_node.g = start_node.f = start_node.h = 0
    end_node = Node(None, end)
    end_node.g = end_node.f = end_node.h = 0

    ol = []
    cl = []

    stop = 0

    directions = [(0, -1), (-1, 0), (-1, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (0, 1), (1, 0)]

    ol.append(start_node)

    while len(ol) > 0:
        stop += 1

        path_ = []
        current_node = ol[0]
        current_index = 0

        for index, item in enumerate(ol):
            if item.f < current_node.f:
                current_index = index
                current_node = item

        ol.pop(current_index)
        cl.append(current_node)

        if stop >= 100:
            return False

        print("текущая", current_node.position)
        print("конечная", end_node.position)
        print("конечная 2", end)

        if current_node == end_node:
            current = current_node

            while current is not None:
                path_.append(current.position)
                current = current.parent

            return path_[::-1]

        children = []

        for new_position in directions:
            node_position = (current_node.position[0] + new_position[0],
                             current_node.position[1] + new_position[1])

            if (node_position[0] > maze[0] - 1 or node_position[0] < 0 or
                    node_position[1] > maze[1] - 1 or node_position[1] < 0):
                continue

            if node_position in obst:
                continue

            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            for c_child in cl:
                if c_child == child:
                    continue

            child.g = current_node.g + 1
            child.h = calculate_H(child, end_node)
            child.f = child.g + child.h

            for o_node in ol:
                if child == o_node and child.g > o_node.g:
                    continue

            ol.append(child)


def convert_to_dirs(path):
    directions = []

    if not path:
        return False

    for index, item in enumerate(path):
        if index == len(path) - 1:
            return directions

        if item[0] < path[index+1][0]:
            directions.append(0)
        if item[0] > path[index+1][0]:
            directions.append(2)

        if item[1] < path[index+1][1]:
            directions.append(1)
        if item[1] > path[index+1][1]:
            directions.append(3)
