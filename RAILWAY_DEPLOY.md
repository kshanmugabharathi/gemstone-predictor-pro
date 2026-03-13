# Railway Deployment Guide for Gemstone Price Predictor

## Prerequisites
- Git installed on your computer
- Railway account (https://railway.app)
- GitHub account

## Step-by-Step Deployment

### 1. Prepare Your Files

The following changes have already been made:
- ✅ Added `Procfile` for Railway
- ✅ Updated `requirements.txt` (removed ipykernel, added gunicorn)
- ✅ Updated `.gitignore` to exclude large files
- ✅ Fixed model compatibility issues

### 2. Initialize Git Repository

Open PowerShell in your project directory and run:

```powershell
cd "e:\New Volume\gemstone-price-predictor-main\gemstone-price-predictor-main"
git init
git add .
git commit -m "Initial commit - Gemstone Price Predictor"
```

### 3. Push to GitHub

Create a new repository on GitHub, then:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

### 4. Deploy on Railway

1. **Go to Railway**: https://railway.app
2. **Sign in** with your GitHub account
3. **Click "New Project"**
4. **Select "Deploy from GitHub repo"**
5. **Choose your gemstone-price-predictor repository**
6. **Railway will automatically detect Python and start building**

### 5. Configure Environment Variables (if needed)

In Railway dashboard:
- Click on your project
- Go to "Variables" tab
- Add any environment variables if needed (usually not required for this app)

### 6. Access Your Deployed App

Once deployment completes (takes ~3-5 minutes):
- Railway will provide you with a public URL
- Click the URL to access your gemstone price predictor
- Share it with anyone!

## Important Notes

### Model Files
The model.pkl and preprocessor.pkl are already trained and compatible with the current scikit-learn version. They're included in the artifacts folder.

### Port Configuration
Railway automatically sets the PORT environment variable. The app is configured to use port 8000 by default but Railway will override this.

### Build Process
Railway will:
1. Detect Python from requirements.txt
2. Install all dependencies
3. Run the command from Procfile: `python app.py`

## Troubleshooting

### If build fails:
1. Check Railway logs in the dashboard
2. Verify all files are committed to Git
3. Make sure model files exist in artifacts/

### Common Issues:

**Issue**: Module not found
- **Solution**: Check requirements.txt has all dependencies

**Issue**: Model loading error
- **Solution**: Verify artifacts/model.pkl and artifacts/preprocessor.pkl exist

**Issue**: Port binding error
- **Solution**: Railway handles this automatically, no action needed

## Cost

Railway offers:
- Free tier with $5/month credit
- Pay-as-you-go after that
- This app should run well within free tier limits

## Updating Your Deployment

After making changes:

```powershell
git add .
git commit -m "Your update message"
git push
```

Railway will automatically redeploy when you push to the main branch!

## Alternative: Deploy Without GitHub

You can also deploy directly using Railway CLI:

```powershell
# Install Railway CLI
npm i -g @railway/cli

# Login to Railway
railway login

# Deploy
railway up
```

## Success! 🎉

Your gemstone price predictor is now live on Railway!
