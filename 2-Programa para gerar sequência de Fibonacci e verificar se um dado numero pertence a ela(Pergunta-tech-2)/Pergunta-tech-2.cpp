#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

int main(){
    setlocale(LC_ALL, "Portuguese");
    int fibonacci[999],numero,proximo=0,anterior=0,tamanho=0;
    cout<<"Digite um número de 0 a 100:"<<endl;
    //gera a sequência de fibonacci
    while(proximo<1000){
         fibonacci[tamanho]=proximo;
         proximo=proximo+ anterior;
         anterior=proximo-anterior;
          tamanho++;
          if(proximo==0){
             proximo=proximo+1;
          }
        
    }
    //pedi um número
    cin>>numero;
    //verifica se o número esta na sequência de Fibonacci
    for(int i=0;i<=tamanho;i++){
        if(fibonacci[i]==numero){
            cout<<"O seu número está na sequência de Fibonacci!"<<endl;
            break;

        }
        else 
        if(fibonacci[i]!=numero&&i>=tamanho){
           cout<<"O seu número não está na sequência de Fibonacci!"<<endl;

        }
    }
}
