def refine_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    for i, range in enumerate(ranges):
        for other in ranges[i+1:]:
            if range[1] >= other[0]: # and range[0] <= other[1]:
                range[1] = max(range[1], other[1])
                ranges.remove(other)
    return ranges

def count_fresh_ids(ranges, available_ids):
    fresh_count = 0
    for id in available_ids:
        for range in ranges:
            if range[0] <= id <= range[1]:
                print(f"ID {id} is fresh in range {range}")
                fresh_count += 1
                break
    return fresh_count

def range_count(range):
    return range[1] - range[0] + 1

def total_fresh_count(ranges):
    total = 0
    for range in ranges:
        total += range_count(range)
    return total

if __name__ == '__main__':
    with open('input.txt', 'r') as f:     
        data = f.read()
    data_sections = data.split('\n\n')
    fresh_ranges = [list(map(int, line.split('-'))) for line in data_sections[0].split('\n')]
    available_ids = list(map(int, data_sections[1].split('\n')))

    fresh_ranges = refine_ranges(fresh_ranges)
    print(count_fresh_ids(fresh_ranges, available_ids))
    print(total_fresh_count(fresh_ranges))