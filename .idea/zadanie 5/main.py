from Smartphone import Smartphone
import pickle

if __name__ == '__main__':
    sp1 = Smartphone("Iphone", "13", 4999)
    sp2 = Smartphone("Iphone", "12 pro", 4499)
    sp3 = Smartphone("Samsung", "s22", 3999)


    with open ("phones.dat", "wb") as file:
        pickle.dump(sp1, file)
        pickle.dump(sp2, file)
        pickle.dump(sp3, file)

        file.close()

    with open ("phones.dat", "rb") as file:
        phone1 = pickle.load(file)
        phone2 = pickle.load(file)
        phone3 = pickle.load(file)

        print(phone1)
        print(phone2)
        print(phone3)

        file.close()
