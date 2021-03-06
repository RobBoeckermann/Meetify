# Meetify Project 

<details><summary><strong>Table of Contents - This File</strong></summary>

- [Overview](#overview)
    - [Team Members](#team-members)
    - [Advisor](#advisor)
- [Project Description](#project-description)

</details>

<details><summary><strong>Table of Contents - Extended Universe</strong></summary>

- [User Manual](docs/user_docs/user_docs.md)
- [User Stories](docs/user_stories.md)
- [Design Diagrams](docs/design_diagrams.pdf)
- [User Interface Specification](docs/ui_spec/UserInterfaceSpec.md)
- Tests
    - [Test Cases](docs/test_cases/TestCases.pdf)
    - [Test Plan](docs/test_cases/TestPlan.pdf)
    - [Test Results](docs/test_cases/TestResults.md)
- Project Progress
    - [Tasks](docs/tasks.md)
    - [Milestones](docs/milestones/milestones.md)
    - [Timeline](docs/milestones/timeline.png)
    - [Effort Matrix](docs/milestones/effort_matrix.png)
- Presentations
    - Midterm
        - [Video Presentation](https://youtu.be/nDZ-knLTBqw)
        - [Slides](docs/presentations/midterm_presentation/midterm_presentation.pdf)
    - Expo
        - [Video Presentation](https://youtu.be/3L6nANa7GtA)
        - [Slides](docs/presentations/expo_presentation/Meetify-Expo-Presentation.pdf)
        - [Poster](docs/presentations/expo_presentation/Meetify-Expo-Poster.pdf)
- Initial Self-Assessment Essays From...
    - [Rob Boeckermann](docs/assessments/fall2020/Rob-Boeckermann-Assessment.md)
    - [Dustin Seger](docs/assessments/fall2020/Dustin-Seger-Assessment.md)
    - [Jake Steuver](docs/assessments/fall2020/Jake-Steuver-Assessment.md)
- Final Self-Assessment Essays From...
    - [Rob Boeckermann](docs/assessments/spring2021/Rob-Boeckermann-Final-Assessment.md)
    - [Dustin Seger](docs/assessments/spring2021/Dustin-Seger-Final-Assessment.md)
    - [Jake Steuver](docs/assessments/spring2021/Jake-Steuver-Final-Assessment.md)
- Professional Biographies From...
    - [Rob Boeckermann](docs/bios/rob-boeckermann-bio.pdf)
    - [Dustin Seger](docs/bios/dustin-seger-bio.md)
    - [Jake Steuver](docs/bios/jake-steuver-bio.md)
- [Hours Summary](docs/milestones/summary_of_hours.md)

</details>

## Overview

**Meetify** is a cross-platform social application for matching users based on
**Spotify activity**. This repository contains the **database code** and
**documentation** for the Meetify project.

For the front-end code, see the [Meetify UI
repository](https://github.com/segeeslice/Meetify-UI). For user usage
instructions, see the [user manual](docs/user_docs/user_docs.md).

### Team Members
**Dustin Seger**  
Computer Science  
dustin.seger@hotmail.com

**Rob Boeckermann**  
Computer Science  
robboeckermann@gmail.com

**Jake Steuver**  
Computer Science  
jakesteuver@gmail.com  

### Advisor
**Bret Patton**  
Software Engineer & Scrum Master @ Paycor  
bret.patton@ymail.com

## Project Description

Meetify a cross-platform application and website that **matches users based on
their musical tastes**. These musical tastes are pulled from the users'
respective Spotify accounts *(thus the name __Meetify__!)*. Meetify will also allow
matched users to message each other in-house 

To accomplish these goals, **Meetify** utilizes the following technologies:

- [**MySQL**](https://www.mysql.com/) database
- [**Python 3.7.9**](https://www.python.org/)-based server (via [**Django 3.1.5**](https://www.djangoproject.com/))
- **HTML/JS** web-based application (via [**React**](https://reactjs.org/))
    - *Written as website; distributed to all major platforms!*

## Dependencies

- `pip install mysql mysql-connector spotipy pillow django-extensions djangorestframework django-cors-headers pymysql celery django_celery_beat`
