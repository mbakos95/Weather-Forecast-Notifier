import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config

# Step 1: Get weather data
api_key = "Your-API"  # Securely store your API key in a .env file
city = "Athens, GR" # YOUR CITY
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
if response.status_code == 200:
    weather_data = response.json()
else:
    raise Exception("Error fetching weather data. Check your API key and city name.")

# Step 2: Format the weather data
temperature = weather_data['main']['temp']
description = weather_data['weather'][0]['description']

weather_report = f"Good morning! 🌞\n\nToday's weather in {city}:\n- Temperature: {temperature}°C\n- Condition: {description.capitalize()}"

# Step 3: Send an email
def send_email(subject, body):
    from_email = "example@email.com"  # Use environment variables for sensitive data
    to_email = "example@email.com"
    password = "your password"

    # Email content
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add text content
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)

# Call the email function
try:
    send_email("Today's Weather Report", weather_report)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
