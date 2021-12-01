class Map:
    def __init__(self,file):
        self.w = 0
        self.h = 0
        self.map_array = []
        symbols = {'.': 0, '#': 1}

        with open(file,'r') as f:
            for line in f:
                line = line.strip()
                self.map_array.append([symbols.get(c) for c in line])

        self.w = len(self.map_array[0])
        self.h = len(self.map_array)
                
    def map(self):
        return self.map_array
