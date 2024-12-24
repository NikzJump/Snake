def cycle(field, snake_len):
    result_dirs = []
    for y in range(field[0] * field[1]):
        for i in range(field[0] - 1):
            result_dirs.append(0)
        for i in range(field[1] - 1):
            result_dirs.append(1)

        result_dirs.append(2)

        for i in range(field[1] - 2):
            result_dirs.append(3)

        for k in range(int(field[0] / 2) - 1):
            result_dirs.append(2)

            for i in range(field[1] - 2):
                result_dirs.append(1)

            result_dirs.append(2)

            for i in range(field[1] - 2):
                result_dirs.append(3)

        result_dirs.append(3)

    return result_dirs
