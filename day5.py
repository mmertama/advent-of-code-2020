example = '''FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL'''


def find_seat(data):
    max_id = 0
    min_id = 100000
    occupied_seats = set()
    for line in data:
        row_data = line[:7]
        col_data = line[7:]
        row = 0
        for r in row_data:
            row <<= 1
            row |= 0 if r == 'F' else 1
        col = 0
        for c in col_data:
            col <<= 1
            col |= 0 if c == 'L' else 1
        seat_id = row * 8 + col
        if seat_id < min_id:
            min_id = seat_id
        if seat_id > max_id:
            max_id = seat_id
        occupied_seats.add(seat_id)
    print("max seat id:", max_id)

    for s in range(min_id, max_id + 1):
        if s not in occupied_seats:
            print(s, "missing")
