# Saisie des 30 notes dans un tableau
notes = []
for i in range(30):
    while True:
        note = float(input(f"Entrez la note de l'élève {i + 1} (entre 0 et 20): "))
        if 0 <= note <= 20:
            notes.append(note)
            break
        else:
            print("Veuillez entrer une note valide entre 0 et 20.")

# Calcul et affichage de la moyenne des notes
moyenne = sum(notes) / len(notes)
print(f"La moyenne des notes est : {moyenne}")

# Calcul et affichage de la note maximale et minimale
note_maximale = max(notes)
note_minimale = min(notes)
print(f"La note maximale est : {note_maximale}")
print(f"La note minimale est : {note_minimale}")

# Calcul et affichage de l'étendue de la série de notes
etendue = note_maximale - note_minimale
print(f"L'étendue de la série de notes est : {etendue}")

# Calcul et affichage du nombre de notes en dessous de 10/20
notes_sous_10 = sum(1 for note in notes if note < 10)
print(f"Le nombre de notes en dessous de 10/20 est : {notes_sous_10}")

# Calcul et affichage de la médiane de la classe
notes_triees = sorted(notes)
if len(notes_triees) % 2 == 0:
    mediane = (notes_triees[len(notes_triees) // 2 - 1] + notes_triees[len(notes_triees) // 2]) / 2
else:
    mediane = notes_triees[len(notes_triees) // 2]
print(f"La médiane de la classe est : {mediane}")

# Calcul et affichage de la moyenne élaguée
notes_sans_extremes = sorted(notes)[1:-1]
moyenne_elaguee = sum(notes_sans_extremes) / len(notes_sans_extremes)
print(f"La moyenne élaguée est : {moyenne_elaguee}")
