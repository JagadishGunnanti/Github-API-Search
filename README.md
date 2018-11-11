# Github-API-Search

> Scripts written in Python to search a particular file pattern in an organization recursively and to fetch the list of user accounts existing on Github.

## OrgSearch_API_Python.py

- This .py script helps you to search and list out the files that hold particular search pattern in a Github organization.

### Usage
- Get the github authorization token using below command.

> ```curl -vu $username https://api.github.com/```

- Now, update auth token in the python script(TOK:$Token) and run the script as below.

> ```python3 OrgSearch_API_Python.py $Searchpattern```


## UserSearch_API_Python.py

- This .py script helps you to fetch the list of user accounts existing on Github.

### Usage
- Just run the .py script as below.

> ```python3 UserSearch_API_Python.py $username

- Provide password in the prompt and view the results in output.json file under PWD.

