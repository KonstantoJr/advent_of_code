"""Day 19 part 1"""


class Rule:
    """Rule class"""

    def __init__(self, condition=None, next_rule=None):
        self.condition = condition
        if condition is not None:
            if '>' in condition:
                value, condition = condition.split('>')
                self.value = value
                self.condition = condition
                self.check = '>'
            elif '<' in condition:
                value, condition = condition.split('<')
                self.value = value
                self.condition = condition
                self.check = '<'

        self.next_rule = next_rule

    def __repr__(self):
        return f"Rule({self.condition}, {self.next_rule})"


def input_parse(filename):
    """Read the input file and return a list of lines"""
    rules = {}
    parts = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            if line.startswith("{"):
                continue
            line = line.replace("}", "")
            name, rule = line.split("{")
            rule = rule.split(",")
            for i, r in enumerate(rule):
                if ':' in r:
                    condition, next_rule = r.split(":")
                    rule[i] = Rule(condition=condition,
                                   next_rule=next_rule)
                else:
                    rule[i] = Rule(next_rule=r)
            rules[name] = rule
    return rules, parts


def check(rule, x, m, a, s):
    ranges = {
        'x': x,
        'm': m,
        'a': a,
        's': s
    }

    if rule.check == '>':
        if ranges[rule.value][0] < int(rule.condition) < ranges[rule.value][1]:
            return [(int(rule.condition)+1, ranges[rule.value][1]), (ranges[rule.value][0], int(rule.condition))]
        if ranges[rule.value][0] > int(rule.condition):
            return [(ranges[rule.value][0], ranges[rule.value][1])]
        if ranges[rule.value][1] < int(rule.condition):
            return False
    elif rule.check == '<':
        if ranges[rule.value][0] < int(rule.condition) < ranges[rule.value][1]:
            return [(ranges[rule.value][0], int(rule.condition)-1), (int(rule.condition), ranges[rule.value][1])]
        if ranges[rule.value][0] > int(rule.condition):
            return False
        if ranges[rule.value][1] < int(rule.condition):
            return [(ranges[rule.value][0], ranges[rule.value][1])]


def solution(rules):
    """Solution"""
    queue = [('in', [1, 4000], [1, 4000], [1, 4000], [1, 4000])]
    accepted = []
    while queue:
        state, x, m, a, s = queue.pop(0)
        if state == "A":
            accepted.append((x, m, a, s))
            continue
        if state == "R":
            continue
        rule = rules[state]
        for r in rule:
            if r.condition is None:
                if r.next_rule == 'A':
                    accepted.append((x, m, a, s))
                    break
                if r.next_rule == 'R':
                    break
                queue.append((r.next_rule, x, m, a, s))
            else:
                result = check(r, x, m, a, s)
                if not result:
                    continue
                if len(result) == 1:
                    if r.value == 'x':
                        x = result[0]
                    elif r.value == 'm':
                        m = result[0]
                    elif r.value == 'a':
                        a = result[0]
                    elif r.value == 's':
                        s = result[0]

                    queue.append((r.next_rule, x, m, a, s))
                elif len(result) == 2:
                    if r.value == 'x':
                        x = result[0]
                        queue.append((r.next_rule, x, m, a, s))
                        x = result[1]
                    elif r.value == 'm':
                        m = result[0]
                        queue.append((r.next_rule, x, m, a, s))
                        m = result[1]
                    elif r.value == 'a':
                        a = result[0]
                        queue.append((r.next_rule, x, m, a, s))
                        a = result[1]
                    elif r.value == 's':
                        s = result[0]
                        queue.append((r.next_rule, x, m, a, s))
                        s = result[1]
    return accepted


def main():
    """Main"""
    rules, _ = input_parse("input.txt")
    accepted = solution(rules)
    total = 0

    for x, m, a, s in accepted:
        total += (x[1] - x[0] + 1) * (m[1] - m[0] + 1) * \
            (a[1] - a[0] + 1) * (s[1] - s[0] + 1)
    print(total)


if __name__ == "__main__":
    main()
