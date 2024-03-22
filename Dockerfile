FROM thuuyen18102001/nckh2023:cnn-env-v1.0

RUN pip install jupyter
RUN pip install pandas==0.20.3 matplotlib==2.0.2

WORKDIR /app

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]