import pandas as pd
import matplotlib.pyplot as plt

# on lit le fichier csv
df = pd.read_csv("offres_freelance_mada.csv", encoding="utf-8-sig")

print("ANALYSE MARCHÉ FREELANCE MADAGASCAR (Site MadaAllStar.org)")

nb = len(df)
print(f"\n{nb} offres analysees")

# comptage des domaines
domaines = df['domaine'].value_counts()

print("\n1. DOMAINES QUI RECRUTENT LE PLUS:")
for domaine, compte in domaines.items():
    pourcentage = compte / nb * 100
    print(f"   - {domaine}: {compte} offres ({pourcentage:.0f}%)")

# liste des mots-cles a chercher dans les titres
mots_cles = ['WordPress', 'Node.js', 'SEO', 'Community', 'Assistant', 'Graphiste', 'Marketing', 'PHP', 'Python']

print("\n2. COMPETENCES LES PLUS DEMANDEES:")
for mot in mots_cles:
    compteur = df['titre'].str.contains(mot, case=False, na=False).sum()
    if compteur > 0:
        print(f"   - {mot}: {compteur} offre(s)")

print("\n3. TARIFS PRATIQUES:")
print(" Resultat: les 41 offres ne donnent pas les tarifs. Sur MadaAllStar, les recruteurs ne publient pas les prix")
print("Il faut contacter l'annonceur pour connaitre le tarif ")
print("")

# affichage du graphique avec plusieurs couleurs
plt.figure(figsize=(10, 6))

noms = domaines.index.tolist()
valeurs = domaines.values.tolist()
couleurs = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']

plt.bar(noms, valeurs, color=couleurs[:len(noms)])

plt.title('Offres Freelance par Domaine - Madagascar', fontsize=14, fontweight='bold')
plt.xlabel('Domaine', fontsize=12)
plt.ylabel("Nombre d'offres", fontsize=12)
plt.xticks(rotation=45, ha='right')

# ajout des chiffres sur les barres
for i in range(len(valeurs)):
    plt.text(i, valeurs[i] + 0.3, str(valeurs[i]), ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('resultat_final.png', dpi=150)
plt.show()

# petit recap
print("PROJET TERMINE")
print(" Source: MadaAllStar.org")
print(f"   Offres: {nb}")
print(" Fichier CSV: offres_freelance_mada.csv")
print(" Graphique: resultat_final.png")
print("\n LIMITES:")
print(" - Pas de tarifs sur cette plateforme")
print(" - Une seule source analysee")