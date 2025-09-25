univer = []
kolleje = []
army = []
married = []

abuturient = [
    {'name': 'Radomir', 'OPT':110, 'gender':'male'},
    {'name': 'Alexader', 'OPT':110, 'gender':'male'},
    {'name': 'Denis', 'OPT':90, 'gender':'male'},
    {'name': 'Islam', 'OPT':80, 'gender':'male'},
    {'name': 'Victorya', 'OPT':200, 'gender':'female'},
    {'name': 'Masha', 'OPT':50, 'gender':'female'},
    {'name': 'Angelina', 'OPT':0, 'gender':'female'},
    {'name': 'Alexey', 'OPT': 0, 'gender':'male'},
    {'name': 'Vlad', 'OPT':0, 'gender':'male'},
    {'name': 'Olga', 'OPT':0, 'gender':'female'},
    {'name': 'Diana', 'OPT':0, 'gender':'female'},
    {'name': 'Adelina', 'OPT':12, 'gender':'female'},
    {'name': 'Elnara', 'OPT':250, 'gender':'female'}
]

def all_abit(lst):
    for i in lst:
        for k,v in i.items():
            return(f'{k}-{v}')

all_abit(lst=abuturient)

def selection(lst, univer:list, kolleje:list, army:list, married:list):
    for i in lst:
        if i['OPT'] >=110:
            univer.append(i)
        elif i['OPT'] < 110 and i['OPT'] >=50:
            kolleje.append(i)
        elif i['OPT'] <=49 and i['gender']=='male':
            army.append(i)
        elif i['OPT'] <=49 and i['gender']=='female':
            married.append(i)


    

selection(lst=abuturient, univer=univer, kolleje=kolleje, army=army, married=married)
print('-'*50)
#print(f'V Iniver{univer}\nV Kollege{kolleje}\nV Army{army}\nMarried{married}') 
print("В Университет:", [i['name'] for i in univer])
print("В Колледж:", [i['name'] for i in kolleje])
print("В Армию:", [i['name'] for i in army])
print("Замуж:", [i['name'] for i in married])       