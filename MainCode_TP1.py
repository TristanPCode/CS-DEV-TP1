"""Créé par Tristan POUILLY
Date: 25/09/2023
Fichier création de fonctions du TP1"""



"""Exercice 2"""
def AnneeBissextile(pAnnee):
    """Cette fonction renvoie si l'année en entrée écrit en
    nombre entier int, est bissextile en renvoyant 'True'
    si c'est le cas, 'False' sinon.
    Si l'entrée n'est pas un nombre entier, renverra
    un message indiquant le problème
    Entree: Int"""

    assert isinstance(pAnnee,int), "L'entree n'est pas un entier"
    if pAnnee%100==0: # Si l'année se finit par 00
        return pAnnee%400==0 # On voit si c'est un multiple de 400
    else: # Si l'année ne se finit pas par 00
        return pAnnee%4==0 # On voit si c'est un multiple de 4


def NbJours(pMois,pAnnee):
    """Cette fonction prend 2 paramètres qui sont des nombres entiers, le premier
     est le numéro du mois dans l'année et le deuxième est l'année. La fonction
     renvoie le nombre du jour dans le mois indiqué par un nombre et non pas par
    son équivalent str. Ce nombre en entrée doit être entre 1 et 12 inclus et entier.
    Tout autre nombre ou autre entrée (pour l'année inclus) renverra un message indiquant le problème
    Entree: TUple de 2 nombres: 1 entier en tre 1 et 12 et un entier
    Sortie: Int"""

    assert isinstance(pMois,int), "Le mois n'est pas un entier"
    assert 1<=pMois<=12, "Le mois n'existe pas"
    assert isinstance(pAnnee,int), "L'année n'est pas un entier"
    
    if pMois in [1,3,5, 7, 8, 10, 12]: # Si le mois fait partie de ceux avec 31 jours
        return 31
    elif pMois in [4,6,9,11]: # Si le mois fait partie de ceux avec 30 jours
        return 30
    else: # Si le mois est février
        if AnneeBissextile(pAnnee)==True: # Si l'année est bissextile on renvoie 29 jours
            return 29
        else:
            return 28

def DateValide():
    """Cette fonction va demander une date dans le format DD/MM/YYYY ou DD-MM-YYYY
    Le 3ème et 5ème caractère ne fait rien à la fonction donc l'utilisateur peut
    en théorie mettre ce qu'il veut. Si l'utilisateur renvoie plus de 10 caractères
    et que les 8 autres non mentionnées précédemment ne sont pas des chiffres, la
    date sera considérée comme non valide. Si la date est conforme dans son format,
    on vérifie son existence, si elle existe la fonction dit que la date est valide,
    sinon, elle dit qu'elle n'est pas valide.
    Entrée: Rien
    Sortie: Texte sous forme de print"""

    Valide=False # Vérification finale avant l'affichage à l'utilisateur

    Inp=input("Veuillez saisir votre date pour voir si elle existe! (DD/MM/YYYY) \n")
    assert len(Inp)==10, "Le format n'est pas correct"

    StrChiffres=["0","1","2","3","4","5","6","7","8","9"]
    VerifIndices=[0,1,3,4,6,7,8,9] # L'ensemble des indices à vérifier dans l'entrée
    NextStepChecker=1 # Valeur qui permet si on fait continue l'analyse après la boucle suivante"

    for i in VerifIndices:
        if not Inp[i] in StrChiffres: # On vérifie que nos caractères sont des chiffres (en str)
            NextStepChecker=0
    if NextStepChecker==1: # Si tous les charactères souhaitaient étaient des chiffres
        Jour=int(Inp[0]+Inp[1]) # On convertit nos données en chiffres
        Mois=int(Inp[3]+Inp[4])
        Annee=int(Inp[6:10])
            
        if not (Jour==0 or Mois==0):
            JourMax=NbJours(Mois,Annee) # Nombre de jours maximum dans le mois choisi
            if Jour<=JourMax: # Si le jour ne dépasse pas le nombre de jour possible
                Valide=True # C'est valide!
    
    if Valide==True:
        print("La date existe belle et bien")
    else:
        print("Cette date, si c'en était une, n'existe pas...")

"""Exercice 3"""
def mesImpots(Revenu):
    """Cette fonction vous dit combien vous devez payez aux impôts en 2022. Eh oui faut pas les oublier!
    Rentrez simplement votre revenu annuel brut et découvrez à quel point vous serez généreux au
    gouvernement (générosité obligatoire selon la législation). Si l'entrée n'est pas un entier,
    la fonction vous avertira. Alors combien alllez-vous payez cette année?
    Entree: Int
    Sortie: Int"""

    assert isinstance(Revenu,int), "Le revenu n'est pas entier, c'est pas sérieux ça!"

    ListCap=[0,0,10225,26070,74545,160336] # On rajoute les 0 pour éviter les indices négatives plus tard
    ListTaux=[0,0,0,0.11,0.30,0.41,0.45] # On rajoute les 0 pour éviter les indices négatives plus tard
    indice=0 # Le nombre d'étape à faire
    while Revenu>ListCap[indice] and indice<=4: # Si le revenu est plus grand que le cap suivant
        indice+=1 # On ajoute une étape
    if Revenu>160336: # On rajoute si on est encore au dessus
        indice+=1

    Top=Revenu # On définit une variable de réccurrence avec le plus grand
    Bottom=ListCap[indice-1]+1 # On prend le max du cap précédent et on ajoute 1 pour le min
    Impots=0 # Somme à compléter

    for k in range(indice-2): # Enchaîne les successions d'ajouts d'impôts pendant le nombres d'étapes
        # Sachant que les deux premiers ListCap sont vides donc on enlève 2

        Impots+=(Top-Bottom)*ListTaux[indice-k] # on ajoute l'impot de l'étape (k augmente de 1)
        Top=Bottom-1 # On passe à la tranche d'en dessous, le seuil est le min de l'ancien -1
        Bottom=ListCap[indice-k-2]+1 # et le minimum et celui dans ListCap
    return int((10*Impots)//10) # Une fois la somme faite on renvoie tout

"""Exercice 4"""
def verification(pMat):
    """Vérifie que l'objet envoyer est bien une matrice rectangulaire.
    L'entrée doit se faire sous forme de liste de liste avec des sous listes
    de même longueurs (sinon ce n'est pas une matrice).
    Entree: Liste de listes
    Sortie: True or False"""
    assert isinstance(pMat,list), "Votre objet n'est pas une liste"

    for ligne in pMat:
        assert isinstance(ligne,list), "Votre liste ne contient pas que des sous listes"
        assert len(pMat[0])==len(ligne), False
        for element in ligne:
            assert (isinstance(element,float) or isinstance(element,int)), "Votre matrice ne contient pas que des nombres"
    return True

def verification_matrice(pMat1,pMat2):
    """Vérifie que les objets sont des matrices et que la multiplication est possible.
    Il faut envoyer des listes avec des sous listes pour représenter les matrices.
    Entree: TUple de 2 Listes de listes
    Sortie: True or False"""
    assert verification(pMat1)==True, "Votre premier objet n'est pas une matrice"
    assert verification(pMat2)==True, "Votre deuxième objet n'est pas une matrice"
    return len(pMat1[0])==len(pMat2) # Regarde si la longueur de lignes de pMat1 est égale à la hauteur de colonnes de pMat2

def ProdMat(pMat1,pMat2):
    """Cette fonction effectue quand elle est possible le produit matriciel des deux matrices
    en entrée (sous forme de liste de sous listes) et renvoie le résultat en sortie.
    Entree: TUple de 2 Listes de listes
    Sortier: Liste de listes"""
    assert verification_matrice(pMat1,pMat2)==True, "Le produit matriciel n'est pas possible"

    pMatTotal=[]
    for _ in range(len(pMat1)): # Il y aura autant de lignes que pMat1
        pMatTotal.append([]) # Création de chaque lignes

    for i in range(len(pMat1)):
        for k in range(len(pMat2[0])):
            pMatTotal[i].append(0)
            for j in range(len(pMat1[0])):
                pMatTotal[i][k]+=pMat1[i][j]*pMat2[j][k]
    return pMatTotal