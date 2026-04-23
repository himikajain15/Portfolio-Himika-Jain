
# Himika Jain - Portfolio Website

A modern, fully scrollable single-page portfolio showcasing professional experience, projects, and skills.

## Features

✨ **Modern Design**
- Clean, professional single-page layout
- Smooth scrolling between sections
- Elegant dark theme with professional blue accents
- Subtle animations and transitions
- Fully responsive design

📱 **Responsive**
- Mobile-first design
- Optimized for all screen sizes

🎯 **Project Highlights**
- Featured projects with GitHub links
- Skill tags for quick scanning
- Contact section with a real working contact form (via Formspree)

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Custom CSS with CSS variables
- **Icons**: Font Awesome 6
- **Contact Form Backend**: [Formspree](https://formspree.io/) (no server code required)

## Project Structure

```
Portfolio-Himika-Jain-main/
├── index.html              # Main single-page portfolio
├── index-static.html       # Static build version of the portfolio
├── static/
│   ├── css/
│   │   └── style.css      # All styles
│   ├── js/
│   │   └── main.js        # Optional JS enhancements
│   ├── images/            # Images used in the portfolio
│   └── Himika_Jain_Resume.pdf
└── README.md
```

## Running Locally

### Option 1: Open directly in browser (recommended)
1. Open `index.html` in your browser.

### Option 2: Use a local development server
From the project root:

```bash
# Python 3
python -m http.server 8000
```

Then visit: `http://localhost:8000`

## Deployment

### GitHub Pages
1. Push the repo to GitHub
2. In GitHub settings, enable **Pages** and point it to the `main` branch / `/` root

### Netlify / Vercel
1. Connect the GitHub repo
2. Use the default build settings (static HTML)
3. Deploy

## Customization

### Change Colors
Edit CSS variables in `static/css/style.css`:

```css
:root {
    --primary: #3b82f6;
    --secondary: #6366f1;
    --accent: #8b5cf6;
}
```

### Update Content
All content is in `index.html`. Edit any of the sections (Home, About, Experience, Projects, Skills, Contact) to update your portfolio.

### Add/Remove Sections
Add new sections using the same structure:

```html
<section id="your-section" class="section">
  <div class="container">
    <h2 class="section-title">Your Title</h2>
    <!-- Your content -->
  </div>
</section>
```

## Contact
- Email: himikajain2110@gmail.com
- LinkedIn: [Himika Jain](https://www.linkedin.com/in/himika-jain-a868741b7/)
- GitHub: [himikajain15](https://github.com/himikajain15)

