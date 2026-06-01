# Free Cloud Deployment Guide for Full-Stack AI & Backend Projects

This guide outlines step-by-step instructions for deploying your portfolio applications to free, production-grade cloud hosting services and linking them back to your GitHub repositories.

---

## 🏗️ Deployment Architecture Model

For a complete full-stack project (e.g., frontend, backend, database), the recommended hosting layout is:

```
                  ┌───────────────────────────────┐
                  │      Vercel / Netlify         │
                  │   (Frontend Host — Static)    │
                  └──────────────┬────────────────┘
                                 │
                                 │ HTTPS requests
                                 ▼
                  ┌───────────────────────────────┐
                  │          Render.com           │
                  │     (Backend Host — API)      │
                  └──────┬─────────────────┬──────┘
                         │                 │
            PostgreSQL   │                 │   Redis
            Connection   ▼                 ▼   Connection
        ┌───────────────────┐           ┌───────────────────┐
        │    Neon.tech      │           │   Upstash.com     │
        │ (Serverless SQL)  │           │ (Serverless Redis)│
        └───────────────────┘           └───────────────────┘
```

---

## 🗄️ Phase 1: Provisioning Free Databases

### 1. Serverless PostgreSQL (via [Neon.tech](https://neon.tech/))
Used by: `portfolio-ai-rota-manager`, `healthcare-audit-vault`, `AK_Productions`, `QuestionPaperAI`.
*   **Step 1:** Sign up at [Neon.tech](https://neon.tech/) using your GitHub account (Free Tier provides 1 project with 0.5 GiB storage, which is plenty for portfolios).
*   **Step 2:** Create a new project, choose your region (select closest to your target audience, e.g., US East), and name your database.
*   **Step 3:** Copy the generated Connection String from your dashboard:
    `postgres://alex:PASSWORD@ep-noisy-flower-12345.us-east-2.aws.neon.tech/neondb?sslmode=require`
*   **Step 4 (Local Test):** Update your local `.env` with this connection string and run migrations to test connectivity:
    ```bash
    # Example Node Prisma migration
    DATABASE_URL="postgres://..." npx prisma migrate deploy
    # Example Django migration
    DATABASE_URL="postgres://..." python manage.py migrate
    ```

### 2. Serverless Redis (via [Upstash.com](https://upstash.com/))
Used by: `django-payroll-engine` (as task broker), `agentic-apps-portfolio` (as model router cache).
*   **Step 1:** Sign up at [Upstash](https://upstash.com/) using GitHub. (Free Tier provides 10,000 commands/day).
*   **Step 2:** Create a Redis Database, choose your region, and enable TLS.
*   **Step 3:** Copy the **Redis URL** from the dashboard:
    `rediss://default:PASSWORD@aws-noisy-flower-12345.upstash.io:32311`

---

## 🤖 Phase 2: Deploying Backend APIs (FastAPI, Express, Django)

We recommend using [Render.com](https://render.com/) for backends. The Free Web Service tier spins down after 15 minutes of inactivity, but it is excellent and free for portfolios.

### Step-by-Step Backend Setup on Render:
1.  **Sign Up**: Create an account on [Render](https://render.com/) and link your GitHub account.
2.  **Create New Service**: Click **New +** > **Web Service**.
3.  **Connect GitHub Repo**: Search for and select your repository (e.g., `django-payroll-engine` or `portfolio-ai-rota-manager`).
4.  **Configure Environment**:
    *   **Region**: Same as database (e.g., Oregon or Frankfurt).
    *   **Branch**: `main`.
    *   **Root Directory**: Set this if your backend resides in a subdirectory (e.g., `backend` or leave empty for root projects).
    *   **Runtime**: Select `Python` or `Node`.
5.  **Build & Start Commands**:
    *   *For FastAPI:*
        *   Build Command: `pip install -r requirements.txt`
        *   Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
    *   *For Express (Node):*
        *   Build Command: `npm install`
        *   Start Command: `node dist/index.js` or `npm run start`
    *   *For Django:*
        *   Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
        *   Start Command: `gunicorn payroll_engine.wsgi:application --bind 0.0.0.0:$PORT`
6.  **Add Environment Variables**: Under the **Environment** tab, add your credentials:
    *   `DATABASE_URL` (From Neon)
    *   `REDIS_URL` (From Upstash)
    *   `OPENAI_API_KEY` or `GEMINI_API_KEY`
    *   `PORT` (Automatically provided by Render, but mapped to your start script)
7.  **Deploy**: Render will build the container/package and provision a public URL (e.g., `https://my-payroll-backend.onrender.com`).

---

## 🖥️ Phase 3: Deploying Frontends (Next.js, React/Vite)

Frontends are completely static or serverless-capable, making them perfect for [Vercel](https://vercel.com/) or [Netlify](https://www.netlify.com/). Both deploy instantly and automatically upon every git push.

### Step-by-Step Frontend Setup on Vercel:
1.  **Sign Up**: Create an account on [Vercel](https://vercel.com/) via GitHub.
2.  **Import Project**: Click **Add New** > **Project** and select your repository (e.g., `healthcare-audit-vault` or `akmalkhaniub.github.io`).
3.  **Framework Preset**: Select `Next.js` or `Vite`.
4.  **Root Directory**: Set to `frontend` if it's a sub-directory.
5.  **Environment Variables**: Add your frontend env files.
    *   `NEXT_PUBLIC_API_URL`: Set this to your live Render backend URL (e.g., `https://my-payroll-backend.onrender.com`).
6.  **Deploy**: Vercel compiles the build and assigns a custom URL (e.g., `https://my-payroll.vercel.app`).

---

## 🔗 Linking Deployments to GitHub Repositories

To make it easy for recruiters to review code and visit live demonstrations:

1.  **Add Homepage URL**: Go to your repository settings page on GitHub. In the **About** card on the right-hand side, click the gear icon ⚙️ and paste your live Vercel URL in the **Website** field.
2.  **Highlight in README**: In the top section of your project's `README.md`, add a conspicuous badge linking to your live site:
    ```markdown
    [![Live Demo](https://img.shields.io/badge/Demo-Live_Website-brightgreen?style=for-the-badge)](https://my-app.vercel.app)
    ```
