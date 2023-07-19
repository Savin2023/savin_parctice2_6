from random import randint

def inter_search(to_search):
    arr=[]
    for i in range(100):
        arr.append(randint(1,100))
    arr.sort()
    answer=-1
    print(arr)          
    left=0              # левая граница списка
    right=len(arr)-1    # правая граница
    while (left<=right and to_search>=arr[left] and to_search<=arr[right]):
        part1=float(right-left)/(arr[right]-arr[left])
        part2=to_search-arr[left]
        index=left+(int(part1*part2))
        if arr[index]==to_search:
            answer=index
            break
        if arr[index]<to_search:
            left=index+1
        else:
            right=index-1
    
    if answer!=-1:
        print("Элемент в списке присутствует, его индекс:",answer)
    else:
        print("Элемент в списке отсутствует")

# --------------------------------------
def erato(n):
    arr=[]
    for i in range(n):
        arr.append(i)
    arr[1]=0
    for i in range(n):
        if arr[i]!=0:
            j=i*2
            while j<n:
                arr[j]=0
                j+=i
    for elem in arr:
        if elem!=0:
            print(elem,end=" ")
    print("\n")
# --------------------------------------
def find_str():
    str_where="Sabracadabra"
    str_find="cad"
    index_where=0
    index_find=0
    len_where=len(str_where)
    len_find=len(str_find)

    while (index_where<=(len_where-len_find) and index_find<len_find):
        if str_where[index_where+index_find]==str_find[index_find]:
            index_find+=1
        else:
            index_where+=1
            index_find=0
    print(f"'{str_where}'")
    print(f"'{str_find}'")
    if index_find==len_find:
        print(f"Такая подстрока есть, её начало - {index_where}\n")
    else:
        print("Такой подстроки в исходной строке нет\n")
# --------------------------------------
command=""
while command!="stop":
    print("Введите команду:")
    print("i - интерполяционный поиск")
    print("r - решето Эратосфена")
    print("s - поиск подстроки в строке")
    print("stop - выход")
    command=input()
# --------------------------------------
    if command=="i":
        print("Введите натуральное число до 100")
        to_search=int(input())
        if to_search <1 or to_search>1000:
            print("Ошибка ввода\n")
        else:
            inter_search(to_search)
# --------------------------------------
    elif command=="r":
        print("Введите натуральное число")
        predel=int(input())
        if predel<1:
            print("Ошибка ввода\n")
        else:
            erato(predel)
# --------------------------------------
    elif command=="s":
        find_str()
