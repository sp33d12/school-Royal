# 🚀 Deploy to Render.com — Complete Guide

Host your School Transport System online, for FREE to start, then upgrade for production.

---

## 📋 What You'll Get

- ✅ Live website at `https://your-app.onrender.com`
- ✅ Free SSL certificate (HTTPS)
- ✅ PostgreSQL database (production-grade)
- ✅ Auto-deploy when you push code updates to GitHub
- ✅ Free tier to start (upgrade when you have paying customers)

---

## 📝 Before You Start

You need:
1. A **GitHub account** — free at github.com
2. A **Render account** — free at render.com (sign up with GitHub)
3. **Git** installed on your computer — free at git-scm.com

---

## 🎯 Step-by-Step Deployment

### Step 1: Upload code to GitHub

1. Go to https://github.com/new
2. Create a new repository called `school-transport` (can be **Private** ✓)
3. Don't add README or anything — just click "Create repository"

4. Open PowerShell **inside the `school_v2` folder**:

```bash
cd C:\path\to\school_v2

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/school-transport.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your actual GitHub username.

If git asks you to sign in, use your GitHub email + a **Personal Access Token** (not your password). Create one at: https://github.com/settings/tokens

---

### Step 2: Create the database on Render

1. Go to https://dashboard.render.com
2. Click **"New +"** → **"PostgreSQL"**
3. Fill in:
   - **Name**: `school-transport-db`
   - **Database**: `school_transport`
   - **User**: `school_transport`
   - **Region**: Frankfurt or Singapore (whichever is closer)
   - **Plan**: **Free** (90 days) or **Starter $7/month** (permanent)
4. Click **"Create Database"**
5. Wait 2 minutes for it to initialize
6. Scroll down and **copy the "Internal Database URL"** — you'll need it

---

### Step 3: Create the web service

1. Click **"New +"** → **"Web Service"**
2. Click **"Build and deploy from a Git repository"**
3. Connect your GitHub and select your `school-transport` repo
4. Fill in the settings:

| Field | Value |
|---|---|
| **Name** | `school-transport` (this becomes your URL) |
| **Region** | Same as your database |
| **Branch** | `main` |
| **Runtime** | `Python 3` |
| **Build Command** | `./build.sh` |
| **Start Command** | `gunicorn school_transport.wsgi:application` |
| **Plan** | Free (cold starts) OR Starter $7/month (always on) |

5. Click **"Advanced"** and add these environment variables:

| Key | Value |
|---|---|
| `PYTHON_VERSION` | `3.11.0` |
| `SECRET_KEY` | Click **"Generate"** (Render auto-fills a secure random key) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `.onrender.com` |
| `CSRF_TRUSTED_ORIGINS` | `https://*.onrender.com` |
| `DATABASE_URL` | Paste the database URL from Step 2 |
| `WEB_CONCURRENCY` | `4` |

6. Click **"Create Web Service"**
7. Wait 5-10 minutes for the first build
8. When it shows **"Live"**, your app is online! 🎉

Your URL will be: `https://school-transport-xxxx.onrender.com`

---

### Step 4: Create the admin account

1. In your Render dashboard, click on your web service
2. Click the **"Shell"** tab (in the left sidebar)
3. Run this command:

```bash
python manage.py createsuperuser
```

4. Enter username, email, and password when prompted
5. Now log in at `https://your-app.onrender.com/login/`

---

### Step 5: (Optional) Connect your own domain

1. Buy a domain from:
   - Namecheap (~$12/year)
   - GoDaddy (~$15/year)
   - Cloudflare (cheapest, ~$9/year)

2. In Render, go to your web service → **"Settings"** → **"Custom Domains"**
3. Click **"Add Custom Domain"** → enter `yourdomain.com`
4. Render gives you a CNAME record — add it to your domain provider's DNS
5. Wait 10 minutes — Render auto-generates a free SSL certificate
6. Add your domain to the env var `ALLOWED_HOSTS`:
   - Change `ALLOWED_HOSTS` from `.onrender.com` to `.onrender.com,yourdomain.com`
   - Change `CSRF_TRUSTED_ORIGINS` to `https://*.onrender.com,https://yourdomain.com`

---

## 💰 Pricing Summary

### Free Tier
- **Cost**: $0/month
- **Good for**: Testing, demos, 1-2 schools
- **Limits**:
  - App sleeps after 15 min idle (30s cold start)
  - Database expires after 90 days
  - 750 hours/month web service

### Starter Tier (Recommended for paying customers)
- **Cost**: $14/month total ($7 web + $7 DB)
- **Good for**: Selling to 1-10 schools
- **Benefits**:
  - Always on, no cold starts
  - Persistent database
  - Auto-backups
  - More RAM and CPU

### Pro Tier (For scaling)
- **Cost**: $25-85/month
- **Good for**: 50+ schools
- **Benefits**: More power, priority support

---

## 🔄 How to Update Your App

Whenever you change the code:

```bash
git add .
git commit -m "Added new feature"
git push
```

Render will **automatically rebuild and deploy** — no manual steps needed.

---

## 🆘 Troubleshooting

### "Application failed to respond"
- Check the **"Logs"** tab in Render
- Make sure `DATABASE_URL` is set correctly

### "CSRF verification failed"
- Add your domain to `CSRF_TRUSTED_ORIGINS` with `https://` prefix
- Format: `https://yourdomain.com,https://*.onrender.com`

### "Static files not loading"
- Make sure `build.sh` is executable
- Check logs for `collectstatic` errors

### "Photos disappear after deploy"
- **Important**: Render's free tier has no persistent file storage
- Uploaded photos will be lost on redeploy
- **Solution**: Use AWS S3 or Cloudinary for media files (see `MEDIA_S3.md`)

### App is slow / sleeping
- Free tier sleeps after 15 min idle
- Upgrade to Starter plan ($7/month) to keep it always on
- Or use UptimeRobot.com (free) to ping your app every 5 min

---

## 💼 Selling & Client Management

### For each client school:
1. Create a new Render service (or deploy the same one)
2. Use their school name in the URL: `alnoor-school.onrender.com`
3. Connect their custom domain if they want: `bus.alnoor.edu.iq`
4. Create their superuser account, give them the login
5. Charge them monthly or one-time

### Recommended pricing for hosted service:
- **75,000-150,000 IQD/month** per school (~$60-115)
- Your cost: ~$14/month → profit: $45-100/school/month
- 10 schools = $450-1000/month passive income
- 50 schools = $2,250-5,000/month

---

## 🎯 Quick Checklist

- [ ] Code pushed to GitHub
- [ ] PostgreSQL database created on Render
- [ ] Web service created with correct env vars
- [ ] Admin account created via Shell tab
- [ ] Site loads at `.onrender.com` URL
- [ ] Can log in and add students
- [ ] Custom domain connected (optional)
- [ ] Upgraded to Starter plan (recommended before selling)

---

**📞 Support: Eng. Mohammad Abbas — 07716912103**
