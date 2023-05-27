FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the necessary files
COPY city1.py /app/city1.py
COPY city2.py /app/city2.py
COPY city3.py /app/city3.py
COPY city4.py /app/city4.py


# Install any dependencies
#RUN pip install socket

# Set the command to run the city.py script
CMD [ "python", "city1.py", "city2.py", "city3.py", "city4.py" ]



