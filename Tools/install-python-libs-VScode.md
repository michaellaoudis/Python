# Setup Virtual Environment in VS Code (Windows) to Install Python Libraries 

1. Open a folder in your workspace
2. Copy the full system path of the intended project folder
3. Open a new terminal
4. Run the following in terminal: 
	
		python -m venv (folder path)\venv
	
	Example: 

		python -m venv D:\Projects\Python\WebAppSec\venv
	
	This will create a virtual environment in a folder called 'venv'. Any libraries you install with be added to this folder for access by the parent folder.
	
5. Close terminal window and then open a new one
6. Prompt should now reflect a green (venv) followed by current working directory
7. Now you can 'pip install' your libraries!

<hr>

## Activate venv

1. If terminal prompt does not reflect green (venv), type:

		/venv/Scripts/activate

<hr>

## Activate venv for folder on startup

1. In File Explorer, add the intended Folder to your Workspace or Create a new Workspace 

		File > Add Folder to Workspace

2. In File Explorer, Right-Click the Folder and Select 'Open Folder Settings'

3. Search for 'environment'

4. Ensure the following is checked:

		Activate Python Environment in Terminal created using the Extension
