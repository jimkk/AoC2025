
def remove_item_by_index(lst, index):
    del lst[index]
    return lst

def find_accessible_papers(grid):
    accessible_locations = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '@':
                continue
            grid[i][j] = '#'
            neighbours = [x[max(j-1,0):min(j+2,len(grid[i]))] for x in grid[max(i-1,0):min(i+2, len(grid))]]
            if sum(x.count('@') for x in neighbours) < 4:
                accessible_locations.append((i,j))
            grid[i][j] = '@'
    return accessible_locations

def find_accessible_papers_p2(grid):
    paper_taken = 0
    found_one = True
    while found_one:
        found_one = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '@':
                    continue
                grid[i][j] = '#'
                neighbours = [x[max(j-1,0):min(j+2,len(grid[i]))] for x in grid[max(i-1,0):min(i+2, len(grid))]]
                if sum(x.count('@') for x in neighbours) < 4:
                    grid[i][j] = '.'
                    paper_taken += 1
                    found_one = True
                else:
                    grid[i][j] = '@'
    return paper_taken

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = [list(x.strip()) for x in f.readlines()]

    accessible_locations = find_accessible_papers(data)
    print("Total accessible papers:", len(accessible_locations))

    total_papers_taken = find_accessible_papers_p2(data)
    print("Total papers that can be taken:", total_papers_taken)