
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Forecast Notifier</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; background-color: #f9f9f9; margin: 0; padding: 0;">
    <div style="max-width: 800px; margin: 20px auto; background: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
        <h1 style="color: #333;">🌦️ Weather Forecast Notifier</h1>
        <p style="color: #555;">A simple Python script to fetch weather data and send it as an email notification. This project demonstrates how to integrate APIs, format data, and automate email notifications.</p>

        <h2 style="color: #444;">🚀 Features</h2>
        <ul style="color: #555;">
            <li>Fetch weather data from the OpenWeatherMap API.</li>
            <li>Format the weather information into a readable report.</li>
            <li>Send email notifications with the weather report.</li>
        </ul>

        <h2 style="color: #444;">📋 Prerequisites</h2>
        <ul style="color: #555;">
            <li>Python installed on your system.</li>
            <li>An API key from <a href="https://openweathermap.org/api" style="color: #007BFF;">OpenWeatherMap</a>.</li>
            <li>An email account with app password enabled.</li>
            <li>Python libraries: <code>requests</code>, <code>python-decouple</code>.</li>
        </ul>

        <h2 style="color: #444;">⚙️ Installation</h2>
        <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; color: #333;">
# Clone the repository
git clone https://github.com/your-username/weather-forecast-notifier.git

# Install dependencies
pip install requests python-decouple
        </pre>

        <h2 style="color: #444;">📝 Usage</h2>
        <p style="color: #555;">Edit the script to include your API key, email credentials, and desired city. Run the script:</p>
        <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; color: #333;">
python weather_notifier.py
        </pre>

        <h2 style="color: #444;">🔐 Security Note</h2>
        <p style="color: #555;">Avoid hardcoding sensitive credentials in the script. Use environment variables or a <code>.env</code> file to store your API key and email credentials securely.</p>

        <h2 style="color: #444;">📜 License</h2>
        <p style="color: #555;">This project is licensed under the MIT License.</p>

        <footer style="text-align: center; margin-top: 20px; color: #777;">
            <p>Created with ❤️ by <a href="#" style="color: #007BFF;">Your Name</a></p>
        </footer>
    </div>
</body>
</html>
