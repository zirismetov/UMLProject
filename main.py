class ArtistInfo:
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.__name


class SampleClips:
    def __init__(self, length):
        self.__length = length

    def getName(self):
        return self.__length

class Reviews:
    def __init__(self, author):
        self.__author = author

    def getName(self):
        return self.__author

class MarketingMaterial:
    def __init__(self, type, description, email, content, artistinfo , sampleclip ,reviews,  ):
        self.__type = type
        self.__description = description
        self.__email = email
        self.__content = content
        self.__artist = artistinfo
        self.__sample = sampleclip
        self.__reviews = reviews
        print(vendor.__class__)


class Vendor:
    def __init__(self, name, street, city, state, zipcode, contact, phone):
        self.__name = name
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        self.__contact = contact
        self.__phone = phone

class Product:
    def __init__(self, number, description):
        self.__number = number
        self.__description = description

class CD(Vendor):
    def __init__(self, sku, title, category, salestatus):
        self.__sku = sku
        self.__title = title
        self.__category = category
        self.__salestatus = salestatus


class Inventory:
    def __init__(self , store, inventory):
        self.__store = store
        self.__inventory = inventory
    def getStoreid(self):
        return self.__store

    def showAllinventory(getStoreid):
        pass




class Customer:
    def __init__(self, email, lname, fname, address, city ,state, zipcode, phone):
        self.__email = email
        self.__lname = lname
        self.__fname = fname
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        self.__phone = phone

@Inventory.showAllinventory
class InStoreHold:
    def __init__(self, date):
        self.__date = date

artist = ArtistInfo('Alesha')
sample = SampleClips(12)
reviews = Reviews(5)
vendor = Vendor("Joha,", "dada", 'dasdada', 123131, 2222, 'Mr', 22222331)
cd = CD('Jazz', 'Bob Marly', 'adad', 'Excellent');
mark = MarketingMaterial(0, 0, 0,0,artist, sample, reviews)