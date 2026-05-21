#!/usr/bin/env python3
"""
Google Colab GitHub Repository Setup Script
This script helps you clone and configure your GitHub repository in Google Colab
"""

import subprocess
import os
from google.colab import userdata

def setup_github_repo(repo_url, user_email, user_name):
    """
    Setup GitHub repository in Google Colab
    
    Args:
        repo_url: Your GitHub repository URL (e.g., https://github.com/username/repo-name.git)
        user_email: Your GitHub email
        user_name: Your GitHub username
    """
    
    print("🚀 Starting GitHub Repository Setup...\n")
    
    # Step 1: Get GitHub Token from Secrets
    print("Step 1️⃣: Getting GitHub Token...")
    try:
        github_token = userdata.get('GITHUB_TOKEN')
        print("✅ Token retrieved successfully!\n")
    except Exception as e:
        print(f"❌ Error: Could not get token. Make sure you added GITHUB_TOKEN to Secrets")
        print(f"Error details: {e}\n")
        return False
    
    # Step 2: Clone Repository
    print("Step 2️⃣: Cloning repository...")
    try:
        # Extract repo name from URL
        repo_name = repo_url.split('/')[-1].replace('.git', '')
        
        # Clone with authentication
        clone_url = repo_url.replace('https://', f'https://{github_token}@')
        subprocess.run(['git', 'clone', clone_url], check=True)
        print(f"✅ Repository cloned: {repo_name}\n")
    except Exception as e:
        print(f"❌ Error cloning repository: {e}\n")
        return False
    
    # Step 3: Configure Git
    print("Step 3️⃣: Configuring Git...")
    try:
        subprocess.run(['git', 'config', '--global', 'user.email', user_email], check=True)
        subprocess.run(['git', 'config', '--global', 'user.name', user_name], check=True)
        print("✅ Git configured successfully!\n")
    except Exception as e:
        print(f"❌ Error configuring Git: {e}\n")
        return False
    
    # Step 4: Navigate to repo
    print("Step 4️⃣: Entering repository directory...")
    try:
        os.chdir(repo_name)
        print(f"✅ Now in {repo_name} directory\n")
    except Exception as e:
        print(f"❌ Error changing directory: {e}\n")
        return False
    
    print("🎉 Setup Complete! You can now work with your repository.")
    print("\nCommon commands:")
    print("  !git status          - Check changes")
    print("  !git add .           - Stage all changes")
    print("  !git commit -m 'msg' - Commit changes")
    print("  !git push            - Push to GitHub")
    
    return True


if __name__ == "__main__":
    # Configuration - CHANGE THESE VALUES
    REPO_URL = "https://github.com/gayathribommidi09/repo-1.git"
    USER_EMAIL = "your-email@gmail.com"  # Change this
    USER_NAME = "Your Name"               # Change this
    
    # Run setup
    setup_github_repo(REPO_URL, USER_EMAIL, USER_NAME)
