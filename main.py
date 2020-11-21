import time

EMPTY_TOKEN = []

class Token:
    #The token is simply a value
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "{}".format(self.value)

class Node:
    #The node contains a key (consider it uniquer identifier), a value, which is an array of tokens and a capacity (the number of tokens)
    def __init__(self, key, value, capacity):
        self.key = key
        self.value = value
        self.capacity = capacity

    
    def get_value(self):
        return self.value


    def get_capacity(self):
        return self.capacity

    
    def set_value(self, new_val):
        self.value = new_val


    def __str__(self):
        values = []
        for item in self.value:
            values.append(item)
        return "Node with key {} has value {}".format(self.key, values)


class Transition:
    def __init__(self, input_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.output_nodes = output_nodes

    
    #According to the definition of this data structure, we can only pass through a transition if all the input nodes contain at least one token 
    #Eg.: We consider three nodes a, b and c. We have a transition from a to b and c, we will need to have at least a token in a to send the data over to b and c
    # We will consider the same nodes, but we will say that the transition is from a and b to c. For this to be possible, both a and b must have tokens
    # Another thing we need to keep track of is the capacity (a node a can hold so much values inside)
    def check_validity(self):
        for node in self.input_nodes:
            if node.get_value() == EMPTY_TOKEN:
                return False

        for node in self.output_nodes:
            if node.get_capacity() < len(node.get_value()) + len(self.input_nodes):
                return False

        return True

    # This function simply executes a transition, it takes the value from the input nodes and adds it to the output nodes
    def make_transition(self):
        for inp in self.input_nodes:
            for out in self.output_nodes:
                out.value.append(inp.get_value())
            inp.set_value([])
            


class Net:
    def __init__(self, left_hand_nodes, right_hand_nodes, transition_table):
        self.left_hand_nodes = left_hand_nodes
        self.right_hand_nodes = right_hand_nodes
        self.transition_table = transition_table

    # This function tries all the transition paths, when it finds one it exists. I didn't let it continue trying so that I could send a print out intermediary results
    def _mass_transition(self):
        for transition in self.transition_table:
            if transition.check_validity():
                transition.make_transition()
                return None

    
    def _print(self):
        all_nodes = self.left_hand_nodes + self.right_hand_nodes
        for node in all_nodes:
            print(node)

    
    def _continue_running(self):
        self._mass_transition()
        self._print()
        time.sleep(1)


    # Run the simulation
    def simulate(self):
        self._print()
        for i in range(10):
            print("Running step {}".format(i))
            self._continue_running()
            



# A really simple example that I found on wikipedia that tests the main functionality of the data structure
def main():
    x = Node('x', [Token(1)], 2)
    y = Node('y', [], 2)
    z = Node('z', [], 2)
    a = Node('a', [], 2)
    t1 = Transition([x], [z, a])
    t2 = Transition([z, a], [y])
    net = Net([x, y], [z, a], [t1, t2])
    net.simulate()

main()