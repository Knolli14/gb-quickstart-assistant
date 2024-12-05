FROM python:3.10.15-bookworm
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     libsqlite3-dev
#RUN apt update && apt install -y build-essential python3-dev pkg-config zip zlib1g-dev unzip curl wget git htop openjdk-11-jdk liblapack3 libblas3 libhdf5-dev libsqlite3-dev
COPY gb_assistant /gb_assistant
COPY vector_store /vector_store
COPY requirements.txt /requirements.txt
COPY setup.py /setup.py
RUN pip install -r requirements.txt
RUN pip install .
CMD uvicorn gb_assistant.api.fast:app --host 0.0.0.0 --port $PORT
