# Mobridge

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

> **Bridging the gap between Employers and Talent through Agency-curated recruitment.**

## Demo / Screenshots

![App Screenshot](./path-to-screenshot.png)

## Table of Contents

- [About the Project](#-about-the-project)
- [Tech Stack](#-tech-stack)
- [Key Features](#-key-features)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [Roadmap](#-roadmap)
- [Contact](#-contact)

## 📖 About Mobridge

Mobridge is a specialized recruitment platform designed to streamline the hiring process by introducing a **verified Agency layer**. Unlike standard job boards where employers are flooded with unfiltered applications, Mobridge empowers recruitment agencies to screen, filter, and match the best candidates to specific job openings.

This project was built to demonstrate advanced Full Stack development skills, specifically focusing on multi-user role architecture (Employer, Agency, Applicant) and complex data relationships.

## Tech Stack

**Client:**

- React
- Vite
- TypeScript
- Tailwind CSS
- TanStack (for forms)

**Server:**

- Django
- Django REST Framework
- SQLite (default, can use PostgreSQL)

**DevOps/Tools:**

- Git
- Docker (optional)
- ESLint
- Vite
- npm

## Key Features

- **Multi-Role Authentication:** distinct portals and permissions for Agencies, Employers, and Applicants.
- **Smart Filtering:** Tools for agencies to sort candidates based on skills, willingness to work, and verification status.
- **Document Generation:** Automated rendering of contracts and resume summaries (DOCX/PDF) directly from database records.
- **Application Tracking:** Kanban-style or list-view tracking of a candidate's journey from "Applied" to "Hired."

## Project Structure

This repository is organized as a monorepo:

```
client/      # Frontend (React, Vite, TypeScript)
server/      # Backend (Django)
	core/      # Core mixins and utilities
	domains/   # Modular app domains (account, contact, education, employer, job, work_experience)
	web/       # Django project settings and entry points
```

## Getting Started

### Prerequisites

- Node.js & npm (for client)
- Python 3.10+ (for server)
- pip (Python package manager)

### Setup

#### 1. Clone the repository

```powershell
git clone https://github.com/mourey-dev/mobridge.git
cd mobridge
```

#### 2. Install client dependencies

```powershell
cd client
npm install
```

#### 3. Install server dependencies

```powershell
cd ../server
pip install -r requirements.txt
```

#### 4. Run database migrations

```powershell
python manage.py migrate
```

#### 5. Start the development servers

- **Client:**
  ```powershell
  cd client
  npm run dev
  ```
- **Server:**
  ```powershell
  cd server
  python manage.py runserver
  ```

## Usage

- Access the frontend at `http://localhost:5173` (default Vite port)
- Access the backend API at `http://localhost:8000`

## Environment Variables

### Client

Create a `.env` file in the `client/` directory. Example:

```env
VITE_API_URL=http://localhost:8000
```

### Server

Create a `.env` file in the `server/` directory if needed for secrets or environment-specific settings.

## Roadmap

- [ ] Add more user roles and permissions
- [ ] Integrate third-party job boards
- [ ] Improve UI/UX for candidate tracking
- [ ] Add automated testing and CI/CD

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## Contact

For questions or support, please open an issue on [GitHub](https://github.com/mourey-dev/mobridge/issues) or contact pantanosasmoureyjames@gmail.com.

## License

MIT
