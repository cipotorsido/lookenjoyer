setup:
	pip install -r requirements.txt

cache:
	Get-ChildItem -Path . -Include __pycache__,*.pyc -Recurse -Force | Remove-Item -Recurse -Force

chat:
	adk web

venv:
	.venv\Scripts\activate