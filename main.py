import task
import os

print("\033[1;30mhello")
choice = "0"

taches = task.load_list()
task.task_list(taches)

while choice != "6":
    choice = input(str("\033[1;34mque voulez vous faire?\n\033[1;31m1- \033[1;34m Ajouter une tache\n\033[1;31m2- \033[1;34m Afficher les taches\n\033[1;31m3- \033[1;34m Supprimer une tache\n\033[1;31m4- \033[1;34m Cocher les taches\n\033[1;31m5- \033[1;34m Afficher les statistiques\n\033[1;31m6- \033[1;34m Quitter\n"))
    if choice == "1":
        task.task_add(taches)
    elif choice == "2":
        task.task_list(taches)
    elif choice == "3":
        task.task_remove(taches)
    elif choice == "4":
        task.task_check(taches)
    elif choice == "5":
        task.print_statistics(taches)
        (taches)
    elif choice == "6":
        print("Bye")