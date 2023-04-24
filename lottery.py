import random

class lottery:
    def __init__(self):

        self.list_Awards = ["Solstol",
                           "Roccat Musmatta",           # 1
                           "Sten",                      # 2
                           "Isak IPhone",               # 3
                           "Båt",                       # 4
                           "Vatten",                    # 5
                           "Samsung Note 7",            # 6
                           "Glasögon",                  # 7
                           "Macbook",                   # 8
                           "Äpple",                     # 9
                           "Elspis",                    # 10
                           "Internet",                  # 11
                           "Isak My Beloved Halsband",  # 12
                           "Djungel Boken på DVD",      # 13
                           "påse Zoo",                  # 14
                           "Isaks glasögon",            # 15
                           "Banan",                     # 16
                           "Lök",                       # 17
                           "Skål",                      # 18
                           "Pirates of the Caribbean",  # 19
                           "4 Ton Sten",                # 20
                           "tom CD skiva",              # 21
                           "halv äten semla"]           # 22
        
    def getAward(self):
        return self.list_Awards[random.randint(0,22)]