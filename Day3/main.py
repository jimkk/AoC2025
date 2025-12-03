
def get_highest_joltage(bank:list[int]) -> int:
    highest_value = max(bank[:-1])
    first_highest = bank.index(highest_value)
    second_value = max(bank[first_highest+1:])
    return int(str(highest_value) + str(second_value))

def get_highest_joltage_p2(bank:list[int]) -> int:
    values = []
    for i in range(11, -1, -1):
        highest_value = max(bank[:-i] if i != 0 else bank)
        # print(bank, bank[:-i], highest_value)
        values.append(highest_value)
        first_highest = bank.index(highest_value)
        bank = bank[first_highest+1:]
    return int(''.join(map(str, values)))


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = f.readlines()
    data = [[int(y) for y in x.strip()] for x in data]

    bank_sum = 0
    for bank in data:
        bank_sum += get_highest_joltage(bank)
    print('P1', bank_sum)

    bank_sum_p2 = 0
    for bank in data:
        sum = get_highest_joltage_p2(bank)
        # print(bank, sum)
        bank_sum_p2 += sum
    print('P2', bank_sum_p2)