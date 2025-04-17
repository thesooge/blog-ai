# Django Blog

A modern blog application built with Django that allows users to create, edit, and manage their blog posts.

## Features

- User authentication (login/signup)
- Create, read, update, and delete blog posts
- Rich text editor for post content
- Responsive design using Bootstrap
- User-specific post management
- Clean and modern UI

## Requirements

- Python 3.8+
- Django 4.2+
- Bootstrap 5
- Font Awesome 5

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd prj-7-blog-ai
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see the blog in action.

## Usage

1. Register a new account or log in
2. Create new posts using the "New Post" button
3. Edit or delete your own posts using the buttons on each post
4. View all posts on the home page
5. Click on a post to view its full content

## Project Structure

```
prj-7-blog-ai/
├── blog/                   # Main blog application
│   ├── models.py          # Database models
│   ├── views.py           # View logic
│   ├── urls.py           # URL routing
│   └── templates/        # HTML templates
├── static/               # Static files (CSS, JS)
├── templates/           # Base templates
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies
```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 