FROM --platform=linux/amd64 python:3.10.6-buster
COPY gb_assistant /gb_assistant
COPY requirements.txt /requirements.txt
COPY setup.py /setup.py
RUN pip install -r requirements.txt
RUN pip install .
CMD uvicorn gb_assistant.api.fast:app --host 0.0.0.0 --port $PORT
