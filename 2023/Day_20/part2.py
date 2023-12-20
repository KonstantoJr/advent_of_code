"""Day 20 part 1"""

import math


class FlipFlop:

    def __init__(self, name, state, send):
        self.name = name
        self.state = state
        self.send = send

    def __repr__(self) -> str:
        return f"{self.name} {self.state} {self.send}"

    def receive_signal(self, signal):
        if signal == 'high':
            return

        if self.state:
            self.state = False
            return 'low'

        self.state = True
        return 'high'


class Conjunction:

    def __init__(self, name, inputs, output):
        self.name = name
        self.inputs = inputs
        self.output = output

    def __repr__(self) -> str:
        return f"{self.name} {self.output} {self.inputs}"

    def init_inputs(self, flipflops, conjunctions):
        for flipflop in flipflops:
            if self.name in flipflop.send:
                self.inputs[flipflop.name] = 'low'
        for conjunction in conjunctions:
            if self.name in conjunction.output:
                self.inputs[conjunction.name] = 'low'

    def send_pulse(self):
        if all([value == 'high' for value in self.inputs.values()]):
            return 'low'
        return 'high'

    def update_inputs(self, name, pulse):
        self.inputs[name] = pulse
        return self.send_pulse()


def input_parse(filename):
    broadcaster = ""
    flipflops = []
    conjunctions = []
    output = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("broadcast"):
                broadcaster = line.split(">")[1]
                broadcaster = list(map(lambda x: x.strip(),
                                       broadcaster.strip().split(',')))
            elif line.startswith("%"):
                line = line.replace("%", "")
                line = line.replace("-", "")
                name, send = line.split(">")
                name = name.strip()
                send = list(
                    map(lambda x: x.strip(), send.strip().split(',')))

                flipflops.append(FlipFlop(name, False, send))
                if 'rx' in send:
                    output.append(name)
            elif line.startswith("&"):
                line = line.replace("&", "")
                line = line.replace("-", "")
                name, outputs = line.split(">")
                name = name.strip()
                outputs = list(
                    map(lambda x: x.strip(), outputs.strip().split(',')))
                conjunctions.append(Conjunction(name, {}, outputs))
                if 'rx' in outputs:
                    output.append(name)

    return broadcaster, flipflops, conjunctions, output


def press_button(broadcaster: list[str], flipflops: dict[str, FlipFlop], conjunctions: dict[str, Conjunction], output: str, index: int, modules: dict[str, int]):
    queue = [[('broadcaster', receiver, 'low') for receiver in broadcaster]]
    while queue:
        pulse = queue.pop(0)
        new_pulse = []
        for sender, receiver, signal in pulse:
            if receiver in flipflops:
                s = flipflops[receiver].receive_signal(signal)
                if s:
                    for con in flipflops[receiver].send:
                        if s == 'high' and con == output:
                            if con not in modules:
                                modules[receiver] = index
                            if set(modules) == set(conjunctions[output].inputs):
                                return math.lcm(*modules.values())
                        new_pulse.append((receiver, con, s))

            elif receiver in conjunctions:
                s = conjunctions[receiver].update_inputs(sender, signal)
                if s:
                    for con in conjunctions[receiver].output:
                        if s == 'high' and con == output:
                            if con not in modules:
                                modules[receiver] = index
                            if set(modules) == set(conjunctions[output].inputs):
                                return True
                        new_pulse.append((receiver, con, s))

        if new_pulse:
            queue.append(new_pulse)

    return False


def main():
    """Main"""
    broadcaster, flipflops, conjunctions, output = input_parse("input.txt")
    output = output[0]

    for conjunction in conjunctions:
        conjunction.init_inputs(flipflops, conjunctions)

    flipflops = {
        flipflop.name: flipflop for flipflop in flipflops
    }

    conjunctions = {
        conjunction.name: conjunction for conjunction in conjunctions
    }
    print(set(conjunctions[output].inputs))
    print(output)
    index = 0
    modules = {}
    while True:
        index += 1
        if (index % 1000) == 0:
            print(modules)
        if press_button(broadcaster, flipflops, conjunctions, output, index, modules):
            break
    print(modules)
    print(math.lcm(*modules.values()))


if __name__ == "__main__":
    main()
