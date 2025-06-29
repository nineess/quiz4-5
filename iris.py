import sqlite3


conn = sqlite3.connect('nine.sqlite3')
conn.row_factory=sqlite3.Row
c = conn.cursor()
c.execute("SELECT * FROM Iris WHERE Species='Iris-setosa'")
# print(c.fetchone()['SepalLengthCm'])#აბრუნებს პირველ ჩანაწერს მოცემული ველიდან
# print(tuple(c.fetchone()))#დააბრუნებს მეორე ხაზს ცხრილიდან


# for each in c.fetchall():#Iris-setosaს ყველა მონაცემს დაბეჭდავს
#     print(tuple(each))
#
for each in c.fetchmany(5): #Iris-setosaს პირველ 5 ხაზს დაბეჭდავს
    print(tuple(each))



# # ვთხოვთ მომხმარებელს მონაცემების შეყვანას რომელიც შემდეგ დაემატება ცხრილში
# id=float(input("შეიყვანე id (153_ზე მეტი): "))
# sepal_length = float(input("შეიყვანეთ SepalLengthCm: "))
# sepal_width = float(input("შეიყვანეთ SepalWidthCm: "))
# petal_length = float(input("შეიყვანეთ PetalLengthCm: "))
# petal_width = float(input("შეიყვანეთ PetalWidthCm: "))
# species = input("შეიყვანეთ Species (მაგ. Iris-setosa): ")
#
#
# c.execute("INSERT INTO Iris (Id,SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species) VALUES (?, ?, ?, ?, ?, ?)",
#           (id,sepal_length, sepal_width, petal_length, petal_width, species))
# print("ჩანაწერი დაემატა ცხრილში")
#

#
# # მომხმარებლის მიერ არჩეული ხაზი განახლდბა species da petalwith_ის მიხედვით
# id=int(input("შეიყვანე id რომლის განახლებაც გსურთ: "))
# new_species=input("შეიყვანე ახალი species:")
# new_petalwidth=float(input("შეიყვანე ახალი PetalWidthCm: "))
# c.execute("UPDATE iris SET Species=?, PetalWidthCm=? WHERE Id=?", (new_species, new_petalwidth, id))
#
#
# #მომხმარებლის მიერ მოწოდებული id_ით ხაზი წაიშლება ცხრილიდან
# delete_id=int(input("შეიყვანე ის id, რომლის წაშლაც გინდა:"))
# c.execute("DELETE FROM Iris WHERE Id=?", (delete_id,))
# print(f"ჩანაწერი Id={delete_id} წაიშალა წარმატებით")
#
#


import matplotlib.pyplot as plt
import numpy as np

# # დიაგრამაზე ნაჩვენებია რამდენი ჩანაწერია თითოეულ სახეობაზე
# c.execute("SELECT Species, COUNT(*) FROM Iris GROUP BY Species")
# data = c.fetchall()
#
# species = [row[0] for row in data]
#
# counts = [row[1] for row in data]
#
#
# fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
#
#
# def func(pct, allvals):
#     absolute = int(np.round(pct/100.*np.sum(allvals)))
#     return f"{pct:.1f}%\n({absolute:d} g)"
#
#
# wedges, texts, autotexts = ax.pie(counts, autopct=lambda pct: func(pct, counts),
#                                   textprops=dict(color="w"))
#
# ax.legend(wedges, species,
#           title="სახეოებები",
#           loc="center left",
#           bbox_to_anchor=(1, 0, 0.5, 1))
#
# plt.setp(autotexts, size=8, weight="bold")
#
# ax.set_title("Iris სახეობების განაწილება: A pie")
#
# plt.show()
#



#
# # დიაგრამით ვიგებ რამდენი ყვავილია species_ში
# import sqlite3
# import matplotlib.pyplot as plt
#
#
# conn = sqlite3.connect('nine.sqlite3')
# c = conn.cursor()
#
#
# c.execute("SELECT Species, COUNT(*) FROM Iris GROUP BY Species")
# data = c.fetchall()
# conn.close()
#
#
# species = [row[0] for row in data]
# counts = [row[1] for row in data]
# colors = ['tab:blue', 'tab:green', 'tab:orange']
#
# fig, ax = plt.subplots()
#
# ax.bar(species, counts, color=colors)
#
# ax.set_ylabel('მონაცემების რაოდენობა')
# ax.set_title('Iris სახეობების რაოდენობა')
#
# plt.show()
#
#



# აჩვენებს სახეობების ზომებს
import sqlite3
import matplotlib.pyplot as plt
import numpy as np


c.execute("""
    SELECT Species, 
           MAX(SepalLengthCm), 
           MAX(SepalWidthCm), 
           MAX(PetalLengthCm), 
           MAX(PetalWidthCm)
    FROM Iris
    GROUP BY Species
""")
data = c.fetchall()


species = [row[0] for row in data]

iris_max = {
    'Sepal Length': [row[1] for row in data],
    'Sepal Width':  [row[2] for row in data],
    'Petal Length': [row[3] for row in data],
    'Petal Width':  [row[4] for row in data],
}

x = np.arange(len(species))
width = 0.2
multiplier = 0

fig, ax = plt.subplots(layout='constrained', figsize=(10, 6))

for attribute, measurement in iris_max.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

ax.set_ylabel('მაქსიმალური სიგრძე / სიგანე (სმ)')
ax.set_title('Iris სახეობების მაქსიმალური ზომები')
ax.set_xticks(x + width * 1.5, species)
ax.legend(loc='upper left', ncols=2)
ax.set_ylim(0, max(max(v) for v in iris_max.values()) + 1)

plt.show()











conn.commit()
conn.close()

