Knapsack problem:
https://en.wikipedia.org/wiki/Knapsack_problem

Mając do dyspozycji plecak (W) o określonej maksymalnej ładowności, chcemy go zapełnić przedmiotami o sumarycznie największej wartości. Każdy przedmiot posiada swój ciężar (wt) i wartość (val). Algorytm powinien działać w tak, że w sposób dynamiczny wybierze z listy przedmiotów przedmioty, które zmieszczą się w plecaku i łącznie będą miały możliwie największą wartość. Algorytm nie powinien działać siłowo, czyli analizować każdą możliwą opcję zapakowania plecaka, ponieważ złożoność takiego algorytmu wyniesie 2^n i przy dużych zbiorach będzie działał zdecydowanie za wolno.




Dane wejściowe (pobierane od użytkownika z konsoli:
- wartość przedmiotu (val),
- waga przedmiotu (wt)
- maksymalna pojemność plecaka (W)

Dane wyjsciowe:
- łączna wartość przedmiotów w plecaku
