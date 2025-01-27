
# Library Management System

![Django](https://img.shields.io/badge/Django-3.x-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![GitHub](https://img.shields.io/badge/license-MIT-orange)

A **Library Management System** built using Django, designed to manage books, members, and transactions in a library. This project is my second Django project, aimed at showcasing my skills in web development with Django.

## Features

- **Book Management**: Add, update, delete, and view books in the library.
- **Member Management**: Add, update, delete, and view library members.
- **Transaction Management**: Issue books to members and track return dates.
- **Search Functionality**: Search for books and members easily.
- **User Authentication**: Secure login and logout functionality for admin users.
- **Responsive Design**: The system is designed to be responsive and user-friendly.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (Default Django DB)
- **Version Control**: Git, GitHub

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/almohsinkhan/Library-Management-System.git
   cd Library-Management-System
   ```

2. **Set Up a Virtual Environment** (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser** (Admin Account):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

- **Admin Panel**: Access the Django admin panel at `http://127.0.0.1:8000/admin/` to manage books, members, and transactions.
- **User Interface**: Use the frontend interface to issue books, return books, and search for books or members.

## Screenshots
![login page](https://github.com/user-attachments/assets/f55e19a0-9b31-488c-befe-58860a8ad260)
![Home Page](https://github.com/user-attachments/assets/a7dc4cc0-ba82-43c2-a18a-34dff23aa4b5)



![Book List](https://github.com/user-attachments/assets/8d052391-98b2-4322-8682-12c887d2b4bc)

![Member List](https://github.com/user-attachments/assets/99b42e5b-e315-4c24-be80-fcaa80b8b982)
![borrow record](https://github.com/user-attachments/assets/622055ca-ce84-45dc-be94-19d72ebc6cf7)


## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Django community for providing excellent documentation and resources.
- Inspired by real-world library management systems.

## Contact

If you have any questions or suggestions, feel free to reach out:

- **Name**: Mohsin Khan
- **Email**: almohsinkhan2004@gmail.com
- **GitHub**: [almohsinkhan](https://github.com/almohsinkhan)

---


