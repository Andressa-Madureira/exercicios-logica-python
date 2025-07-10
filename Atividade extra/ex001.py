#%%
import pandas as pd
# %%{}
idadess = pd.Series([18, 22, 35, 50], index = ['Ana', 'Bruno', 'Carlos', 'Diana'])

print(idadess)
# %%
import pandas as pd

s1 = pd.Series([2, 4, 6], index=["a", "b", "c"])
s2 = pd.Series([1, 2, 3], index=["b", "c", "d"])

print(s1 + s2)
# %%
import pandas as pd
df = pd.DataFrame({'nomes':['João', 'Maria', 'Pedro'],
                   'idades': [25, 30, 22]} )
df.tail(3) #as 3 últimas linhas da tabela

df.head(3) #cabeçalho - primeiras 3 linhas 
# %%
