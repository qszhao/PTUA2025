#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().run_cell_magic('writefile', 'gal.py', 'def read_gal_file(filepath):\n    neighbors = {}\n    with open(filepath, \'r\') as file:\n        for line in file:\n            parts = line.strip().split()\n            try:\n                key = int(parts[0])\n                values = [int(part) for part in parts[1:] if part.isdigit()]  # 只转换数字\n                if values:  \n                    neighbors[key] = values\n                else:\n                    print(f"No valid neighbors found for key {key} in line: {line}")\n            except ValueError as e:\n                print(f"Error converting line: {line}. Error: {e}")\n    return neighbors\n\n\ndef generate_histogram(neighbor_dict):\n    histogram = {}\n    for key, values in neighbor_dict.items():\n        count = len(values)\n        if count in histogram:\n            histogram[count] += 1\n        else:\n            histogram[count] = 1\n    return histogram\n\ndef check_asymmetries(neighbor_dict):\n    asymmetries = []\n    for key, values in neighbor_dict.items():\n        for value in values:\n            if key not in neighbor_dict.get(value, []):\n                asymmetries.append((key, value))\n    return asymmetries\n')


# In[18]:


import importlib
import gal  
importlib.reload(gal)


# In[20]:


neighbor_dict = gal.read_gal_file('Lab04-1.gal')
histogram = gal.generate_histogram(neighbor_dict)
asymmetries = gal.check_asymmetries(neighbor_dict)

print("Neighbor Histogram:", histogram)
print("Asymmetries:", asymmetries)


# In[ ]:


get_ipython().system('jupyter nbconvert --to script my_notebook.ipynb')

