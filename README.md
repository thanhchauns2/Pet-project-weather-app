# Weather Notifier

A backend-sided-only of a project that tracks weather conditions and sends rendered weather reports via email. The system handles data collection, processing, and automated email delivery without a user interface.

The frontend is a separated project.

## Features

- User account management (register, update, delete)
- Weather tracking at specified locations using latitude/longitude
- Email notifications for weather updates
- Multiple notification frequencies (hourly, daily)

## Weather Data Available

### Hourly Data
- Temperature (2m above ground)
- Relative humidity
- Dew point
- Apparent temperature 
- Precipitation (probability, amount, rain, snow)
- Snow depth

### Daily Data
- Temperature (max/min)
- Apparent temperature (max/min)
- Sunrise/sunset times
- Daylight duration
- Sunshine duration
- UV index
- Precipitation (rain, snow)
- Wind speed and gusts

## Getting Started

1. Install required packages:
   ```
   pip install -r requirements.txt
   ```

2. Set up the SQLite database:
   - Uncomment the database creation code in `test.py`
   - Run `python test.py` to create the database and add sample accounts

3. Configure email settings:
   - Update `SMTP_SERVER`, `SMTP_PORT`, `SENDER_EMAIL`, and `SENDER_PASSWORD` in `Business/Constants.py`

4. Run the main application:
   ```
   python main.py
   ```
   This will start the FastAPI server and schedule weather notifications

5. Test the weather notification system:
   ```
   python test.py
   ```
   This will trigger a weather notification for all accounts in the database

## Project Structure

- `main.py`: Entry point of the application, sets up FastAPI and schedules notifications
- `test.py`: Used for database setup and testing the notification system
- `Controller/controller.py`: Contains main logic for weather notifications
- `Controller/DTO.py`: Handles route creation for FastAPI
- `Infra/SQLiteConnector.py`: Manages database operations
- `Business/`: Contains business logic, services, and entity classes

## API Endpoints

- GET `/index`: Returns "Hello World" (example endpoint)

Note: Additional endpoints can be added in `controller.py` and `DTO.py`
