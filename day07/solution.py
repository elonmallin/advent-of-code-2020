import os
import re

# input_file = open(os.path.join(os.path.dirname(__file__), './test_input_2.txt'))
input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))

all_text = input_file.read().strip('\n')
lines = list(map(lambda l: l.replace('bags contain no other bags.', ''), all_text.split('\n')))


class part_1:
    @staticmethod
    def solve(lines):
        hashmap = {}

        for l in lines:
            main = re.findall('^(\w+ \w+)', l)[0]
            children = re.findall('\d+ (\w+ \w+)', l)

            if main not in hashmap:
                hashmap[main] = part_1.make_node([], [], False)

            hashmap[main]['is_gold'] = True if re.search('shiny gold', l) else False

            for c in children:
                if c not in hashmap:
                    hashmap[c] = part_1.make_node([hashmap[main]], [], False)

                hashmap[main]['children'].append(hashmap[c])
        
        count = 0

        for k, v in hashmap.items():
            if k != 'shiny gold' and (v['is_gold'] or part_1.has_child_gold(v['children'])):
                count += 1

        return count

    
    @staticmethod
    def make_node(parents, children, gold):
        return {
            'parents': parents,
            'children': children,
            'is_gold': True if gold else False
        }


    @staticmethod
    def has_child_gold(children):
        for c in children:
            if c['is_gold']:
                return True
            elif part_1.has_child_gold(c['children']):
                return True
            
        return False


class part_2:
    @staticmethod
    def solve(lines):
        hashmap = {}

        for l in lines:
            main = re.findall('^(\w+ \w+)', l)[0]
            children = re.findall('(\d+) (\w+ \w+)', l)

            hashmap[main] = children

        return part_2.count_bags_in_bags(hashmap, 'shiny gold')


    @staticmethod
    def count_bags_in_bags(hashmap, key):
        count = 0

        for bag in hashmap[key]:
            (n, key_next) = (int(bag[0]), bag[1])
            inner_count = part_2.count_bags_in_bags(hashmap, key_next)

            count += n + (n * inner_count)

        return count


print('Solve part 1:', part_1.solve(lines))
print('Solve part 2:', part_2.solve(lines))
