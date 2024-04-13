# Flask Blog Application

This is a simple blog application built with Flask, a micro web framework for Python. It uses an external API to fetch blog posts and displays them on a user-friendly web interface.

## Project Structure

```
/
├── main.py          # Main Flask application file with routes.
├── post.py          # Post class to handle API requests and data manipulation.
├── templates/       # Folder for HTML templates.
│   ├── index.html   # Home page template showing all posts.
│   └── post.html    # Template for displaying a single post.
└── static/
    └── css/         # Folder for CSS files.
        └── style.css # Styles for the application.
```

### `main.py`

This is the entry point of the application. It initializes the Flask app and defines routes for the home page and individual blog posts.

### `post.py`

Defines the `Post` class which fetches data from an external API and provides methods to retrieve individual post attributes like title, subtitle, and body.

### HTML Templates

- `index.html`: Shows a list of all posts. Each post includes a title, subtitle, and a link to the full post.
- `post.html`: Displays the title, subtitle, and body of a single post based on its ID.

### CSS

- `style.css`: Contains the styling rules for the application, ensuring a clean and responsive design.

## Installation

To run this application, you will need Python installed on your machine. Follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
3. Install Flask using pip:

```bash
pip install Flask
```

4. Run the application:

```bash
python main.py
```

The application will be available at `http://localhost:5000`.

## Additional Notes

- The application fetches data from an external API hosted at `https://api.npoint.io/c790b4d5cab58020d391`. Ensure this API is accessible when you run the application.
- The application uses the Raleway font from Google Fonts and has a simple, responsive design.

