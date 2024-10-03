x = input("Введите имя...\n").lower()
aleksei_list = ['alex', 'alexei', 'alekesi', 'леха лепеха']
if any(leha in x for leha in aleksei_list):
    print (f'Выйдите из команты, {x.title()}')
else:
    print (f'Здравствуйте, {x.title()}')