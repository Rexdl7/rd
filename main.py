class mobile:
    
    def __init__(self, ram: int, storage: int, name: str):
        self.ram = ram
        self.storage = storage
        self.name = name
        
    def get_info(self):
        print(f'Model name: {self.name}, RAM: {self.ram}, ROM: {self.storage}\n')
 
# Here i am stating all my phones

OnePlus: mobile = mobile(12, 256, "OnePlus 9 Pro")
OnePlus_2: mobile = mobile(8, 128, "OnePlus 9 Pro")
Vivo: mobile = mobile(6, 64, "Vivo V9 Pro")
samsung: mobile = mobile(4, 32, "Samsung J7 Max")
# Some print statememts...

print(f'1.\nOnePlus 9 Pro\'s ram is {OnePlus.ram} GB and its storage is {OnePlus.storage}GB !\n')
print(f'2.\nMy Second OnePlus 9 Pro\'s ram is {OnePlus_2.ram}GB and its storage is {OnePlus_2.storage}GB !\n')
print(f'3.\nVivo V9 Pro\'s ram is {Vivo.ram}GB and its storage is {Vivo.storage}GB!\n')
print(f"4.\n{samsung.name}\'s ram is {samsung.ram}GB and its storage is {samsung.storage}GB ! ")
print("\n")

# Calling Info for all the mobiles respectively
Vivo.get_info()
OnePlus.get_info()
OnePlus_2.get_info()
samsung.get_info()
