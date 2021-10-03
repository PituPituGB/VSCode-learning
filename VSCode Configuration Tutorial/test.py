#%%
import math
import sys
import requests
from os import rename

r = requests.get("https://coreyms.com")
print(r.status_code)
print(r.ok)
# %%

# %%
