# Universal-Passport API

## install
### 1. Setup virtual environment
```
$ python3 -m venv unipa-API-venv
```
### 2. Activate virtual environment
```
$ source ./unipa-API-venv/bin/activate
```
### 3. Install required package list
```
unipa-API-venv $ sh ./install.sh
```
### 4. Exit from virtual environment
```
unipa-API-venv $ deactivate
```

## Run
### Normal execution
```
unipa-API-venv $ uvicorn main:app
```
### For development &#x1f527;
```
unipa-API-venv $ uvicorn main:app --reload
```
