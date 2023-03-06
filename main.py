import csv
from datetime import datetime


class WrongChoiseException(Exception):
    # Raises when user enters invalid choice
    pass


class Pizza():
    def __init__(self):
        pass

    def get_description(self):
        print("Pizza, bir İtalyan yemek çeşididir ve çok yaygındır.")

    def get_cost(self):
        pass


class Klasik(Pizza):
    def __init__(self):
        self.name = "Klasik Pizza"
        self.price = 10

    def get_cost(self):
        return self.price

    def get_description(self):
        print(
            "Klasik pizza düz hamur, peynir, mantar, sucuk, sosis ve sostan oluşmaktadır.")


class Margarita(Pizza):
    def __init__(self):
        self.name = "Margarita Pizza"
        self.price = 20

    def get_cost(self):
        return self.price

    def get_description(self):
        print("Margarita pizza domates, mozarella, fesleğen, zeytinyağı ve tuzla yapılan Napoli pizzasıdır.")


class Turk(Pizza):
    def __init__(self):
        self.name = "Türk Pizza"
        self.price = 30

    def get_cost(self):
        return self.price

    def get_description(self):
        print("Batılılar için Turkish Pizza yani Türk Pizzası olarak bilinen lahmacun,"
              "ince çıtır hamurun üzerine konan baharatlı ve kıymalı karışımdan meydana gelir.")


class Sade(Pizza):
    def __init__(self):
        self.name = "Sade Pizza"
        self.price = 40

    def get_cost(self):
        return self.price

    def get_description(self):
        print("Sade pizza düz hamur, sos ve peynirden oluşmaktadır.")


class Decorators():
    def __init__(self):
        pass

    def get_description(self):

        return "Eklenen sos "


class Zeytin(Decorators):
    def __init__(self):
        self.name = "Zeytin"
        self.price = 5
        super().__init__()

    def get_cost(self):
        return self.price

    def get_description(self):
        return super().get_description() + "Zeytin !!"


class Mantarlar(Decorators):
    def __init__(self):
        self.name = "Mantarlar"
        self.price = 10
        super().__init__()

    def get_cost(self):
        return self.price

    def get_description(self):
        return super().get_description() + "Mantarlar !!"


class KeciPeyniri(Decorators):
    def __init__(self):
        self.name = "Keçi Peyniri"
        self.price = 15
        super().__init__()

    def get_cost(self):
        return self.price

    def get_description(self):
        return super().get_description() + "Keçi Peyniri !!"


class Et(Decorators):
    def __init__(self):
        self.name = "Et"
        self.price = 20
        super().__init__()

    def get_cost(self):
        return self.price

    def get_description(self):
        return super().get_description() + "Et !!"


class Sogan(Decorators):
    def __init__(self):
        self.name = "Soğan"
        self.price = 25
        super().__init__()

    def get_cost(self):
        return self.price

    def get_description(self):
        return super().get_description() + "Soğan !!"


class Misir(Decorators):
    def __init__(self):
        self.name = "Mısır"
        self.price = 30
        super().__init__()

    def get_cost(self):
        return self.price

    def get_description(self):
        return super().get_description() + "Mısır !!"


def main():

    while True:

        try:
            pizza_choise = int(input("Lütfen bir Pizza Seçiniz :\n \
                1: Klasik \
                2: Margarita \
                3: TürkPizza  \
                4: Sade Pizza\n"))

            if not 0 < pizza_choise < 5:
                raise WrongChoiseException

            sauce_choise = int(input("ve seçeceğiniz sos :\n \
                11: Zeytin \
                12: Mantarlar \
                13: Keçi Peyniri \
                14: Et \
                15: Soğan \
                16: Mısır\n"))

            if not 10 < sauce_choise < 17:
                raise WrongChoiseException
            break
        except WrongChoiseException:
            print("Yanlış bir seçim yaptınız. Lütfen tekrar deneyin !\n")

    pizza_dict = {1: Klasik, 2: Margarita, 3: Turk, 4: Sade}

    pizza = pizza_dict[pizza_choise]()

    sauce_dict = {11: Zeytin,
                  12: Mantarlar,
                  13: KeciPeyniri,
                  14: Et,
                  15: Sogan,
                  16: Misir}

    sauce = sauce_dict[sauce_choise]()

    pizza.get_description()
    print(sauce.get_description())

    header = ["Name", "ID", "Credit Card",
              "Order Description", "Order Time", "Password"]

    with open('orders_db.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        # print(f"Sipariş Tutarınız :{int(pizza.get_cost() + sauce.get_cost())}")
        name = input("Devam etmek için kullanıcı adı giriniz : ")
        id = input("TC Kimlik Numarası giriniz : ")
        credit_card = input("Kredi Kartı Numarasını giriniz : ")
        passwd = input("Şifresini giriniz : ")
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        row = [name, id, credit_card, pizza.name+" "+sauce.name+" " +
               str(pizza.get_cost()+sauce.get_cost())+"TRY", dt_string, passwd]
        writer.writerow(row)


if __name__ == '__main__':
    main()
