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
            (reaction_name, molecules_to_be_parsed) = line.strip().split(":")
            # print ("reaction_name", reaction_name)
            # print ("molecules_to_be_parsed", molecules_to_be_parsed)
            reactants_and_catalysts, products_string = molecules_to_be_parsed.split("->") # change for reversible reactions
            # print ("reactants_and_catalysts", reactants_and_catalysts)
            # print ("products_string", products_string)
            products_list = products_string.split("+")
            reactants_string, catalysts_string = reactants_and_catalysts.split("[")
            reactants_list = reactants_string.split("+")            
            print (catalysts_string)
            catalysts_list = catalysts_string.split("]")[0].split(",")
            self.reactions[reaction_name] = {}
            self.reactions[reaction_name]["in"] = reactants_list
            self.reactions[reaction_name]["out"] = products_list
            self.reactions[reaction_name]["cat"] = catalysts_list
            self.molecules.update(set(reactants_list))
            self.molecules.update(set(products_list))
            self.molecules.update(set(catalysts_list))
        ACS_file.close()
    # Hordijk and Steel (2004)
    def RAF(self):
        pass
    def ComputeClosure(self):
        pass



