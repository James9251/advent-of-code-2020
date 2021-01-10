# Open the file containing timestamp and bus timetable information
f = open('input.txt', 'r')
timestamp = int(f.readline().rstrip())
timetable = f.readline().split(',')
bus_ids = [int(x) for x in timetable if x != 'x']
earliest_bus = bus_ids[0]
shortest_wait = earliest_bus # The wait time is guaranteed to be shorter than this
for bus_id in bus_ids:
    wait_time = -timestamp % bus_id
    if wait_time < shortest_wait:
        shortest_wait = wait_time
        earliest_bus = bus_id
solution = earliest_bus * shortest_wait
print("Puzzle 1 solution = {}".format(solution))

def product(numbers):
    '''
    Recursive function that finds the product of numbers in the input list
    '''
    if len(numbers) == 1:
        return numbers[0]
    return product(numbers[1:]) * numbers[0]

# Chinese Remainder Theorem solves puzzle 2
# This is guaranteed since the bus_ids are pairwise coprime
m_prod = product(bus_ids)
x = 0
for i in range(len(timetable)):
    bus_id = timetable[i]
    if bus_id == 'x':
        continue
    m = int(bus_id) # ith modulus
    a = -i % m # the ith residue
    z = m_prod // m
    y = pow(z, m - 2, m) # m is always prime so use Fermat's little theorem
    w = (z * y) % m_prod
    x += a * w
x = x % m_prod
print("Puzzle 2 solution = {}".format(x))