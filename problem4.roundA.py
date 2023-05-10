def get_nth_letter(n):
    length = 0
    rep = 1
    while length + 26 * rep < n:
        length += 26 * rep
        rep += 1

    position_in_repetition = (n - length - 1) // rep

    letter_index = position_in_repetition % 26
    return chr(ord('A') + letter_index)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        result = get_nth_letter(n)
        print("Case #{}: {}".format(i+1, result))