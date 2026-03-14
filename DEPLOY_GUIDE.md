# 🚀 Railway Deployment Guide - Streamlit Gemstone Predictor

## ✅ Files Ready for Deployment

All configuration files have been set up:
- ✅ `app_streamlit.py` - Beautiful Streamlit UI
- ✅ `Procfile` - Configured for Streamlit
- ✅ `.streamlit/config.toml` - Streamlit settings
- ✅ `requirements.txt` - All dependencies including streamlit
- ✅ Trained model with 97.45% accuracy

---

## Quick Deployment (3 Steps)

### Step 1: Push to GitHub

```powershell
# Navigate to project
cd "e:\New Volume\gemstone-price-predictor-main\gemstone-price-predictor-main"

# Initialize Git
git init

# Add all files
git add .

# Commit
git commit -m "Ready for Railway deployment"

# Connect to GitHub (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/gemstone-predictor.git

# Set branch and push
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Railway

1. Go to **https://railway.app**
2. Sign in with **GitHub**
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. Select your **gemstone-predictor** repository
5. Railway will auto-detect Python and deploy! ⚡

### Step 3: Access Your Live App

- Deployment takes ~3-5 minutes
- Railway provides a public URL (e.g., `gemstone-predictor-production.up.railway.app`)
- Share it with the world! 🌍

---

## What You Get

✨ **Features:**
- Modern, responsive UI
- Two-column layout for better UX
- Interactive input fields with validation
- Quality reference guide
- Instant price predictions
- Professional styling

🎯 **Model Performance:**
- Training R²: 0.9752
- Test R²: 0.9745
- Powered by CatBoost

---

## Deployment Configuration

### Procfile
```
web: streamlit run app_streamlit.py --server.port $PORT --server.address 0.0.0.0 --server.headless true
```

### Requirements
- streamlit
- pandas
- scikit-learn
- catboost
- xgboost
- dill
- gunicorn (Railway uses this)

### Environment Variables
No configuration needed! Everything works out of the box.

---

## Troubleshooting

### Build Fails?
1. Check Railway logs in dashboard
2. Verify all files committed: `git status`
3. Ensure artifacts/model.pkl exists

### App Won't Load?
1. Check Railway logs for errors
2. Verify Procfile has correct command
3. Make sure port configuration is correct

### Model Loading Error?
1. Confirm `artifacts/model.pkl` exists
2. Confirm `artifacts/preprocessor.pkl` exists
3. Check file sizes (model.pkl ~32MB, preprocessor.pkl ~3KB)

---

## Cost Estimate

Railway Free Tier:
- $5/month credit included
- This app typically uses ~$2-3/month
- Pay-as-you-go after free credit

Estimated monthly cost: **FREE or ~$2-3**

---

## Alternative: Deploy with Railway CLI

```powershell
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Deploy directly
railway up
```

---

## Updating Your App

After making changes:

```powershell
git add .
git commit -m "Your update message"
git push
```

Railway automatically redeploys on push! 🔄

---

## Success Indicators

✅ Build completes without errors
✅ Logs show "You can now view your Streamlit app"
✅ App accessible via Railway URL
✅ Predictions working correctly

---

## Need Help?

1. Check Railway dashboard logs
2. Review this guide's troubleshooting section
3. Verify all files are committed to Git

**Your gemstone predictor will be live in minutes!** 🎉
