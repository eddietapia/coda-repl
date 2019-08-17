""""
Author: Eddie Tapia
File name: main
Purpose: Will create a Read-Eval-Print-loop )REPL that
is accessible via the command line
"""
import copy


class Table:
    def __init__(self):
        self.states = [{}]  # Stack to keep the states of the dictionaries
        self.state_index = 0

    def set(self, key, val):
        # TODO: Perform input checks
        self.states[self.state_index][key] = val

    def get(self, key):
        if key in self.states[self.state_index]:
            print(key, '=', self.states[self.state_index][key])
        else:
            print(key, 'not set')

    def delete(self, key):
        try:
            del self.states[self.state_index][key]
        except KeyError:
            print(key, "not set")

    def count(self, val):
        counter = 0
        for value in self.states[self.state_index].values():
            if value == val:
                counter += 1
        print(counter)

    def begin(self):
        table_copy = copy.deepcopy(self.states[self.state_index])
        self.states.append(table_copy)
        self.state_index += 1

    def commit(self):
        if self.state_index > 0:
            # Push the changes to our previous state
            self.states[self.state_index - 1] = self.states[self.state_index]
            # Pop the table and adjust our index to the previous state
            self.states.pop()
            self.state_index -= 1
        else:
            print("NO TRANSACTION")

    def rollback(self):
        if self.state_index > 0:
            self.state_index -= 1
            self.states.pop()
        else:
            print("NO TRANSACTION")


def main():
    print("Beginning command line REPL")
    table = Table()
    command = input()
    while command != "END":
        # Process the inputs
        inputs = command.split(" ")
        size = len(inputs)
        if size == 3:
            if command.startswith("SET"):
                table.set(inputs[1], inputs[2])
        elif size == 2:
            if command.startswith("GET"):
                table.get(inputs[1])
            elif command.startswith("DELETE"):
                table.delete(inputs[1])
            elif command.startswith("COUNT"):
                table.count(inputs[1])
        elif size == 1:
            if command.startswith("BEGIN"):
                table.begin()
            elif command.startswith("COMMIT"):
                table.commit()
            elif command.startswith("ROLLBACK"):
                table.rollback()
        else:
            print("Command not recognized. Please try again :)")
        command = input()
        
        
if __name__ == '__main__':
    main()
