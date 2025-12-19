# Portfolio Website Generator

A Python-based static site generator for building a portfolio website on GitHub Pages.

## 🎯 Overview

This project generates a responsive, modern portfolio website from Python configuration files and Jinja2 templates. Perfect for hosting on `aslamhossin.github.io` using GitHub Pages.

## 📋 Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Your Portfolio

Edit `config.py` to customize:
- Your name, title, and social links
- Project descriptions and links
- Skills and technologies

### 3. Generate the Site

```bash
python generator.py
```

This creates a `docs/` directory with your static HTML files.

### 4. Deploy to GitHub Pages

1. Create a repository named `aslamhossin.github.io` on GitHub
2. Push the contents of the `docs/` folder to the repository:
   ```bash
   git init
   git add docs/
   git commit -m "Initial portfolio"
   git remote add origin https://github.com/aslamhossin/aslamhossin.github.io.git
   git push -u origin main
   ```
3. Visit `https://aslamhossin.github.io` in your browser

## 📁 Project Structure

```
├── config.py           # Portfolio configuration
├── generator.py        # Site generator script
├── requirements.txt    # Python dependencies
├── templates/          # Jinja2 HTML templates
│   ├── index.html      # Home page
│   ├── projects.html   # Projects page
│   ├── about.html      # About page
│   └── 404.html        # Error page
├── static/             # CSS and static files
│   └── style.css       # Stylesheet
└── docs/               # Generated static site (created by generator)
```

## 🎨 Customization

### Adding Projects

Edit `config.py` and add to the `projects` list:

```python
'projects': [
    {
        'title': 'Project Name',
        'description': 'Project description',
        'technologies': ['Python', 'React'],
        'github_url': 'https://github.com/...',
        'demo_url': 'https://...',
    },
]
```

### Updating Styles

Modify `static/style.css` to customize the look and feel.

### Adding Pages

1. Create a new Jinja2 template in `templates/`
2. Add a method in `PortfolioGenerator` class in `generator.py`
3. Call the method in `build()`

## 🔧 Development

To regenerate the site after making changes:

```bash
python generator.py
```

## 📝 License

This project is open source and available under the MIT License.

## 📧 Contact

Update the email and social links in `config.py` to match your details.

---

**GitHub**: [aslamhossin](https://github.com/aslamhossin)  
**Portfolio**: [aslamhossin.github.io](https://aslamhossin.github.io)
