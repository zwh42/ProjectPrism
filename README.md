# Project Prism
A experimental Flask project with embedded Jupyter notebook
+ config:
  overide/modify the local jupyter config file with the config file in folder ***config***
  
+ to start:
    + start jupyter notebook locally, record its path, such as "http://localhost:8889/notebooks/analysis.ipynb" 
    + Change the ```notebook_path``` In ***app.py***'s to the local active notebookp ath.  
    + ```python app.py```

+ reference:
  [StackOverflow](https://stackoverflow.com/questions/54535841/jupyter-lab-iframe-in-flask-web-page)