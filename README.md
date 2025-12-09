# Himika Jain - Portfolio Website

A modern, fully scrollable single-page portfolio showcasing professional experience, projects, and skills.

## Features

✨ **Modern Design**
- Clean, professional single-page layout
- Smooth scrolling between sections
- Elegant dark theme with professional blue accents
- Subtle animations and transitions
- Fully responsive design
- Sophisticated color palette

📱 **Responsive**
- Mobile-first design
- Optimized for all screen sizes

💌 **Contact Form**
- Functional email integration
- Form validation
- Success/error feedback

🎨 **Professional Features**
- Smooth scroll animations
- Subtle hover effects
- Professional transitions
- Clean, elegant design
- Industry-standard aesthetics

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python Flask (minimal - only for email)
- **Styling**: Custom CSS with CSS variables
- **Icons**: Font Awesome 6

## Project Structure

```
Portfolio-Himika-main/
├── index.html              # Main single-page portfolio
├── app.py                  # Flask backend for email functionality
├── requirements.txt        # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css      # All styles
│   ├── js/
│   │   └── main.js        # All JavaScript
│   ├── images/
│   │   └── profile.jpg    # Profile image
│   └── Himika_Jain_Resume.pdf
└── README.md
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Email Settings (Important!)

To enable the contact form email functionality, you need to set up environment variables:

#### For Gmail:

1. Enable 2-Factor Authentication on your Google account
2. Create an App Password:
   - Go to: https://myaccount.google.com/apppasswords
   - Select "Mail" and "Other (Custom name)"
   - Copy the generated 16-character password

3. Set environment variables:

**Windows (PowerShell):**
```powershell
$env:MAIL_USERNAME="himikajain2110@gmail.com"
$env:MAIL_PASSWORD="your-app-password-here"
$env:MAIL_DEFAULT_SENDER="himikajain2110@gmail.com"
```

**Mac/Linux:**
```bash
export MAIL_USERNAME="himikajain2110@gmail.com"
export MAIL_PASSWORD="your-app-password-here"
export MAIL_DEFAULT_SENDER="himikajain2110@gmail.com"
```

**Or create a `.env` file** (recommended for local development):
```
MAIL_USERNAME=himikajain2110@gmail.com
MAIL_PASSWORD=your-app-password-here
MAIL_DEFAULT_SENDER=himikajain2110@gmail.com
SECRET_KEY=your-secret-key-here
```

Then install python-dotenv:
```bash
pip install python-dotenv
```

And add to `app.py` at the top:
```python
from dotenv import load_dotenv
load_dotenv()
```

### 3. Run the Application

```bash
python app.py
```

The portfolio will be available at: `http://localhost:5000`

## Deployment

### Render / Heroku / Railway

1. Set environment variables in your hosting platform's dashboard
2. Use `gunicorn` for production (already in requirements.txt)
3. Deploy using Git

### Static Hosting (Netlify / Vercel)

For static-only hosting without email functionality:
- Host `index.html` and `static/` folder directly
- Use a third-party service like:
  - [Formspree](https://formspree.io/) - Easy form backend
  - [EmailJS](https://www.emailjs.com/) - Client-side email
  - [Web3Forms](https://web3forms.com/) - Free form API

## Customization

### Change Colors

Edit CSS variables in `static/css/style.css`:

```css
:root {
    --primary: #3b82f6;        /* Professional blue */
    --secondary: #6366f1;      /* Indigo accent */
    --accent: #8b5cf6;         /* Purple */
}
```

### Update Content

All content is in `index.html` - simply edit the HTML sections.

### Add/Remove Sections

The portfolio is built with semantic HTML sections. Add new sections with:

```html
<section id="your-section" class="section">
    <div class="container">
        <h2 class="section-title">Your Title</h2>
        <!-- Your content -->
    </div>
</section>
```

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## License

© 2024 Himika Jain. All rights reserved.

## Contact

- Email: himikajain2110@gmail.com
- LinkedIn: [Himika Jain](https://www.linkedin.com/in/himika-jain-a868741b7/)
- GitHub: [himikajain15](https://github.com/himikajain15)

