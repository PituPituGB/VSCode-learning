#%%
import math
import sys
import requests
from os import rename


print(sys.version)
print(sys.executable)


def greet(who_to_great):
    greeting = "Hello {}".format(who_to_great)
    return greeting


print(greet("World"))
print(greet("Corey"))

r = requests.get("https://coreyms.com")
print(r.status_code)
# %%

# %%
