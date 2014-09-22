#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import math
import numpy as np
from scipy.stats import t

X = [8,11,5,15,20,11,13,15,8,9,11,18,16,8,10]
alpha = 0.05

def estima_amostra(amostra_piloto, alpha, margem_erro):
	df = len(amostra_piloto) - 1
	std = np.std(amostra_piloto, dtype=np.float64)
	tval = t.isf(alpha/2, df)
	return math.ceil((tval*std/margem_erro)**2);


erro = 2
print ("Margem de Erro: %d - Tamanho necessário da motra: %d" % (erro, estima_amostra(X, alpha, erro)))
erro = 1
print ("Margem de Erro: %d - Tamanho necessário da motra: %d" % (erro, estima_amostra(X, alpha, erro)))

	
