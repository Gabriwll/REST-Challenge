from flask_restful import Resource, reqparse
from bisect import bisect_left #used in Tools class

from spells import SpellModel

spells = [
    {
        'IDSpell': '00',
        'name': 'Acid Splash',
		'level': 0,
		'school': 'evocation',
		'classes': ['sorcerer', 'wizard'],
		'actionType': 'action',
		'concentration': False,
		'ritual': False,
		'range': '60 feet',
		'components': ['v', 's'],
		'duration': 'Instantaneous',
		'description': 'You create an acidic bubble at a point within range, where it explodes in a 5-foot-radius Sphere. Each creature in that Sphere must succeed on a Dexterity saving throw or take 1d6 Acid damage.',
        'cantripUpgrade': 'The damage increases by 1d6 when you reach levels 5 (2d6), 11 (3d6), and 17 (4d6).'
    }
]

class Tools:


    def searchItem(list, target):
        for item in list:
            if item == target:
                return item
        return None
    
    def searchItemByID(list, target): #não testado
        sorted(list, list.IDspell)
        item = bisect_left(list, target)

        if item != len(list) and list[item] == target:
            return item
        return None

class Spell(Resource):
    def get(self):
        return {'Magias': spells}

class Spells(Resource):
    listArgs = reqparse.RequestParser()

    #FIXME: implementar um método que pesquisa os atributos da magia dinamicamente a fim de tornar genérico a inserção na lista
    listArgs.add_argument('name')
    listArgs.add_argument('level')
    listArgs.add_argument('school')
    listArgs.add_argument('classes')
    listArgs.add_argument('actionType')
    listArgs.add_argument('concentration')
    listArgs.add_argument('ritual')
    listArgs.add_argument('range')
    listArgs.add_argument('components')
    listArgs.add_argument('duration')
    listArgs.add_argument('duration')
    listArgs.add_argument('description')
    listArgs.add_argument('cantripUpgrade')

    def get(self, IDspell):
        item = Tools.searchItemByID(spells, IDspell)

        return item if item != None else {'message': 'Not found'}, 404

    def post(self, IDspell):

        #TODO: Usar método de inserção para garantir que a lista esteja sempre ordenada

        pass

    def put(self, IDspell):
        #TODO: Usar método de inserção para garantir que a lista esteja sempre ordenada

        data = Spells.listArgs.parse_args()
        
        newSpell = SpellModel(IDspell, **data)
        newSpell = newSpell.parseHotelData()

        spell = Tools.searchItemByID(IDspell)
        if spell:
            Tools.update(newSpell)
            return newSpell, 200 # Ok

        spells.append(newSpell) #TODO: Usar métood mencionado anteriormente
        return newSpell, 201 # created

    def delete(self, IDspell):
        spell = Tools.searchItem(spells, IDspell)

        if spell:
            spells.remove(spell)
            return {'message': 'Spell deleted'}, 200

        return {'message': 'Not found'}, 404