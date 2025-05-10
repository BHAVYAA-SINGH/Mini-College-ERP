
# Mini College ERP

A simple web application simulating core functionalities of a college Enterprise Resource Planning (ERP) system. Built from scratch as a learning project using Django for the backend and Tailwind CSS for the frontend styling via CDN.

This project demonstrates fundamental web development concepts with Django, including:

*   Multi-app structure
*   Model definition and database migrations
*   Django Admin for data management
*   URL routing
*   Function-based views
*   Django Templates for dynamic content rendering
*   Template inheritance (`base.html`)
*   Displaying data and relationships (Foreign Keys, Many-to-Many via intermediary model)
*   User Authentication (Login/Logout)
*   Restricting access to views (`@login_required`)
*   Frontend forms for creating, editing, and deleting model instances (CRUD)

## Features

*   **Student Management:**
    *   View a list of all students.
    *   View details of a single student.
    *   Add a new student via a frontend form.
    *   Edit an existing student via a frontend form.
    *   Delete a student via a confirmation page.
    *   View courses a student is enrolled in on their detail page.
*   **Course Management:**
    *   View a list of all courses.
    *   View details of a single course.
    *   Add a new course via a frontend form.
    *   Edit an existing course via a frontend form.
    *   Delete a course via a confirmation page.
    *   View students enrolled in a course on its detail page.
*   **Enrollment Management:**
    *   Add an enrollment for a student (linking student and course) via a frontend form (typically initiated from the student's page).
    *   Delete an enrollment from the student or course detail pages.
*   **Authentication & Access Control:**
    *   Users can log in and log out.
    *   Most application pages (lists, details, forms) require a user to be logged in (`@login_required`).
    *   Access to the powerful Django Admin site (`/admin/`) for comprehensive data management (requires superuser).
    *   *Note: A public self-service registration feature was not implemented for simplicity in this version.*

## Technologies Used

*   **Backend:** Python, Django
*   **Frontend:** Django Templates, HTML, Tailwind CSS (via CDN link)
*   **Database:** SQLite (default Django database)

## Setup and Installation

Follow these steps to get the project running on your local machine:

1.  **Ensure Python and pip are installed:**
    If not, download from [python.org](https://www.python.org/downloads/). Make sure to add Python to your system's PATH during installation (especially on Windows).

2.  **Clone the repository or create the project directory:**
    ```bash
    # If using git
    # git clone <repository_url>
    # cd mini_college_erp

    # If creating manually
    mkdir mini_college_erp
    cd mini_college_erp
    ```

3.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    # venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate
    ```

4.  **Install Django:**
    ```bash
    pip install django
    ```

5.  **Create the Django project structure:**
    ```bash
    django-admin startproject college_erp .
    ```

6.  **Create the apps (`core`, `students`, `courses`):**
    ```bash
    python manage.py startapp core
    python manage.py startapp students
    python manage.py startapp courses
    ```
7.  **Apply database migrations:**
    This creates the database tables for built-in apps and your custom models (Student, Course, Enrollment).
    ```bash
    python manage.py migrate
    ```

8.  **Create a superuser:**
    You need a superuser account to access the Django Admin site and initially log in to the main application.
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create a username and password.

9.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## How to Use

1.  Once the server is running (`http://127.0.0.1:8000/`), open this address in your web browser.
2.  The **Home** page is publicly accessible.
3.  To access Student or Course lists and forms, you need to **log in**. Click the "Login" link in the header.
4.  Log in using the superuser account you created.
5.  Navigate to the **Students** or **Courses** links in the header.
6.  From the list pages, you can:
    *   Click on an item's name/code to view its **Details**.
    *   Use the "Add New..." button to **Create** a new item via a form.
7.  From the detail pages, you can:
    *   Use the "Edit..." button to **Update** the item's details via a form.
    *   Use the "Delete..." button to go to a **Confirmation** page for deletion.
    *   On Student/Course detail pages, view related **Enrollments**.
    *   On the Student detail page, use the "Add Enrollment" button to create a new enrollment.
8.  To delete an enrollment, go to the Student or Course detail page where it's listed and use the small "Delete" link next to it.
9.  Access the **Django Admin** site at `http://127.0.0.1:8000/admin/` using your superuser credentials for backend data management.
10. Click the "Logout" button in the header when finished.

## Future Enhancements

*   Implement user roles/permissions (e.g., Faculty vs. Admin) to restrict CRUD actions or data visibility.
*   Add user registration if needed.
*   Add more models (e.g., Instructors, Departments, Semesters, Grades model for more complex grading).
*   Implement search and filtering on list pages.
*   Improve frontend styling and responsiveness using more advanced Tailwind techniques or a build process.
*   Implement features like assigning instructors to courses, students registering for courses themselves (if allowed).
*   Add messaging framework to display success/error messages after form submissions.




