FROM condaforge/miniforge3:4.12.0-0

EXPOSE 8080

WORKDIR /code/

RUN conda install yfinance addict seaborn plotly dash gunicorn
COPY code/main.py /code/

CMD python -m main
