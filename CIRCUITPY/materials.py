class Materials:

    def __init__(self):
        self.materialName=0
        self.materialCode=1
        self.materials=[
            ["PLA Rapido", 1],
            ["PLA Basic", 7],
            ["PLA Matte", 2],
            ["PLA Metal", 3],
            ["PLA Silk", 4],
            ["PETG Basic", 39],
            ["PETG Tough", 40],
            ["PETG Rapido", 41],
            ["PETG Translucent", 45],
            ["ABS", 11],
            ["TPU", 50],
            ["TPU-Aero", 49],
            ["PLA-CF", 5],
            ["PLA-Wood", 6],
            ["PLA Matte Basic", 8],
            ["PET-CF", 37],
            ["PET-GF", 38],
            ["PETG-CF", 42],
            ["PETG-GF", 43],
            ["ABS-GF", 12],
            ["ABS-Metal", 13],
            ["ABS-Odorless", 14],
            ["ASA", 18],
            ["ASA-AERO", 19],
            ["UltraPA", 24],
            ["PA-CF", 25],
            ["UltraPA-CF25", 26],
            ["PA12-CF", 27],
            ["PAHT-CF", 30],
            ["PAHT-GF", 31],
            ["Support for PAHT", 32],
            ["Support for PET/PA", 33],
            ["PC/ABS-FR", 34],
            ["PPS-CF", 44],
            ["PVA", 47]
        ]
        self.length=len(self.materials)

    def getByNumber(self, number):
        for material in self.materials:
            if (material[1] == number):
                return material[0]
        return

    def getByPlace(self, place):
        return self.materials[place]

    def getByMaterial(self, filament):
        for material in self.materials:
            if (material[0] == filament):
                return material
        return


