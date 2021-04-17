def knapSack(W, wt, val): 
    n=len(val)
    #utworzenie tabeli:
    table = [[0 for x in range(W + 1)] for x in range(n + 1)] 
    
    #utworzenie zagnieżdżonych pętli, by przejsc przez tabele i wypelnic kazda komorke
    for i in range(n + 1): 
        for j in range(W + 1): 
            if i == 0 or j == 0:  #ustawienie wiersza i kolumny na 0
                table[i][j] = 0
            elif wt[i-1] <= j:  #sprawdzanie czy waga obiektu jest mniejsza niz calkowita dopuszczalna waga
                    table[i][j] = max(val[i-1] #wybranie obiektu, możemy go wybrać lub wykluczyć  
                    + table[i-1][j-wt[i-1]],  table[i-1][j]) 
            else: 
                table[i][j] = table[i-1][j] 
   
    return table[n][W] 
 

values = input("podaj wartosci przedmiotow (po przecinku): ")
list_of_values = values.split(",")
val = [int(val) for val in list_of_values]


weights = input("podaj wagi wagi przedmiotow (po przecinku): ")
list_of_weights = weights.split(",")
wt = [int(wt) for wt in list_of_weights]

W = int(input('Podaj maksymalna wage plecaka: '))
 
print(knapSack(W, wt, val))