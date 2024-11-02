valorTotal=0
sp=6783643
rj=3667866
mg=2922988
es=2716548
outros=1984953
nomeEstado=''

valorTotal=sp+rj+mg+es+outros

def percent(estado,nomeEstado): #calcula o percentual do valor total de cada Estado
    
    resultado=0
    
    resultado=estado/valorTotal*100
    
    print(" O percentual que representa ",nomeEstado," é de:",resultado,"%")
    
percent(sp, 'SP')

percent(rj, 'RJ')

percent(mg, 'MG')

percent(es, 'ES')

percent(outros, 'OUTROS')

