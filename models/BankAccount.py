class BankAccount:
    def __init__(self):
        self.username = 'username'
        self.password = 'password'
        self.balance = 100

    def sign_in(self):
        username = input('Kasutajanimi: ')
        password = input('Parool: ')
        #print(username, password)
        if username == self.username and password == self.password:
            #print('Kasutaja tuvastatud')
            self.show_menu()
        else:
            print('Vale kasutajanimi või parool.')


    def show_menu(self):
        print('Menüü:')
        print('1 - Lisa raha')
        print('2 - Võta raha välja')
        print('3 - Vaata pangakonto seisu')
        print('4 - Välju')
        user_input = int(input('Sisesta number [1, 2, 3 või 4]: '))
        #print(user_input)
        if user_input == 1:
            self.deposit()
        elif user_input == 2:
            self.withdraw()
        elif user_input == 3:
            self.check_balance()
        elif user_input == 4:
            exit()
        else:
            print('Vale number, vajadusel sisesta uue number.')
            self.show_menu()

    def deposit(self):
        amount = float(input('Kui palju raha soovite sisse panna [number]: '))
        #print(amount)
        if amount >0:
            self.balance += amount
            print(f'Sisestati {amount} eurot, arvel on nüüd {self.balance} eurot.')
            self.show_menu()
        else:
            print('Sisestatud summa on väiksem kui 0, raha ei sisestatud.')
            self.show_menu()

    def withdraw(self):
        amount = float(input('Kui palju raha soovite välja võtta [number]: '))
        #print(amount)
        if amount < 0:
            print('Sisestatud summa on väiksem kui 0, raha välja ei võetud.')
            self.show_menu()
        elif amount > self.balance:
            print(f'Sisestud summa on suurem kui arvel olev jääk. Arvel on {self.balance} eurot.')
            self.show_menu()
        else:
            self.balance -= amount
            print(f'Võeti välja {amount} eurot, arvel on nüüd {self.balance} eurot.')
            self.show_menu()

    def check_balance(self):
        print(f'Arvel on {self.balance} eurot.')
        self.show_menu()







