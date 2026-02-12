class SpellModel:
    def __init__(self, IDspell, name, level, school, classes, actionType, concentration, ritual, range, components, duration, description, cantripUpgrade):
        self.IDspell =IDspell
        self.name = name
        self.level = level
        self.school = school
        self.classes = classes
        self.actionType = actionType
        self.concentration = concentration
        self.ritual = ritual
        self.range = range
        self.components = components
        self.duration = duration
        self.description = description
        self.cantripUpgrade = cantripUpgrade

    def parseSpellData(self):
        return {
            'IDSpell': self.IDspell,
            'name': self.name,
            'level': self.level,
            'school': self.school,
            'classes': self.classes,
            'actionType': self.actionType,
            'concentration': self.concentration,
            'ritual': self.ritual,
            'range': self.range,
            'components': self.components,
            'duration': self.duration,
            'description': self.description,
            'cantripUpgrade': self.cantripUpgrade
        }