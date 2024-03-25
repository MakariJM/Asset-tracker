from helpers import main_menu,add_asset,search_asset,view_assetlists,display_asset

def cli():
    owner_id = 3
    while True:
        main_menu()
        option = input("Enter your option: ")

        if option == "1":
            add_asset()
            break
        elif option == "2":
            search_asset()
            break
        elif option == "3":
            view_assetlists(owner_id)
            break
        elif option == "4":
            display_asset()
            break
        elif option == "5":
            print("Quiting....")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    cli()