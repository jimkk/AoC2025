from pprint import pprint

def simulate_tachyons(grid):
    previous_tachyon_positions = [grid[0].index('S')]
    split_count = 0
    for i, row in enumerate(grid):
        tachyon_positions = []
        for tachyon in previous_tachyon_positions:
            if row[tachyon] == '^':
                split_count += 1
                if tachyon - 1 >= 0:
                    tachyon_positions.append(tachyon - 1) # New left
                if tachyon + 1 < len(row):
                    tachyon_positions.append(tachyon + 1) # New right
            else:
                tachyon_positions.append(tachyon)
        previous_tachyon_positions = list(set(tachyon_positions))  # Remove duplicates
    return split_count

def simulate_tachyons_part2(grid):
    previous_tachyon_positions = [[grid[0].index('S'), 1]] 
    for _, row in enumerate(grid):
        tachyon_positions = []
        for tachyon, count in previous_tachyon_positions:
            if row[tachyon] == '^':
                if tachyon - 1 >= 0:
                    tachyon_positions.append([tachyon - 1, count])
                if tachyon + 1 < len(row):
                    tachyon_positions.append([tachyon + 1, count])
            else:
                tachyon_positions.append([tachyon, count])
        previous_tachyon_positions = tachyon_positions
        
        # Combine counts for same positions
        previous_tachyon_positions = []
        for i in set([x for x,y in tachyon_positions]):
            total_count = sum([y for x,y in tachyon_positions if x == i])
            previous_tachyon_positions.append([i, total_count])

    return sum([y for x,y in previous_tachyon_positions])

if __name__ == "__main__":
    with open('input.txt') as f:
        grid = [list(line.strip()) for line in f.readlines()]

    p1_count = simulate_tachyons(grid)
    print(f"Part 1: Total splits = {p1_count}")

    p2_count = simulate_tachyons_part2(grid)
    print(f"Part 2: Total timelines = {p2_count}")