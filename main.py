import requests
import boto3
GREEN="\033[1;97;92m"
GCYAN="\033[1;97;93m"
CYAN="\033[1;97;96m"
STOP="\033[0m"

print(GCYAN + '''
 _       ____  ______
| |     / / / / / __ \\
| | /| / / / / / /_/ /
| |/ |/ / /_/ / _, _/
|__/|__/\\____/_/ |_|
''' + STOP)

print(CYAN + "The Website Update Responder!!" + STOP)
print(GCYAN + "@By: 0xRobiul\n" + STOP)

url = input("\033[43;31mUrl To Check:\033[0m ")
try:
 def check_website():
    previous_content = ""
    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()
            current_content = response.text
            if current_content != previous_content:
                print("\033[43;31mChange Detected!!\033[0m")
                client = boto3.client('ses',
                                      aws_access_key_id='YOUR_ACCESS_KEY',
                                      aws_secret_access_key='YOUR_SECRET_KEY',
                                      region_name='YOUR_REASON')
                response = client.send_email(
                    Destination={
                        'ToAddresses': [
                            'receiver@mail.com',
                        ],
                    },
                    Message={
                        'Body': {
                            'Text': {
                                'Charset': 'UTF-8',
                                'Data': 'Website content has changed!',
                            },
                        },
                        'Subject': {
                            'Charset': 'UTF-8',
                            'Data': 'Website Content Changed!',
                        },
                    },
                    Source='Notify Bot! <sender@mail.com>',
                )
                print("\033[43;31mEmail Sent!!\033[0m")
                previous_content = current_content
            else:
                print("\033[42;30mChange Not Found!!\033[0m")
        except requests.exceptions.RequestException as e:
            print("\033[41;33m" + f"An error occurred: {e}" + "\033[0m")
 check_website()
except KeyboardInterrupt:
    pass

