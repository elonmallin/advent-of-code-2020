import os

# O(n)
def solve(n_match, numbers):
    hashmap = dict()

    for n in numbers:
        if n_match - n in hashmap and hashmap[n_match - n] + n == n_match:
            print('Answer is {} * {} = {}'.format(n, hashmap[n_match - n], n * hashmap[n_match - n]))
            break

        hashmap[n] = n


# O(n*log(n))?
def solve_part_2(n_match, numbers):
    hashmap = dict()

    for n in numbers:
        idx = n_match - n

        if idx in hashmap and not hashmap[idx]['single'] and hashmap[idx]['n_sum'] + n == n_match:
            print('Answer is {} * {} * {} = {}'.format(
                n, hashmap[idx]['n'], hashmap[idx]['n_2'], n * hashmap[idx]['n'] * hashmap[idx]['n_2']))
            break

        for key in list(hashmap.keys()):
            if hashmap[key]['single']:
                hashmap[key + n] = {
                    'single': False,
                    'n': key,
                    'n_2': n,
                    'n_sum': n + key
                }

        hashmap[n] = {
            'single': True,
            'n': n
        }


input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))
numbers = map(lambda n: int(n), input_file)


solve(2020, numbers)
solve_part_2(2020, numbers)
# solve_part_2(2020, [1721, 979, 366, 299, 675, 1456])
