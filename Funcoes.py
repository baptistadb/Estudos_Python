#!/usr/bin/env python
# coding: utf-8

# In[4]:


horas_trabalhadas = [('Danilo',22550),('Fernanda',350098),('Diego',550)]


# In[5]:


def trab_mes(horas_trabalhadas):
    total_horas = 0
    nome_do_funcionario = ''    
    
    for funcionario,tempo in horas_trabalhadas:       
        if tempo > total_horas:
            total_horas = tempo
            nome_do_funcionario = funcionario
        else:
            pass
        
    return(total_horas,nome_do_funcionario)
        


# In[6]:


trab_mes(horas_trabalhadas)

