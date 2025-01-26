# Smile Social - Social Media Web Application
A full-stack social media web application built with Python and Flask that allows users to share and interact with positive moments and stories.

## Features
- **User Authentication**
  - Register new accounts
  - Login/logout functionality 
  - Password hashing for security
  - Session management

- **Post Management** 
  - Create posts with titles and messages
  - Set happiness levels (Happy, Really Happy, Can't Stop Smiling)
  - Add multiple tags to categorize posts
  - Like posts
  - Delete your own posts
  - View post timestamps

- **Feed & Filtering**
  - Sort posts by date, title, likes, or happiness level
  - Filter to show only your own posts
  - Responsive grid layout for posts

- **UI Features**
  - Clean and responsive design
  - Flash messages for user feedback
  - Moment.js for readable timestamps
  - Tag visualization
  - Like button animations

## Screenshots
| Feature | Screenshot |
|---------|------------|
| Homepage/Feed | ![Homepage showing post feed](/imgs/SmileHome.png) |
| Create Post | ![Create new post form](/imgs/SmilePost.png) |

## Technology Stack
- **Backend**: Python, Flask
- **Database**: SQLAlchemy ORM with SQLite
- **Frontend**: HTML, CSS, Bootstrap, Jinja2 templates
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF
- **Testing**: Unittest, Pytest, Selenium

## Project Structure

This application follows the Model-View-Controller (MVC) architectural pattern:

**Architecture Overview**

* **Model**: Handles data logic and database interactions
* **View**: Manages presentation and user interface
* **Controller**: Coordinates between Model and View, handles business logic

Each component is separated for better maintainability, testability, and scalability.

------------------------
## Install and Run
-----------------------

1. Clone the repository:
```
git clone <repository-url>
cd SmileApp
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Start the development server:
```
python smile.py
```

### Testing
The application includes comprehensive test coverage:

1. Run model tests (unittest):
``` 
python -m unittest -v tests/test_models.py 
```

2. Run the route tests (pytest)

```
python -m pytest -v tests/test_routes.py
```
**Run UI tests** (selenium)

* Download the Chrome webdriver for your Chrome browser version [ChromeDriverDownloads](https://chromedriver.chromium.org/downloads)

* Extract and copy it under `C:\Webdriver` folder.

* Start the application in one terminal: 
```
python smile.py
```

* Run Selenium tests in another terminal:
```
    python tests/test_selenium.py
```