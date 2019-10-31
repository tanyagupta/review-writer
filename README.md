# review-writer
## Objective
Using natural language processing for smart review writing
## Pipenv
1. IMPORTANT: be sure you are in the right directory
2. pipenv shell to install shell
3. pip install nlp (or other packages)
## Import and download packages
*>>> import nltk* in python shell <br>

*>>> nltk.download('wordnet')* in python shell

*nltk.download('opinion_lexicon')*

*nltk.download('punkt')* etc.

For a specific directory use: To specify the download directory, use for example:

nltk.download('wordnet', download_dir='/workspace/nlp/nltk_data')

On the terminal do: export NLTK_DATA=//workspace/nlp/nltk_data before calling your python script

## Gitpod error handling
For error *ERROR: Can not perform a '--user' install. User site-packages are not visible in this virtualenv*, try:
export PIP_USER=no
(reference https://github.com/gitpod-io/gitpod/issues/479)

## Getting Started
1. Go to the correct directory
2. Check if pip file is there
3. Open shell *pipenv shell*
4. Open python by typing *python*, this starts the python shell (you will see three arrows like so >>>)
5. Run a python program with parameters like so: *python main.py feelings_leela_ambience.txt template.txt*


## Useful info
1. Use exit() to exit python shell and exit to exit terminal
1. 4. You have to be in the python shell to run the code
1. Run python code from pipenv shell. You know you are in pipenv shell when you see () around the location
1. Run python shell from pipenv shell. You know you are in python shell when you see >>>
1. Run python code by *python name_of_file.py*
1. If the file is in a different location you can still run it from pipenv shell using the correct location. For instance if the file is one level above the current location use *python ../test.py*
1. Note pipenv shell has nothing to do with directories. You can always cd to change the directory within the pipenv shell. In the above example you can cd .., pwd to check you are one level up and then directly run *python test.py* without the *../*

