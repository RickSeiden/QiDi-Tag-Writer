class FilamentColors:

    def __init__(self):
        self.colorName=0
        self.colorValue=1
        self.colorCode=2
        self.colors=[
            ["White", 0xFAFAFA, 1],
            ["Black", 0x060606, 2],
            ["Gray", 0xD9E3ED, 3],
            ["Bright Green", 0x5CF30F, 4],
            ["Green", 0x63E492, 5],
            ["Blue", 0x2850FF, 6],
            ["Pink", 0xFE98FE, 7],
            ["Dark Yello", 0xDFD628, 8],
            ["Dark Green", 0x228332, 9],
            ["Light Blue", 0x99DEFF, 10],
            ["Dark Blue", 0x1714B0, 11],
            ["Lavendar", 0xCEC0FE, 12],
            ["Pea Green", 0xCADE4B, 13],
            ["Med Dark Blue", 0x1353AB, 14],
            ["Med Light Blue", 0x5EA9FD, 15],
            ["Purple", 0xA878FF, 16],
            ["Salmon", 0xFE717A, 17],
            ["Bright Orange", 0xFF362D, 18],
            ["Darker Gray", 0xE2DFCD, 19],
            ["Dark Gray", 0x898F9B, 20],
            ["Sand", 0x6E3812, 21],
            ["Khaki", 0xCAC59F, 22],
            ["Dark Orange", 0xF28636, 23],
            ["Light Brown", 0xB87F2B, 24]
        ]
        self.length=len(self.colors)

    def getByNumber(self,number):
        for color in self.colors:
            if (color[2]==number):
                return color
        return
