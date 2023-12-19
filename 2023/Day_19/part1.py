"""Day 19 part 1"""


class Parts:
    """Parts class"""

    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
        self.accepted = None
        self.total_rating = x + m + a + s

    def __repr__(self):
        return f"Parts({self.x}, {self.m}, {self.a}, {self.s})"


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
                line = line.replace("{", "")
                line = line.replace("}", "")
                line = line.replace("=", "")
                line = line.replace("x", "")
                line = line.replace("m", "")
                line = line.replace("a", "")
                line = line.replace("s", "")

                x, m, a, s = map(int, line.split(","))
                parts.append(Parts(x, m, a, s))
            else:
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


def check_parts(rules, parts):
    accepted = []
    rejected = []

    for part in parts:
        rule_name = 'in'
        while True:
            if rule_name == "A":
                part.accepted = True
                accepted.append(part)
                break
            elif rule_name == "R":
                part.accepted = False
                rejected.append(part)
                break

            for rule in rules[rule_name]:
                if rule.condition is None:
                    rule_name = rule.next_rule
                    break
                elif rule.check == '>':
                    if getattr(part, rule.value) > int(rule.condition):
                        rule_name = rule.next_rule
                        break
                elif rule.check == '<':
                    if getattr(part, rule.value) < int(rule.condition):
                        rule_name = rule.next_rule
                        break
    return accepted, rejected


def main():
    """Main"""
    rules, parts = input_parse("input.txt")

    accepted, _ = check_parts(rules, parts)

    print(sum([p.total_rating for p in accepted]))


if __name__ == "__main__":
    main()
