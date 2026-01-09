import os 
import papermill as pm
import concurrent.futures

######## DO NOT HAVE ANY TUTORIAL OPEN WHEN RUNNING THIS SCRIPT ########
######## IT WILL CAUSE THE SCRIPT TO BE WIPED - WORKFLOW SAVES THE NOTEBOOK AFTER EVERY CELL ########

tutorials_dir = 'tutorials'
files_to_ignore = ['Importing a spatialData dataset.ipynb',
                   'Importing a Visium dataset.ipynb',
                   'Importing a Xenium dataset.ipynb',
                   'Importing data from QuPath.ipynb',
                   'MuSpAn - Figure_2.ipynb',
                   'MuSpAn - Figure_3.ipynb',
                   'MuSpAn - Figure_4.ipynb',
                   'MuSpAn - Figure_5.ipynb',
                   'MuSpAn - Figure_6.ipynb']

list_of_bad_tutorials = []

def execute_notebook(notebook_path):
    try:
        pm.execute_notebook(notebook_path, notebook_path,progress_bar=False)
        print(f'Successfully executed {notebook_path}')
        return None
    except Exception as e:
        print(f'Error executing {notebook_path}: {e}')
        return notebook_path

notebook_paths = [os.path.join(root, file) for root, dirs, files in os.walk(tutorials_dir) for file in files if file.endswith('.ipynb') and file not in files_to_ignore]

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(execute_notebook, notebook_paths))

list_of_bad_tutorials = [result for result in results if result is not None]

if list_of_bad_tutorials:
    print('The following tutorials failed to execute:')
    for tutorial in list_of_bad_tutorials:
        print(tutorial)
else:
    print('All tutorials executed successfully!')
    

# Clean up files created by the tutorials
files_to_delete = ['Example_domain.csv', 'Random_domain.muspan']

for file_to_delete in files_to_delete:
    file_path = os.path.join(os.getcwd(), file_to_delete)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f'Deleted {file_path}')