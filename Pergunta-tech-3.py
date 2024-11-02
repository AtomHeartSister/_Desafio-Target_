import json
maiorFaturamento=0
menorFaturamento=0
maDia=''
meDia=''
mediaM=0
soma=0
totalD=0
superouDia=0
f = open('dados.json')


dado = json.load(f)


for i in dado:

    soma=soma+i.get('valor')
    
    if i.get('valor')!=0: # calcula quantos dias teve faturamento
        
        totalD=totalD+1
        
    if maiorFaturamento<i.get('valor'): #calcula o dia de maior faturamento
        maiorFaturamento=i.get('valor')
        maDia=i.get('dia')
        
    else:
        
        maiorFaturamento=maiorFaturamento
        maDia=maDia
        
    if menorFaturamento>i.get('valor')or menorFaturamento== 0:#calcula o dia de maior faturamento
        menorFaturamento=i.get('valor')
        meDia=i.get('dia')
        
    else:
        menorFaturamento=menorFaturamento
        meDia=meDia

        
media=soma/totalD #calcula a média

for verificar in dado:
    
    if verificar.get('valor')>media:
        
        superouDia=superouDia+1
        
print("O maior faturamento foi ", maiorFaturamento,"no dia ",maDia)

print("O menor faturamento foi ", menorFaturamento,"no dia ",meDia)

print("Número de dias que superaram a média:",superouDia)

f.close()
