def process_next_line_down(previous_line):
    next_line = []
    for pos,val in enumerate(previous_line):
        if pos == len(previous_line) - 1:
            return next_line
        else:
            next_line.append(previous_line[pos + 1] - val)


def build_triangle_and_return_new_sums(first_line, side):
    splitlist = first_line.split()
    first_line = [int(x) for x in splitlist]
    triangle = []
    triangle.append(first_line)
    while sum(first_line) != 0:
        triangle.append(process_next_line_down(first_line))
        first_line = triangle[-1]
    if side == "left":
        triangle = [x[::-1] for x in triangle]
    triangle[-1].append(0)
    for rownum in range(len(triangle)-1,-1,-1):
        if rownum == len(triangle) -1:
            triangle[-1].append(0)
        else:
            if side == "right":
                triangle[rownum].append(triangle[rownum][-1] + triangle[rownum+1][-1])
            if side == "left":
                triangle[rownum].append(triangle[rownum][-1] - triangle[rownum + 1][-1])

    return triangle[0][-1]

def return_sum_all_triangle_new_values(triangles: list,side="right") -> int:
    return sum([build_triangle_and_return_new_sums(x,side) for x in triangles])