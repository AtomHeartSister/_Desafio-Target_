
def Inversao(frase):
 tamanho=len(frase)#checa o tamanho da string

 nova=[ '']

 regulador = 2 
 
 for letra in frase:
     
    nova.insert( tamanho - regulador,letra)# posiciona as letras começando do ultimo caractere

    regulador=regulador+(regulador+1)# regula a posição
    

     
 for resultado in nova:

    print(resultado,end=" ")# posiona horizontalmente a string invertida
    

minhaFrase=input("Escreva algo:  ")

I
nversao(minhaFrase)
