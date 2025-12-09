import random as rd
# Random sayılarla doğrulama yapmak için sayılar üretiyoruz.
RANDOM_NUMBER_ONE = rd.randint(2,100)
RANDOM_NUMBER_TWO = rd.randint(2,100)
PERSON_NUMBER_ONE = rd.randint(2,100)
PERSON_NUMBER_TWO = rd.randint(2,100)
print(f"random numbers; {RANDOM_NUMBER_ONE}, {RANDOM_NUMBER_TWO}\n------\nperson_1; {PERSON_NUMBER_ONE}\nPerson_2; {PERSON_NUMBER_TWO}\n-----")


# Parent class'ımız.
class Diffie_Hellman:
    # x mod y
    def __init__(self, x, y):
        self.X = x
        self.Y = y

#Birinci kişi
class PersonA(Diffie_Hellman):
    def __init__(self, x, y, number):
        super().__init__(x, y)
        self.number = number
    
    #Kullanıcının private keyi(random belirlendi) ile public bir şifre yayınlıyoruz
    def calculate_public_key(self):
        public_key = (self.X ** self.number) % self.Y
        return public_key
    
    #İletişim kurduğumuz kişiden gelen public şifreyi private anahtarımız ile açıyoruz ve mesajı okuyoruz
    def de_crypt(self, hash):
        self.hash = hash
        password = (self.hash ** self.number) % self.Y
        return password
#İkinci kişi
class PersonB(Diffie_Hellman):
    def __init__(self, x, y, number):
        super().__init__(x, y)
        self.number = number
    
    #Kullanıcının private keyi(random belirlendi) ile public bir şifre yayınlıyoruz
    def calculate_public_key(self):
        public_key = (self.X ** self.number) % self.Y
        return public_key

    #İletişim kurduğumuz kişiden gelen public şifreyi private anahtarımız ile açıyoruz ve mesajı okuyoruz
    def de_crypt(self, hash):
        self.hash = hash
        password = (self.hash ** self.number) % self.Y
        return password


"""
    Oluşturulan kişisel sayılar ve public keyler ile haberleştirilen kişilerin verilerini okuyoruz

"""
ahmet = PersonA(RANDOM_NUMBER_ONE,RANDOM_NUMBER_TWO,PERSON_NUMBER_ONE)
beyza = PersonB(RANDOM_NUMBER_ONE,RANDOM_NUMBER_TWO,PERSON_NUMBER_TWO)

ahmet_key = ahmet.calculate_public_key()
beyza_key = beyza.calculate_public_key()

print(f"Ahmet public key; {ahmet_key}")
print(f"Beyza public key; {beyza_key}")

print(f"Ahmet; {ahmet.de_crypt(beyza_key)}")
print(f"beyza; {beyza.de_crypt(ahmet_key)}")