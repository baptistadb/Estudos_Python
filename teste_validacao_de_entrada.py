#!/usr/bin/env python
# coding: utf-8

# In[ ]:


nick=input('Cadastre seu nome')
passe=input('Cadastre sua senha')


# In[ ]:


nick_insert=input('Nome: ')
passe_insert=input('Senha:')

while nick_insert != nick or passe_insert != passe:
    print('Nome ou senha incorreta')
    nick_insert=input('Nome:')
    passe_insert=input('Senha:')
   
    if nick == nick_insert and passe == passe_insert:
        print('Voce entrou no sistema.')
    else:
        print('Senha errada, tente novamente')

