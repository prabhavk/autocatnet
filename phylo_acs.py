class Network:
    def __init__(self,name):
        # attributes
        self.name = name # name of network
        self.reactions = {} # [R1, R2]
        self.molecules = [] # [A, B, C, D]
        self.food = [] # [True, True, False, False, False] non-food molecules will be enzymes
        self.catalysts = {} # mapping from enzymes to reactions
        # methods
    def Read_ACS(self, ACS_file_name):
        ACS_file = open(ACS_file_name, "r")
        for line in ACS_file:
            # Parse line
            # Let's say the reaction R1 is under consideration
            self.reactions["R1"] = {}
            self.reactions["R1"]["in"] = ["A"]
            self.reactions["R1"]["out"] = ["B"]
            self.reactions["R1"]["cat"] = ["D"]
        ACS_file.close()



