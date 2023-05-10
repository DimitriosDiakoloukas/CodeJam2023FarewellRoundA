def remove_duplicates(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

def assign_integers(colors):
    assigned_ints = {}
    assigned_colors = []
    for color in colors:
        if color in assigned_ints:
            assigned_colors.append(color)
        else:
            assigned_ints[color] = len(assigned_ints) + 1
            assigned_colors.append(color)
    for i in range(1, len(assigned_colors)):
        if assigned_ints[assigned_colors[i-1]] > assigned_ints[assigned_colors[i]]:
            return 'IMPOSSIBLE'
    color_order = [(assigned_ints[color], color) for color in assigned_colors]
    color_order.sort()
    return ' '.join(remove_duplicates([str(color) for (_, color) in color_order]))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        colors = list(map(int, input().strip().split()))
        result = assign_integers(colors)
        print("Case #{}: {}".format(i+1, result))
