class List(list):
    # Constructor
    def __init__(self, input_list: list):
        super(List, self).__init__(input_list)

    # getter:
    def __getitem__(self, *args):
        try:  # if not regular list
            current = super().__getitem__(args[0][0])
            for i in args[0][1:]:
                current = current[i]
            return current
        except:  # if regular use original getter:
            current = super().__getitem__(args[0])
            for i in args[1:]:
                current = current[i]
            return current

    def __setitem__(self, *args):
        val = args[-1]
        try:  # if not regular list
            current = super().__getitem__(args[0][0])
            for i in args[0][1:-1]:
                current = current[i]
            current[args[0][-1]] = val  # getting to one dimensional list and using regular [] operator :)
            return
        except:  # if regular use original setter:
            super().__setitem__(args[0], val)
            return



