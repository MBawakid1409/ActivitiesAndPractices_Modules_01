# Activities & Practices
# --------- [Modules] ---------
print("--------- [Modules] ---------")
print("----------------------------------")
# Practise 01
print("Practise #01")
# Import datetime from datetime below:
from datetime import datetime
current_time = datetime.now()
print(current_time) # 2022-02-17 15:30:21.183400
print("----------------------------------")
# Practise 02
print("Practise #02")
# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1,100) for i in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number) # any random number between 1 and 100
print("----------------------------------")
# Practise 03
print("Practise #03")
# import codecademylib3_seaborn
# from matplotlib import pyplot as plt
# import random
# # Add your code below:
# numbers_a = range(1, 13)
# numbers_b = random.sample(range(1000), 12)
# print(numbers_b)

# plt.plot(numbers_a, numbers_b)

# plt.show()
print("----------------------------------")
print("--------- [Datetimes] ---------")
# Quick introduction about Datetimes
# Importing the 'datetime' module
from datetime import datetime

# Creating a date using year, month, day as arguments.
birthday = datetime(1988, 9, 30, 9, 40, 50)
print(birthday.year) # 1988
print(birthday.month) # 9
print(birthday.day) # 30
print(birthday.hour) # 9
print(birthday.minute) # 40
print(birthday.second) # 50
print(birthday.weekday()) # 4


print("----------------------------------")
# Creating a date using datetime.now()
print(datetime.now()) # 2022-02-18 06:36:51.396052
print(datetime(2018, 1, 1) - datetime(2017, 1, 1)) # 365 days, 0:00:00
print(datetime.now() - datetime(2019, 12, 14)) # 797 days, 6:42:29.689503


print("----------------------------------")
# Parsing a date using strptime (string parsing time)
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

parsed_date = datetime.strptime("Jan 18, 2022", "%b %d, %Y")
print(parsed_date) # 2022-01-18 00:00:00
print(parsed_date.month) # 1
print(parsed_date.year) # 2022
print(parsed_date.day) # 18

print("----------------------------------")
# Rendering a date as a string using strftime (string format time)
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string) # Feb 18, 2022
print("----------------------------------")

time_string = "08/01/2011"

time_stamp = datetime.strptime(time_string,"%d/%m/%Y")


print(time_stamp) # Output: 2011-01-08 00:00:00


print("----------------------------------")
print("--------- [Pipenv] ---------")

# What are [virtual environments] and why are they useful
# local to a specific project which defines all the different versions of Python and the different versions of the different libraries and the different dependencies that you have for a specific project so you can use a virtual environment and in one directory for your one project you might have request version 2.20.1 and yet in another directory and different virtual environment you might be using request version 2.19.0 or some other version.

# Virtual environment just allows you to keep all this organized without you having to manually change the different versions and change the different files that you have for each of these versions on your own, and really when you're working on multiple Python projects and you're working in a real production environment you need to have something like virtual environments set up.

# so as we go forward we'll see how to set one of these virtual environments up and how to install different versions of the same packages and different directories and all sorts of cool stuff, but before we do that we need to actually install what's called pip m or pip env and this is a program allow us to create these virtual environments and to be able to do all of these cool things.

# ----------------------------------
# ----------------------------------
# [Installing pipenv on Windows]
# ----------------------------------
# ----------------------------------

# 1. go to cmd > type: pip --version
# pip 21.2.3 from C:\Python310\lib\site-packages\pip (python 3.10)
# 2. type: pip install --user pipenv < this going to store it on the user level instead of on the global level
# WARNING: The scripts pipenv-resolver.exe and pipenv.exe are installed in 'C:\Users\Yank086L\AppData\Roaming\Python\Python310\Scripts' which is not on PATH.
# Consider adding this directory to [PATH] or, if you prefer to suppress this warning, use --no-warn-script-location.
# Successfully installed certifi-2021.10.8 distlib-0.3.4 filelock-3.6.0 pipenv-2022.1.8 platformdirs-2.5.0 six-1.16.0 virtualenv-20.13.1 virtualenv-clone-0.5.7
# WARNING: You are using pip version 21.2.3; however, version 22.0.3 is available.
# You should consider upgrading via the 'C:\Python310\python.exe -m pip install --upgrade pip' command.

# PATH: a system variable that Windows uses in order to determine where the executables are, so we need to add this PATH onto our path variable so that we can just type in pip env and it'll automatically know to execute pipenv.exe 
# so if we type: pipenv you'll see that 'pipenv' is not recognized as a command so we're going to fix that
# we need to copy the path shown on cmd 'C:\Users\Yank086L\AppData\Roaming\Python\Python310\Scripts' and type on search box beside start button and type 'env' > "Edit the system environment variables" > Environment Variables button > User variables > click on Path > Edit button > New button > ctrl+v the path you already copied > ok ok > close cmd and open it again > type: pipenv --version
# Output: pipenv, version 2022.1.8

# ----------------------------------
# ----------------------------------
# [Creating some virtual environments]
# ----------------------------------
# ----------------------------------

# while you are on the directory type: pipenv --three
# this will initialize a Python virtual environment for Python 3
# Output: Creating a virtualenv for this project...
# Pipfile: G:\000[CodecademyPro]\ComputerScience Career Path\CS101\12Modules\playGround\Desktop\project-1\Pipfile
# Using C:/Python310/python.exe (3.10.0) to create virtualenv...
# [=   ] Creating virtual environment...created virtual environment CPython3.10.0.final.0-64 in 8293ms
#   creator CPython3Windows(dest=C:\Users\Yank086L\.virtualenvs\project-1-bOIUkT3b, clear=False, no_vcs_ignore=False, global=False)     
#   seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Yank086L\AppData\Local\pypa\virtualenv)
#     added seed packages: pip==22.0.3, setuptools==60.6.0, wheel==0.37.1
#   activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

# Successfully created virtual environment!
# Virtualenv location: C:\Users\Yank086L\.virtualenvs\project-1-bOIUkT3b
# Creating a Pipfile for this project...

# generate Pipfile . and this Pipfile is basically a file that has information about the virtual environment and about all the different packages and dependencies that I have
# so inside the file you will see the required version which is 3.10 
# this can actually be configured so you could have one virtual environment that uses one version of python another uses another version of python in our case we have version 3.10 installed so that's what shows up here

# ----------------------------------
# ----------------------------------
# [Working with virtual environments]
# ----------------------------------
# ----------------------------------

# So now we have our virtual environment initialized, we'll see how we can start managing different libraries and different dependencies so we're actually going to go ahead and install one of those libraries we were looking at before so we have request library we also have the numpy library
# This link >> https://pypi.org/project/requests/
# and this > https://pypi.org/project/numpy/

# Install numpy on > type: pipenv install numpy
# Output:
# Installing numpy...
# Adding numpy to Pipfile's [packages]...
# Installation Succeeded
# Pipfile.lock not found, creating...
# Locking [dev-packages] dependencies...
# Locking [packages] dependencies...
#            Building requirements...
# Resolving dependencies...
# Success!
# Updated Pipfile.lock (a6e810)!
# Installing dependencies from Pipfile.lock (a6e810)...
#   ================================ 0/0 - 00:00:00
# To activate this project's virtualenv, run pipenv shell.
# Alternatively, run a command inside the virtualenv with pipenv run.

# pipenv is going to go out and it's going to grap that package and now it's going to update out virtual environment to indicate that it requires this package so that it's using this package now you'll see on Pipfile that numpy="*" that means virtual environment supports any version of numpy because when we install it we didn't specify what version I was looking to use and as far as pipenv is concerned we can use any version

# you'll also notice that another file got created over here this Pipfile.lock file and this basically a file that specifies all of these specific versions of these different libraries and it also just has some other useful information in here and this Pipfile.lock file is meant to be a file that pipenv itself is going to edit so you don't want to actually edit this file  

# Install requests library > type: pipenv install requests==2.26.0
# let's specify the version, older one

# change directory > cd ../project-2
# do it again in project-2 environment
# pipenv --three > pipenv install numpy==1.22.0 > pipenv install requests

# So we have these two projects project-1 project-2 and you can imagine that if you're working in a company these might be two different Python projects that you're responsible for developing in, and instead of having to go off and configure your global Python environment to maintain all these different versions every time that you switch between these projects.

# Now we have these virtual environments set up in order to do that, but the question is how do we actually use these different versions and how do we use this virtual environment?

# well in order to access it we can use the [pipenv shell] 
# the terminal is our normal shell, type: pipenv shell 
# Output: Launching subshell in virtual environment... > type: python
# this is going to open Python interpreter and then in here we can actually use different dependencies and we can operate inside of this virtual environment
# for example: type: import numpy > print(numpy.__version__) > Output: 1.22.0
# in this virtual machine numpy version is different from project-1 version
# type: exit
# now we do this in project-1 and can see different version of numpy is 1.22.2 and also same thing with

# hopefully you guys can see how this works right we can set up these virtual environments and then within these virtual environments we can actually access the shell and from that we can execute our Python programs or we can just use the Python interpreter and that Python will execute in the environment that we set up so all those Python files and everything will execute in that virtual environment and the cool thing is that just by switching from project 1 to project 2 by loading up the shell and in sort of going into that virtual environment, that's all the work I have to do I don't have to change any files I don't have to redownload or change versions I just go into the new project and everything is automatically set up for me so this is the one of the reasons why this is so useful.

# The other reason is because you can specify the environment and then every developer that's working on the project can automatically have that same environment so these pipfile and pipfile.lock can be uploaded into version control or they can be sent to other developers and as long as those developers have these files they'll be able to have the same exact environment that you do when you're developing your Python programs and that's why this so useful.

# This should gives us a basic overview of how all of this stuff works, hopefully it makes sense these virtual environments are pretty simple to understand but they're extremely powerful so it's allows us to customize and to maintain and to change our Python environments without actually having to do any confuguration on our computer from our global Python installation