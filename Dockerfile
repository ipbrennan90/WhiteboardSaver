
FROM resin/raspberry-pi-python
ENV INITSYSTEM on
RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*
COPY ./requirements.txt /requirements.txt
ENV READTHEDOCS True
RUN pip install -r ./requirements.txt
COPY ./main.py /main.py
CMD ["python", "main.py"]

