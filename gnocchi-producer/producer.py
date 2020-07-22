import requests
import random
import datetime
import json
import time
import sys
import argparse
import subprocess

###########################################
# REMEMBER: RUN "source admin-openrc.sh"  #
# because that program puts ENV variables #
# important for the producer and consumer #
###########################################

# Setting up arguments parser
# Example run command:
# python producer.py --min 10 --max 100 --date 2020-06-11T13:32:51 --id ca3ac69a-67d0-4bd4-bd8b-22debdab0fb3 --sec 15

parser = argparse.ArgumentParser(description='Process gnocchi requests.')

parser.add_argument('--min', type=int, default=0, help='Minimum value for random generator.')
parser.add_argument('--max', type=int, default=100, help='Maximum value for random generator.')
parser.add_argument('--date', default=datetime.datetime.now().replace(microsecond=0).isoformat(), help='Date gnocchi use for start the process.')
parser.add_argument('--id', default="ec021b1a-9156-4011-9b62-8d861d4b6eb3", help='Metric ID. Use by default Huminity Metric ID.')
parser.add_argument('--sec', type=int, default=10, help='Time express on seconds for the sleep time.')

args = parser.parse_args()

##########################################
# Remember the MEASURE                   #
# - Tempeture                            #
# - Wind Speed                           #
# - Humidity                             #
##########################################

# Get the Token from the OpenStack environment
def get_token():
  out = subprocess.Popen(['openstack', 'token', 'issue'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  stdout,stderr = out.communicate()

  if stderr == None:
    response = stdout.decode("utf-8").split("|")

    if len(response) > 0:
      return response[8].strip()
    else:
      return None

  else:
    return None

# Build the URL of the metric we want to request /measures
def get_measurement_url():
  url = 'http://252.3.36.203:8041/v1/metric/' + args.id +  '/measures'
  print("================================")
  print(url)
  print("================================")
  return url

# Build the header for the request session
def get_requests_session(token):
  sess = requests.Session()
  sess.headers.update({'X-AUTH-TOKEN': token,'Content-type':'application/json'})
  return sess

# Parse date for the gnocchi format (ISO-format)
def parse_date():
  return datetime.datetime.strptime(args.date, '%Y-%m-%dT%H:%M:%S')

# Create Random values to put the dimension random.uniform float values between the --min value and the --max value
def generate_random():
  return random.uniform(args.min, args.max)

# Example of the genereted request body: {'timestamp': '2020-06-10T16:44:07', 'value': 57.013062521671884}
def generateRequestBody(item_date):
  return { "timestamp": item_date.replace(microsecond=0).isoformat(), "value": generate_random() }

############################################
# START THE MAIN CODE                      #
############################################

# Gets a token
auth_token = get_token()

if auth_token == None:
  print("There was a problem creating the token.")
  sys.exit()

# Gets the URL to do the requests
url = get_measurement_url()

# Gets a session to do the requests using an authentication code
sess = get_requests_session(auth_token)

# Parses the date we pass as argument
item_date = parse_date()

# Initializing auxiliar variables
data = []
keepRunning = True
seconds = args.sec

# Runs indefinetly the data generation
while keepRunning:

  # Generate 10 values to put them as body
  for i in range(10):
    # Picks the latest date and increase 1 minute
    item_date = item_date + datetime.timedelta(minutes = 1)
    # Includes a random created values
    data.append(generateRequestBody(item_date))

  # Post Data to Gnocchi REST API
  response = sess.post(url, data = json.dumps(data))

  # Prints the result
  print(response)
  print("\n")
  print(data)

  # Refresh variables
  data = []

  # Waits n seconds before running again the program
  time.sleep(seconds)


