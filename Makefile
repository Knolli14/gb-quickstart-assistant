#################### PACKAGE ACTIONS ###################
reinstall_package:
	@pip uninstall -y 7-wonders || :
	@pip install -e .


run_api: # make -j 2 run_api run_app
	uvicorn gb_assistant.api.fast:app


run_app:
	streamlit run gb_assistant/api/webapp.py


