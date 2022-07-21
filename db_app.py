import db_funcs

for x in range(int(input('ile rekordow chcesz dodac? '))):
    print('Wprowadzanie rekordu nr {}: '.format(x+1))
    db_funcs.add_one(input('podaj imie: '), input('podaj nazwisko: '), input('podaj email: '))

for x in range(int(input('ile rekordow chcesz usunac? '))):
    print('Usuwanie rekordu nr {} '.format(x+1))
    db_funcs.delete_one(input('podaj rowid do usuniecia: '))

db_funcs.show_all()

if input('Czy chcesz uzyc funkcji podladu wlasciciela adresu email? [Y/N] ').upper()=='Y':
    try: 
        db_funcs.email_lookup(input('podaj adres email: '))
    except:
        print('Brak adresu email w bazie.')

print('KONIEC PROGRAMU DB')