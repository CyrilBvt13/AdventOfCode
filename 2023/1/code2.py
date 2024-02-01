# Creer un tableau vide
sum = [] #tableau des sommes du 1er et dernier chiffre par ligne
total = 0 #total de toutes les lignes

# Fonction : comparer si c'est un nombre
def convert_number(value):
    if value == '1':
        return 1
    elif value == '2':
        return 2
    elif value == '3':
        return 3
    elif value == '4':
        return 4
    elif value == '5':
        return 5
    elif value == '6':
        return 6
    elif value == '7':
        return 7
    elif value == '8':
        return 8
    elif value == '9':
        return 9
    elif value == 'one':
        return 1
    elif value == 'two':
        return 2
    elif value == 'three':
        return 3
    elif value == 'four':
        return 4
    elif value == 'five':
        return 5
    elif value == 'six':
        return 6
    elif value == 'seven':
        return 7
    elif value == 'eight':
        return 8
    elif value == 'nine':
        return 9


# Parcourir le fichier txt et le stocker dans le tableau
with open('input.txt', 'r') as f:
        input = ([f.read().splitlines()])

# Remplir le tableau des sommes  
i = 0
while i < len(input[0]): 

    test_str = input[0][i]

    print(test_str) #On affiche la ligne

    j = 0
    first = False
    last = False

    res = dict([('1', [i for i in range(len(test_str)) if test_str.startswith('1', i)]), 
          ('2', [i for i in range(len(test_str)) if test_str.startswith('2', i)]), 
          ('3', [i for i in range(len(test_str)) if test_str.startswith('3', i)]),
          ('4', [i for i in range(len(test_str)) if test_str.startswith('4', i)]),
          ('5', [i for i in range(len(test_str)) if test_str.startswith('5', i)]),
          ('6', [i for i in range(len(test_str)) if test_str.startswith('6', i)]),
          ('7', [i for i in range(len(test_str)) if test_str.startswith('7', i)]),
          ('8', [i for i in range(len(test_str)) if test_str.startswith('8', i)]),
          ('9', [i for i in range(len(test_str)) if test_str.startswith('9', i)]),
          ('one', [i for i in range(len(test_str)) if test_str.startswith('one', i)]),
          ('two', [i for i in range(len(test_str)) if test_str.startswith('two', i)]),
          ('three', [i for i in range(len(test_str)) if test_str.startswith('three', i)]),
          ('four', [i for i in range(len(test_str)) if test_str.startswith('four', i)]),
          ('five', [i for i in range(len(test_str)) if test_str.startswith('five', i)]),
          ('six', [i for i in range(len(test_str)) if test_str.startswith('six', i)]),
          ('seven', [i for i in range(len(test_str)) if test_str.startswith('seven', i)]),
          ('eight', [i for i in range(len(test_str)) if test_str.startswith('eight', i)]),
          ('nine', [i for i in range(len(test_str)) if test_str.startswith('nine', i)]),
          ])
    
    for k, v in list(res.items()):
        if v == []:
            del res[k]

    minval = {}
    maxval = {}

    for k in res:
        minval[k] = res[k]
    
    for k in res:
        maxval[k] = res[k]

    for k, v in minval.items():
        minval[k] = min(v)
    
    for k, v in maxval.items():
        maxval[k] = max(v)

    minres = convert_number(min(minval, key=minval.get))
    maxres = convert_number(max(maxval, key=maxval.get))

    print('Valeur basse : ', minres)
    print('Valeur haute : ', maxres)
    
    result = str(minres) + str(maxres)

    print('resultat : ', result)
    sum.append(result)

    print()

    i += 1

# Afficher le tableau
i = 0
while i < len(sum):
    total += float(sum[i])
    i += 1 

print('the total is :', total)
