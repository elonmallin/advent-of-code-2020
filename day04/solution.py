import os
import re
import functools

# input_file = open(os.path.join(os.path.dirname(__file__), './test_input.txt'))
# input_file = open(os.path.join(os.path.dirname(__file__), './valid_part_2.txt'))
input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))
lines = list(map(lambda l: l.replace('\n', ' ').strip(), re.split('\n\n', input_file.read()))) # normalized to one liners


def kvp_reduce_to_hashmap(acc, kvp):
    acc[kvp[0]] = kvp[1]

    return acc


def is_valid(line):
    line_list = re.split('\s', line)
    kvp_list = list(map(lambda l: re.split(':', l), line_list))
    hashmap = functools.reduce(kvp_reduce_to_hashmap, kvp_list, {})
    
    # 'cid' in hashmap
    return 'byr' in hashmap and 'iyr' in hashmap and 'eyr' in hashmap and 'hgt' in hashmap and 'hcl' in hashmap and 'ecl' in hashmap and 'pid' in hashmap


def validate_hgt(value):
    value = value.strip()
    m = re.findall('(\d+)(in|cm)', value)
    if m:
        height, unit = m[0]
    else:
        return False

    if unit == 'cm':
        return int(height) in range(150, 193+1)
    if unit == 'in':
        return int(height) in range(59, 76+1)
    
    return False


def is_valid_part_2(line):
    line_list = re.split('\s', line)
    kvp_list = list(map(lambda l: re.split(':', l), line_list))
    hashmap = functools.reduce(kvp_reduce_to_hashmap, kvp_list, {})
    
    # 'cid' in hashmap
    if 'byr' in hashmap and 'iyr' in hashmap and 'eyr' in hashmap and 'hgt' in hashmap and 'hcl' in hashmap and 'ecl' in hashmap and 'pid' in hashmap:
        if (int(hashmap['byr'].strip()) in range(1920, 2002+1) and
            int(hashmap['iyr'].strip()) in range(2010, 2020+1) and
            int(hashmap['eyr'].strip()) in range(2020, 2030+1) and
            validate_hgt(hashmap['hgt']) and
            re.match('^#([0-9|a-f]{6})$', hashmap['hcl']) and
            hashmap['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and
            re.match('^([0-9]{9})$', hashmap['pid'])):
            return True

    return False


def solve(lines, valid_check):
    valid_count = 0

    for line in lines:
        if valid_check(line):
            valid_count += 1

    return valid_count


# ~35 min
print('Solution 1:', solve(lines, is_valid))
# ~35 min
print('Solution 2:', solve(lines, is_valid_part_2))

#
# Solution 3 - less data transformations
#
def switch_valid(key, value):
    switcher = {
        'byr': lambda v: int(v) in range(1920, 2002+1),
        'iyr': lambda v: int(v) in range(2010, 2020+1),
        'eyr': lambda v: int(v) in range(2020, 2030+1),
        'hgt': validate_hgt,
        'hcl': lambda v: re.match('^#([0-9|a-f]{6})$', v),
        'ecl': lambda v: v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda v: re.match('^([0-9]{9})$', v),
        'invalid': lambda v: False,
    }

    return switcher.get(key, 'invalid')(value)


def solve_3(lines, part_2):
    count = 0
    props = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for l in lines:
        found = True

        for w in props:
            if not w + ':' in l:
                found = False
                break

        if found and part_2:
            kvps = [(k, re.findall(k+':([\w|#]+)', l)[0].strip()) for k in props]
            for k, v in kvps:
                if not switch_valid(k, v):
                    found = False
                    break

        if found:
            count += 1

    return count


print('Solution 3 - Part 1:', solve_3(lines, False))
print('Solution 3 - Part 2:', solve_3(lines, True))

