# integer-predictor

A very simple integer predictor using the Linear Regression model from sklearn / scikit-learn. 

# Installation

Download & install [Python 3.x](https://www.python.org/download/releases/3.0/). After that:
```
git clone https://github.com/martinkaptein/integer-predictor.git

cd integer-predictor/

sudo pip3 install -r requirements.txt
``` 

# Usage

Add the numbers you'd like to predict to a .csv file. It should be structured like this (see example.csv):
```
 0 ,
12 ,
24 ,
36 ,
48 ,
60 ,
72 ,
```
 Hence: Comma-separated integers, in a column (NOT row).

Then just run the script:
`python3 integer-predictor.py`

# Example 

Here's an example on how to generate your .csv input file:

`touch script.py`

```
echo 'for i in range (1000):
    if not (i % 12):
        print(i,",")' >> script.py
```

`python3 script.py >> example.csv`


