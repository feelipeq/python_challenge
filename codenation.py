#codenation code
#felipe queiroz
import json
import requests
import hashlib
import string

def busca_cifra():
    r=requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=4a2c35df492a5652843194044be93056b51b3363") #Realizar requisição para buscar o json response
    json_data = json.loads(r.text) #Carrega o json de response em uma variavel
    for key,value in json_data.items(): #Percorrer chave e valor do JSON
        if key=='cifrado': #Buscar o campo 'cifrado'
            return value #retorna valor do cifrado
        
    return r.text #retorna o json inteiro caso nao encontre o campo cifrado

def busca_casas():
    r=requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=4a2c35df492a5652843194044be93056b51b3363") #Realizar requisição para buscar o json response
    json_data = json.loads(r.text) #Carrega o json de response em uma variavel
    for key,value in json_data.items(): #Percorrer chave e valor do JSON
        if key=='numero_casas':  #Buscar o campo 'numero_casas'
            return value  ##Retornar o numero de casas
        
    return r.text #retorna o json inteiro caso nao encontre o campo numero de casas
    
def cifra(casas): #Funcao que cria o dicionario de referencia com base no numero de casas
    ref=[] #Array que contera o alfabeto
    for i in range(0,2): #DOis percursos para alimentar o array acima evitando index out of len
        for a in string.ascii_lowercase: #Busca todas as strings em minusculo 
            ref.append(a) #incrementa o array ref com a letra do alfabeto
            
    resultado={} #Dicionario que tera a letra e sua respectiva letra cifrada
    aux={} #Dicionario auxiliar para carregar individualmente os valores
    for i in range (0,26):
        aux={string.ascii_lowercase[i]:ref[i+casas]} #O valor 'a' será igual a + o valor de casas para frente, se 5, a:f
        resultado.update(aux) #Update no dicionario resultado
    aux={' ':' ','.':'.'} #Incluir no dicionario espaco e ponto
    resultado.update(aux) #Incluir ponto e espaço no dicionario auxiliar
    return resultado #retornar o dicionario completo

def cesar(msg,cifra): #funcao que recebe o dicionario referencia e a mensagem a ser traduzida
    cesar='' #String auxiliar que contera a mensagem traduzida
    for i in msg: #Percorrer cada letra da mensagem e buscar o seu valor cifrado no dicionario
        cesar+=cifra[i]
    return cesar

def posta_resultado(json):
    return ''

def main():
    r=busca_cifra() #Busca a frase cifrada
    casas=busca_casas() #Busca qtde de casas
    c={} #Cria dicionario com a letra e sua respectiva cifra
    c=cifra(casas) #Carrega o dicionario na variavel c
    traduzido=cesar(r,c) #Traduz a cifra 
    print(traduzido)
    hexa=hashlib.sha1((traduzido).encode('utf-8')).hexdigest()
    print(hexa)
    input()
    
if __name__ == "__main__":
    main()