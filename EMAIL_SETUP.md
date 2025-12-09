# Email Configuration Guide

## Quick Setup for Contact Form

To receive emails from your portfolio's contact form, follow these steps:

### Option 1: Gmail App Password (Recommended)

1. **Enable 2-Factor Authentication**
   - Go to your Google Account settings
   - Security → 2-Step Verification → Turn On

2. **Create App Password**
   - Go to: https://myaccount.google.com/apppasswords
   - Select app: "Mail"
   - Select device: "Other" (name it "Portfolio Website")
   - Click "Generate"
   - Copy the 16-character password (e.g., `abcd efgh ijkl mnop`)

3. **Set Environment Variables**

   **Windows PowerShell:**
   ```powershell
   $env:MAIL_USERNAME="himikajain2110@gmail.com"
   $env:MAIL_PASSWORD="abcd efgh ijkl mnop"  # Your app password
   $env:MAIL_DEFAULT_SENDER="himikajain2110@gmail.com"
   ```

   **Mac/Linux Terminal:**
   ```bash
   export MAIL_USERNAME="himikajain2110@gmail.com"
   export MAIL_PASSWORD="abcd efgh ijkl mnop"  # Your app password
   export MAIL_DEFAULT_SENDER="himikajain2110@gmail.com"
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

### Option 2: Alternative Email Services

If you don't want to use Flask backend, consider these services:

#### A. Formspree (Easiest - No Backend Needed!)
1. Sign up at https://formspree.io/
2. Get your form endpoint
3. Update the form in `index.html`:
   ```html
   <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```
4. Remove Flask backend - just serve `index.html` directly!

#### B. EmailJS (Client-Side)
1. Sign up at https://www.emailjs.com/
2. Create email service
3. Add EmailJS SDK to index.html
4. Update the form handler in `main.js`

#### C. Web3Forms
1. Get API key from https://web3forms.com/
2. Add hidden input to form:
   ```html
   <input type="hidden" name="access_key" value="YOUR_ACCESS_KEY">
   ```

### Option 3: Deploy with Email

**Render.com (Free Tier):**
1. Create account at https://render.com/
2. Create new Web Service
3. Connect your GitHub repository
4. Add environment variables in dashboard:
   - `MAIL_USERNAME`
   - `MAIL_PASSWORD`
   - `MAIL_DEFAULT_SENDER`
5. Deploy!

**Heroku:**
```bash
heroku create your-portfolio-name
heroku config:set MAIL_USERNAME="your-email@gmail.com"
heroku config:set MAIL_PASSWORD="your-app-password"
heroku config:set MAIL_DEFAULT_SENDER="your-email@gmail.com"
git push heroku main
```

## Testing

After setup, test the contact form:
1. Fill out all fields
2. Click "Send Message"
3. Check your email inbox (himikajain2110@gmail.com)
4. You should receive an email with the form submission

## Troubleshooting

**"SMTPAuthenticationError"**
- Make sure you're using an App Password, not your regular Gmail password
- Verify 2FA is enabled on your Google account

**"Connection refused"**
- Check if Gmail SMTP port 587 is not blocked by firewall
- Try port 465 with `MAIL_USE_SSL = True` instead of `MAIL_USE_TLS`

**"Failed to send email"**
- Verify environment variables are set correctly
- Check the terminal for detailed error messages
- Ensure `MAIL_USERNAME` matches `MAIL_DEFAULT_SENDER`

## Need Help?

If you encounter issues, consider using Formspree (Option 2A) - it's the simplest solution and doesn't require any backend configuration!

