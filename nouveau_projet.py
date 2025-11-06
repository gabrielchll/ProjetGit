class Pouliquen :

    def __init__(self, name) :
        self.name = name

    def __repr__(self) :
        return self.name + " est le plus beau"
    
pouliquen = Pouliquen("Martin")

print(pouliquen)
