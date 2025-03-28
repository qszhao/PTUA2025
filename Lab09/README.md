# PTUA lecture 9

## Content
This lecture will go through three topics: 
1. Basic SQL in SQL.ipynb
2. Spatail SQL in duckDBVanna_Parquet_v2.ipynb
3. text-to-SQL in LLM.ipynb

**NOTE**
## Installation

DuckDB is extremely easy to install. Go to __[https://duckdb.org/#quickinstall](https://duckdb.org/#quickinstall)__ and select the programming language you are using. 

Due to some version issues with GeoPandas, I recommend following these steps to create a conda environment for this exercise.
<div class="alert alert-block alert-danger">
<b>Note:</b> conda install GeoPandas before DuckDB and others!
</div>

Please create new environmet for this lab using  **Python 3.13**
 
Using [Anaconda](https://docs.anaconda.com/anaconda/install/)  please install the following 

Note: if you use MacOS, you can install the packages via terminal directly. if you use Windows, you can open Anaconda Prompt or cmd.exe Prompt and install the packages from there. 

```bash

#Check current conda channel priority

conda config --get channels

#Switch your default conda channel to conda-forge and set it as the highest priority

conda config --add channels conda-forge 

#Create new environment

conda create -n "geo_env" python=3.13.1

#Check existing conda environment

conda info --envs

#Make sure that you are going to work in newly created environment

conda activate geo_env

# Install jupyter lab

conda install jupyter

# Install packages

conda install python=3 geopandas

#Start the  jupyter lab

jupyter lab

```

More information about creating python virtual environment with conda can be found from [here][blog].
More details about managing conda channel can be found from [1][1] and [2][2]. Difference between Anaconda Prompt and Anaconda Powershell Prompt can be found from [3][3].

[blog]: https://heartbeat.fritz.ai/creating-python-virtual-environments-with-conda-why-and-how-180ebd02d1db
[1]: https://stackoverflow.com/questions/54150169/how-update-remove-conda-forge-channel-from-anaconda/54150817
[2]: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-channels.html
[3]: https://stackoverflow.com/questions/56656493/what-is-the-difference-between-anaconda-prompt-and-anaconda-powershell-prompt
