# Easy Move Project Documentation

## Project Overview

**Project Name:** Easy Move
**Tag Line:** Simplifying Your Journey: Efficient Routes and Weather Insights

## Team Members

- Precious Enuagwune: Frontend Developer
- Godwin Lawal: BackEnd/DevOps Specialist
- Sideeg Mohammed: BackEnd Developer
- Roles Decision: The team roles were decided based on individual strengths and expertise. Godwin has experience in project management and system design and Precious excels in software frontend development, specializing in user interface and experience design.ٍSideeg has experience in backend, database design and api building

## Technologies Used

- **Programming Language:** Python
- **Libraries/Frameworks:** Flask (for web application), Requests (for API calls), Geopy (for location-based calculations), OpenWeatherMap API (for weather data)
    - **Resources:** Code editor (e.g., Visual Studio Code), version control system (e.g., Git), web browser

    **Alternate Technology Options and Trade-offs:**
    1. Instead of Flask, we could have considered Django as an alternative web framework. The trade-off was complexity; Flask's lightweight nature aligns better with the simplicity goal.
    2. For weather data, we could have chosen the Weather API from a different provider. The trade-off was familiarity; we opted for OpenWeatherMap due to its wide usage and ease of integration.

## Challenge Statement

- **Problem:** The Easy Move project aims to address the challenge of finding the shortest route and obtaining weather conditions for a user's desired destination.
- **Project Scope:** The project will not provide real-time traffic updates or suggest alternative modes of transportation.
- **Target Users:** The project will benefit travelers who seek efficient routes and want to be aware of weather conditions at their destinations.
- **Locale Dependency:** The project's functionality is not dependent on any specific locale; it can be used globally.

## Risks

    - **Technical Risks:** A potential technical risk is integrating the APIs smoothly. To mitigate this, we will thoroughly test API interactions and have error-handling mechanisms.
    - **Non-Technical Risks:** Users' reliance on accurate weather information is a non-technical risk. You will add disclaimers about data accuracy to minimize potential impacts.

## Infrastructure

    - **Branching and Merging:** The team will use a feature branching model in the Git repository, ensuring each feature is developed independently before merging.
    - **Deployment Strategy:** The application will be deployed on a cloud platform (e.g., Heroku) using a continuous deployment pipeline.
    - **Data Population:** Initial data will be populated through API calls and user interactions during application use.
    - **Testing Tools:** Automated testing will be performed using the unittest framework in Python, ensuring reliability and functionality.

## Existing Solutions

    - **Google Maps:** Similar in providing routes but lacks weather information.
    - **Waze:** Offers real-time traffic data but lacks weather information.
    - **Weather.com:** Provides weather forecasts but lacks route planning.

    ---
