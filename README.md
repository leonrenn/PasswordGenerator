# PasswordGenerator
Simple password generator with easy extandable code.

## Idea behind this Project
Browser and operating systems often offer strong password generation when a new registration on an app
or website is made.<br>
These passwords are extremely secure and I would definitely suggest to use them ahead over this script
also because it is a very fast way generate a new password and store it.<br>
Nevertheless, what happened to me sometimes is that these passwords did not match the requirements
that are made by the app or website. In some cases the password should be of specific length or should just contain
numerical characters, etc.<br>
As far as I know, most of the password providers have not fixed this problem yet, so this is were this project
comes in.


## Short Description
Simple password generator written in such a way that one can easily extend the source code.<br>
The passwords are generated on the command line and specified with flags and respective arguments.<br>
One can easily define default arguments if some specific password types are needed more often.

## Code and Usage

To get the source code from github:
```sh
git clone https://github.com/leonrenn/PasswordGenerator && echo "Copy the following path for your .rc-file:\n" && echo ${PWD}/PassordGenerator/
```
Now you can easily edit the code in your editor.<br>
As this CLI tool should be callable from everywhere and anytime in your terminal, it should be packed in the 
_.*rc_-file of your terminal. To do this go to your home directory and and open the file with your preferred editor (for me it is ***vim***, but this should be adjusted by you):

```sh
cd ~ && vim .bashrc
```

Afterwards you can just easily put an alias that does the job (the path to the directory has to be modified for your system):

```sh
alias pwd_gen='python3 copied_path/src/main.py'
```

When reopening the terminal again, one can easily use the the command ***pwd_gen***.<br>

To see the different options that are supplied by default use the help flag:<br>

```sh
pwd_gen -h
```

The result will give you a table with the following information:<br>

| Flag | Explanation |
| --- | --- |
| -h, --help | Show this help message and exit. |
| -n NUMBER_OF_CHARACTERS, --number_of_characters NUMBER_OF_CHARACTERS | Number of characters. |
| -a, --all | All characters (alphabetic)numeric, special. |
| -abc, --alphabetic | Alphabetic characters. |
| -num, --numeric | Numeric characters. | 
| -s, --special | Special characters. |

The default number of characters is 12 which the security standard for a password. This can be modified by setting the flag and supply a positive integer number greater than 0.<br>
To include all kinds of characters just use the ***[-a]/[--all]*** flag which is equivalent to 
***[-abc -num -s]***. You are free to combine any of the other flags in any order (order won't change the result).


## Requirements
Python version: 3+

## Modifications
If wanted you can go straight ahead and modify the code in your base environment.<br>
Normally, it is good practice to use a virtual environment for development. It can be activated in the following way:

```sh
cd copied_path && conda env create -f environment.yml && conda activate PasswordGenerator 
```





