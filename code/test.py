#%%
import pandas as pd 
import numpy as np

df = pd.DataFrame({"col_1": np.random.randint(10), "col_2": np.random.random(size=10)})
#%%


df["col_1"].plot()
# %%


def my_func(a:int=3, b:int=2) -> float: 
    """[summary]

    Args:
        a (int, optional): [description]. Defaults to 3.
        b (int, optional): [description]. Defaults to 2.

    Returns:
        float: [description]
    """    
    
    return a * 0.1 + b 