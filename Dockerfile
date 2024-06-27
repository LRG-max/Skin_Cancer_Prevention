FROM python:3.10.6-buster

COPY skin_cancer_prevention skin_cancer_prevention
COPY requirements.txt requirements.txt
COPY model model
COPY setup.py setup.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -e .

#Run container locally
CMD uvicorn skin_cancer_prevention.api_file:app --reload --host 0.0.0.0

#Run container deployed
# CMD uvicorn skin_cancer_prevention.api_file:app --reload --host 0.0.0.0 --port $PORT
