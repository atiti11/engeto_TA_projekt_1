#!/usr/bin/python3

#TASK MANAGER

ukoly: list[tuple] = []

def hlavni_menu() -> None:
    print("\nSprávce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")

    warning_msg: str = "\nNeplatná hodnota! Zadejte hodnotu v rozsahu 1-4"

    try:
        user_input: int = int(input("Vyberte možnost (1-4): "))
 
        if user_input == 1: pridat_ukol()
        elif user_input == 2: zobrazit_ukoly()
        elif user_input == 3: odstranit_ukol()
        elif user_input == 4: konec_programu()
        else: 
            print(warning_msg)
            hlavni_menu()
    
    except ValueError:
        print(warning_msg)
        hlavni_menu()

def pridat_ukol() -> None:
    task_name: str = input("\nZadejte název úkolu: ")
    task_description: str = input("Zadejte popis úkolu: ")
    task: tuple[str,str] = (task_name, task_description)
    
    if all(task) and not (task[0].startswith(" ") or task[1].startswith(" ")):
        ukoly.append(task)
        print(f"\nÚkol '{task_name}' byl přidán.")
    else:
        print("\nZadejte platný vstup!\n")
        pridat_ukol()
    
    hlavni_menu()

def zobrazit_ukoly(only_list: bool = False) -> None:
    print("\nSeznam úkolů:")
    
    if ukoly:
        for index, (name, description) in enumerate(ukoly, start=1):
            print(f"{index}: {name} - {description}")
    else:
        print("\nAktuálně nemáte vytvořené žádné úkoly.")

    if not only_list: hlavni_menu()

def odstranit_ukol() -> None:
    zobrazit_ukoly(only_list=True)

    try:
        if ukoly:
            task_number: int = int(input("\nZadejte číslo úkolu, který chcete odstranit: ")) 
            task_deleted: str = ukoly[task_number - 1][0]

            if task_number > 0: ukoly.pop(task_number - 1) 
            else: raise IndexError

            print(f"\nÚkol '{task_deleted}' byl odstraněn.")
        else:
            hlavni_menu()

    except ValueError:
        print("\nZadejte platné číslo úlohy.")
        odstranit_ukol()
    except IndexError:
        print(f"\nÚloha {task_number} nenalezena!")
        odstranit_ukol() if ukoly else hlavni_menu()
    
    hlavni_menu()

def konec_programu() -> None:
    print("\nKonec programu.\n")
    exit() 

def main() -> None:
    hlavni_menu()

if __name__ == "__main__":
    main()
