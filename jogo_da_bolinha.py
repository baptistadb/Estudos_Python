#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import shuffle

def shuffle_list(copos):
    shuffle(copos)
    return copos

copos_emb=shuffle_list(copo)


# In[ ]:


def palpite():
    
    escolha=''

    while escolha not in ['0','1','2']:
        escolha=input('Escolha um numero entre 0, 1 e 2')
        print('Voce precisa escolher um numero entre 0,1 e 2.')
    
    return int(escolha)


# In[ ]:


def corrigir_palpite(copos,palpite):
    if copos[palpite] == 'O':
        print('Parabens, voce acertou!')
    else:
        print('Voce errou, tente novamente.')
        print(copos)


# In[ ]:


#lista inicial
cops=[' ','O',' ']
#embaralhar os copos
copos_emb=shuffle_list(copo)
#palpite
guess = palpite()
#corrigir o palpite
corrigir_palpite(copos_emb, guess)

