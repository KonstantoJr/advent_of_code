"""Day 20 part 1"""


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

    def init_inputs(self, flipflops):
        for flipflop in flipflops:
            if self.name in flipflop.send:
                self.inputs[flipflop.name] = 'low'

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
            elif line.startswith("&"):
                line = line.replace("&", "")
                line = line.replace("-", "")
                name, outputs = line.split(">")
                name = name.strip()
                outputs = list(
                    map(lambda x: x.strip(), outputs.strip().split(',')))
                conjunctions.append(Conjunction(name, {}, outputs))

    return broadcaster, flipflops, conjunctions


def current_state(flipflops, conjunctions):
    flips = tuple((f, flipflops[f].state) for f in flipflops)
    conj = tuple((c, tuple((name, conjunctions[c].inputs[name]) for name in conjunctions[c].inputs))
                 for c in conjunctions)

    return conj, flips


def press_button(broadcaster: list[str], flipflops: dict[str, FlipFlop], conjunctions: dict[str, Conjunction]):
    queue = [[('broadcaster', receiver, 'low') for receiver in broadcaster]]
    high = 0
    low = 1 + len(broadcaster)
    while queue:
        pulse = queue.pop(0)
        new_pulse = []
        for sender, receiver, signal in pulse:
            if receiver in flipflops:
                s = flipflops[receiver].receive_signal(signal)
                if s == 'high':
                    for con in flipflops[receiver].send:
                        high += 1
                        new_pulse.append((receiver, con, 'high'))
                elif s == 'low':
                    for con in flipflops[receiver].send:
                        low += 1
                        new_pulse.append((receiver, con, 'low'))
            elif receiver in conjunctions:
                s = conjunctions[receiver].update_inputs(sender, signal)
                if s == 'high':
                    for con in conjunctions[receiver].output:
                        high += 1
                        new_pulse.append((receiver, con, 'high'))
                elif s == 'low':
                    for con in conjunctions[receiver].output:
                        low += 1
                        new_pulse.append((receiver, con, 'low'))
        if new_pulse:
            queue.append(new_pulse)

    return high, low


def find_loop(broadcaster, flipflops, conjunctions, presses=None):
    state = set()
    order = []
    while True:
        high, low = press_button(broadcaster, flipflops, conjunctions)
        s_f, s_c = current_state(flipflops, conjunctions)
        if (s_f, s_c, high, low) in state:
            return order
        state.add((s_f, s_c, high, low))
        order.append((s_f, s_c, high, low))
        if presses and len(state) == presses:
            print("Loop not found")
            return order


def calculate_total_pulses(order, presses):
    loops = presses // len(order)
    remainder = presses % len(order)
    high = 0
    low = 0
    for _ in range(loops):
        high += sum([h for _, _, h, _ in order])
        low += sum([l for _, _, _, l in order])
    if remainder:
        high += sum([h for _, _, h, _ in order[:remainder]])
        low += sum([l for _, _, _, l in order[:remainder]])

    return high, low


def main():
    """Main"""
    broadcaster, flipflops, conjunctions = input_parse("input.txt")

    for conjunction in conjunctions:
        conjunction.init_inputs(flipflops)

    flipflops = {
        flipflop.name: flipflop for flipflop in flipflops
    }

    conjunctions = {
        conjunction.name: conjunction for conjunction in conjunctions
    }
    presses = 1000
    order = find_loop(broadcaster, flipflops, conjunctions, presses)

    high, low = calculate_total_pulses(order, presses)

    print(f"High: {high}, Low: {low}")
    print(f"Solution: {high * low}")


if __name__ == "__main__":
    main()
