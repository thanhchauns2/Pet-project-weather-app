import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class NotificationService:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def send_notification(self, recipient_email, from_email, subject, body):
        message = MIMEMultipart()
        message["From"] = from_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "html"))
        
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.send_message(message)

    def send_daily_weather_notification(self, recipient_email, latitude, longitude, daily_notifier):
        try:
            # Create message
            from_email = self.sender_email
            subject = "Weather Update"
            body = self._format_daily_data(latitude, longitude, daily_notifier)
            self.send_notification(recipient_email, from_email, subject, body)

            return True

        except Exception as e:
            print(f"Failed to send email: {str(e)}")
            return False
    
    def send_hourly_weather_notification(self, recipient_email, latitude, longitude, hourly_notifier):
        try:
            from_email = self.sender_email
            subject = "Weather Update"
            body = self._format_hourly_data(latitude, longitude, hourly_notifier)
            self.send_notification(recipient_email, from_email, subject, body)

            return True

        except Exception as e:
            print(f"Failed to send email: {str(e)}")
            return False

    def _format_daily_data(self, latitude, longitude, daily_notifier):
        # Daily data
        formatted_content = "Daily Forecast:\n"
        formatted_content += f"Max Temperature: {daily_notifier.temperature_2m_max(latitude, longitude)[0]}°C\n"
        formatted_content += f"Min Temperature: {daily_notifier.temperature_2m_min(latitude, longitude)[0]}°C\n"
        formatted_content += f"Sunrise: {daily_notifier.sunrise(latitude, longitude)[0]}\n"
        formatted_content += f"Sunset: {self.daily_notifier.sunset(latitude, longitude)[0]}\n"
        formatted_content += f"UV Index Max: {daily_notifier.uv_index_max(latitude, longitude)[0]}\n"
        formatted_content += f"Rain Sum: {daily_notifier.rain_sum(latitude, longitude)[0]} mm\n"
        return formatted_content

    def _format_hourly_data(self, latitude, longitude, hourly_notifier):
        formatted_content = """
<html>
<body>
<h2>Hourly Forecast (next 24 hours)</h2>
<table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse;">
    <tr style="background-color: #f2f2f2;">
        <th>Hour</th>
        <th>Temperature (°C)</th>
        <th>Humidity (%)</th>
        <th>Precipitation Probability (%)</th>
    </tr>"""

        temperatures = hourly_notifier.temperature_2m(latitude, longitude)[:24]
        humidities = hourly_notifier.relative_humidity_2m(latitude, longitude)[:24]
        precip_probs = hourly_notifier.precipitation_probability(latitude, longitude)[:24]
        
        for hour in range(24):
            row_style = 'background-color: #ffffff;' if hour % 2 == 0 else 'background-color: #f9f9f9;'
            formatted_content += f"""
            <tr style="{row_style}">
                <td>{hour:02d}:00</td>
                <td>{temperatures[hour]:.1f}</td>
                <td>{humidities[hour]:.0f}</td>
                <td>{precip_probs[hour]:.0f}</td>
            </tr>"""
        
        formatted_content += """
</table>
</body>
</html>
            """
        return formatted_content

