# Music App - Django Basics Exam

The app allows a user to browse different albums, including the author, genre, and price. The user can create a catalog of albums. Album creators can also edit or delete their posts at any time.

## Table of Contents

1. [Routes](#routes) 
2. [Identity Requirements](#identity-requirements)  
3. [Database Requirements](#database-requirements)  
4. [Page Requirements](#page-requirements)
5. [Functionality](#functionality)
6. [Security Requirements](#security-requirements)
7. [Code Quality](#code-quality)  
8. [Installation](#installation)  

## Routes
-	http://localhost:8000/ - Home page
-	http://localhost:8000/album/add/ - Add album page
- http://localhost:8000/album/<id>/details/- Details album page
-	http://localhost:8000/album/<id>/edit/ - Edit album page
- http://localhost:8000/album/<id>/delete/ - Delete album page
-	http://localhost:8000/profile/details/ - Profile details page
-	http://localhost:8000/profile/delete/ - Delete profile page

## Identity Requirements

- **Profile Model**: Each user must have a profile with the following fields:
  - **Username** (Character field, required) with a minimum of 2 characters and a maximum of 15 characters. It must contain only letters, numbers, and underscores.
  - **Email** (Email field, required).
  - **Age** (Integer field, optional), but cannot be below 0.
  
- Users can create a profile when they first visit the app. Once a profile is created, they can create albums and perform other actions.

## Database Requirements

Two primary models should be created:

### Profile Model:
- **Username**: Required field, validated for characters.
- **Email**: Required field for email.
- **Age**: Optional integer field, must be above 0.

### Album Model:
- **Album Name**: Required field, unique, max length of 30 characters.
- **Artist**: Required field, max length of 30 characters.
- **Genre**: Required field, max length of 30 characters, with predefined choices.
- **Description**: Optional text field.
- **Image URL**: Required field (URL format).
- **Price**: Required field, must be a positive number.
- **Owner**: ForeignKey relation to the Profile model.

## Page Requirements

### Home Page

- Displays a form to create a profile if one doesn't exist.
  ![image](https://github.com/user-attachments/assets/153eeae7-8dfe-48ef-9cb3-96551dbcd803)
- Once the profile is created, the homepage will display a list of albums associated with the user.
![image](https://github.com/user-attachments/assets/718ac120-fc23-4dd4-96c6-4b32b08a158c)
![image](https://github.com/user-attachments/assets/ec4a72b8-69e4-46d2-85d7-66bc16a42505)

### Add Album Page

- Allows the user to create a new album, including fields like album name, artist, genre, description, image URL, and price.
![image](https://github.com/user-attachments/assets/05063ac8-9d01-4cc7-a410-dd784b0f4da2)

### Album Details Page

- Displays album details like the image, name, artist, genre, price, and description.
![image](https://github.com/user-attachments/assets/8af5ef31-b37a-48c8-93e1-008b0ecb6572)

### Edit Album Page

- Allows the user to edit an existing album's details.
![image](https://github.com/user-attachments/assets/e1d9d57a-d7eb-4381-b6cf-e43b3555ef81)

### Delete Album Page

- Displays album details in a read-only form and allows the user to delete the album.
![image](https://github.com/user-attachments/assets/1aa07e3d-9163-4dc0-98d8-01a8b52c1a15)

### Profile Details Page

- Shows the user's profile, including the username, email, age, and the number of albums.
![image](https://github.com/user-attachments/assets/09cc1fe0-3a27-4f3f-bc2b-35d63ca879ee)

### Delete Profile Page

- Allows the user to delete their profile and all associated albums.
![image](https://github.com/user-attachments/assets/26e0bfe8-efd1-45e5-95db-3c7fc3b1ee40)

## Functionality

- **Profile Creation**: Users must create a profile on the homepage.
- **Album Creation**: Once a profile is created, users can create albums with specific fields.
- **Album Management**: Users can edit, delete, and view album details.
- **Profile Management**: Users can view and delete their profile.

## Security Requirements

- Ensure that the app is secured against common vulnerabilities such as SQL injection, XSS, CSRF, etc.
- Profiles should only be editable by the user who owns them.
- Proper validation and error messages should be implemented for user input.

## Code Quality

- Follow Django best practices for project structure and views.
- Separate concerns between views, templates, and static files.
- Maintain clean and readable code with comments where necessary.
- Implement form validation and error handling for better user experience.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/musicapp.git
   cd musicapp
2. Create a virtual environment and activate it:
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
4. Apply migrations:
   ```bash
   python manage.py migrate
5. Run the development server:
   ```bash
   python manage.py runserver

