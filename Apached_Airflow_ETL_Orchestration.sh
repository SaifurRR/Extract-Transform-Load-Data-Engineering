****On Mac or Linux****

# Installing Airflow with Pip
pip install apache-airflow

# Initialise the airflow database with the command
airflow db init


# Edit the airflow.cfg file that is found in $AIRFLOW_HOME/airflow.cfg
# for me, it is jennifer/airflow/airflow.cfg 
# Search for [webserver] in the airflow.cfg file
# Add the following lines

authenticate = True
auth_backend = airflow.contrib.auth.backends.password_auth

# Save and close the file.

# Go back to the terminal, we run the user create command 
airflow users create  -u USERNAME  -p PASSWORD -e EMAIL -r ROLE -f FIRSTNAME -l LASTNAME  

# Sample user create command
# airflow users create --username admin --password admin --email ebejennifer14@gmail.com --role Admin --firstname jennifer --lastname ebe

# Start the Airflow Web Server and Scheduler using the command
airflow webserver --port 8080

# click on Allow to allow incoming communications


# In a separate terminal tab without closing the first run the command 
airflow scheduler

# this starts the airflow scheduler

# Open your web browser and go to 
http://localhost:8080 



******On Windows**********

# Make sure you have Python installed on your Windows machine.
# You can download the latest version of Python from the official Python website. During installation, 
# make sure to check the box that says "Add Python to PATH."

# Install Apache Airflow Dependencies:

pip install pywin32
pip install apache-airflow[win]


# Initialize Airflow Database:
# Run the following commands to initialize the Airflow database


airflow db init


# Create Airflow Home Directory:
# Set the AIRFLOW_HOME environment variable to point to the directory where you want to store Airflow's configuration and logs:


set AIRFLOW_HOME=C:\path\to\your\airflow\directory


# Configure Airflow:
# Navigate to the AIRFLOW_HOME directory and create a file named airflow.cfg with the following contents:

[core]
executor = SequentialExecutor


# 6. Start Airflow Web Server:
# Run the following command to start the Airflow web server:


airflow webserver --port 8080


# Start Airflow Scheduler:
# Open a new command prompt, navigate to the AIRFLOW_HOME directory,
# and run the following command to start the scheduler:


airflow scheduler


# Access Airflow Web UI:
Open a web browser and go to http://localhost:8080. 
# You should see the Airflow web UI.

# Create Your First DAG:
# You can create your first DAG (Directed Acyclic Graph) by placing Python scripts with DAG definitions in the AIRFLOW_HOME/dags directory.

