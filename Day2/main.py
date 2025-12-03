def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def invalid_ids(start, end):
    invalid_ids = []
    for i in range(start, end + 1):
        s = str(i)

        halves = [s[:len(s)//2], s[len(s)//2:]]
        if halves[0] == halves[1]:
            # print(f"Invalid ID found: {i}")
            invalid_ids.append(i)
    return invalid_ids
    
def invalid_ids_p2(start, end):
    invalid_ids = []
    for i in range(start, end + 1):
        s = str(i)
        length = len(s)
        for divisor in [i for i in range(2, length + 1) if length % i == 0]:
            s_chunks = list(chunks(s, length // divisor))
            if all(chunk == s_chunks[0] for chunk in s_chunks):
                # print(f"Invalid ID found: {i}")
                invalid_ids.append(i)
                break
    return invalid_ids

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = f.readline().split(',')
    

    sum_of_invalids = 0
    for r in data:
        start, end = map(int, r.split('-'))
        ret = invalid_ids(start, end)
        # print(f"Total invalid IDs between {start} and {end}: {len(ret)}")
        sum_of_invalids += sum(ret)
    print(f"P1 - Sum of all invalid IDs: {sum_of_invalids}")

    sum_of_invalids = 0
    for r in data:
        start, end = map(int, r.split('-'))
        ret = invalid_ids_p2(start, end)
        # print(f"Total invalid IDs between {start} and {end}: {len(ret)}")
        sum_of_invalids += sum(ret)
    print(f"P2 - Sum of all invalid IDs: {sum_of_invalids}")