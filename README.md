# python-project-template
preparation for future development in python. 

# setup virt env and install modules
(install anaconda/conda)
(open conda)
(base) >> conda create -n new_env python=3.8
(new_env) python -m pip install -r requirements.txt

# RUN options (via tasks)
In vscode under TERMINAL -> RUN TASKS ... 
- RUN main APP
- RUN lintering the codes/folders
- RUN unit-test / functional-test
- RUN auto DOCS creation

# folder structure and includes
main.py #main app
README.md # how setup etc
requirements.txt
RUN.bat # *.sh
.vscode
    - tasks.json
        {pylint main app and folders, RUN app/unit-test/fn-test}
docs/
    - user guides 
        {how to run tasks,details, app et cetera}
    - auto created docs
unit_test/
    - __init__.py
    - test_x.py #files
modules/
    - __init__.py
    - modulex.py #files
