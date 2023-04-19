#!/usr/bin/env python
# coding: utf-8

# #### Ao final do processamento, qual será o valor da variável SOMA?

# In[1]:


k = 0
soma = 0
indice = 13
while (k < indice):
    k += 1
    soma = soma + k
    
print(soma)


# #### Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# In[6]:


def belongsFibo(N):
    n1,n2 = 0,1
    while n1<N:
        n1,n2 = n2,n1+n2
    return n1 == N

belongsFibo(5)


# #### Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# In[88]:


import json

f = open('dados.json')
data = json.load(f)
fatur = []

for i in data:
    if i['valor'] > 0:
        fatur.append(i['valor'])

f.close()
media = sum(fatur)/len(fatur)
dias = 0
for num in fatur:
    if num >= media:
        dias += 1

print('O menor valor de faturamento ocorrido em um dia do mês ==>> {:,.2f}'.format(min(fatur)))
print('O maior valor de faturamento ocorrido em um dia do mês ==>> {:,.2f}'.format(max(fatur)))
print('Número de dias no mês em que o valor de faturamento diário foi superior à média mensal ==>> {}'.format(dias))


# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# 
# SP – R$ 67.836,43
# RJ – R$ 36.678,66
# MG – R$ 29.229,88
# ES – R$ 27.165,48
# Outros – R$ 19.849,53
# 
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

# Escreva um programa que inverta os caracteres de um string.
# 
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

# In[89]:


def contrario(w):
    return w[::-1]
        
contrario('O python é a melhor linguagem para aprendizado')

