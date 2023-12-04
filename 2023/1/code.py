# Creer un tableau vide
sum = []
total = 0

# Fonction : comparer si c'est un nombre
def isnumber(value):
    if value == '1':
        return True
    elif value == '2':
        return True
    elif value == '3':
        return True
    elif value == '4':
        return True
    elif value == '5':
        return True
    elif value == '6':
        return True
    elif value == '7':
        return True
    elif value == '8':
        return True
    elif value == '9':
        return True
    else:
        return False


# Parcourir le fichier txt et le stocker dans le tableau
with open('input.txt', 'r') as f:
        input = ([f.read().splitlines()])

# Remplir le tableau des sommes  
i = 0
while i < len(input[0]): 
    print(input[0][i])
    j = 0
    first = False
    while (j < len(input[0][i])) and (first == False): 
        if isnumber(input[0][i][j]):
            print('first val : ' + input[0][i][j])
            val = input[0][i][j]
            first = True
            j += 1
        else: 
            j += 1
    k = len(input[0][i])
    second = False
    while (k != 0) and (second == False):
        if isnumber(input[0][i][k-1]):
            print('second val : ' + input[0][i][k-1])  
            val += input[0][i][k-1]
            second = True
            k -= 1 
        else: 
            k -= 1
    print(val)
    sum.append(val)
    i += 1

# Afficher le tableau
i = 0
while i < len(sum):
    #print(sum[i])
    total += float(sum[i])
    i += 1 

print('the total is :')
print(total)

