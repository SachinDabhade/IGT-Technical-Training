FROM python:3.8-slim-buster
 
WORKDIR /app
 
COPY app.py .
 
RUN pip install flask
 
EXPOSE 80
 
# Command to run the app
CMD ["python", "app.py"]
