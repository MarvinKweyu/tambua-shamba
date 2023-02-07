# TambuaShamba - Client

> A project to collect and preview soil organic carbon performance in farms across Kenya 

Preview SVG

- [TambuaShamba - Client](#tambuashamba---client)
  - [Local setup](#local-setup)
    - [Manual](#manual)
    - [Docker](#docker)
  - [Project Improvements](#project-improvements)
  - [Production ready(WIP)](#production-readywip)

## Local setup

**Assumptions:**
The SoilCarbon frontend application assumes you are running the backend
application on `127.0.0.1:8000`.

### Manual

**Basic requirements**

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 14.2.2
At the project's root directory:

```bash
npm install
ng serve
```

Navigate to `http://localhost:4200/`

### Docker

**Basic requirements**

- Docker

On the project root, run the below

```bash
docker build -t soilcarbonfrontend .
docker run -d -p 4200:80 soilcarbonfrontend
```

Navigate to `http://localhost:4200/`

## Project Improvements

- Download a file previously uploaded
- Paginate the files listed
- List and search for farms accepted under a specific file uploaded
- Search for a file by title or filter by date
- Search for a farm from the home page. The user should be able to zoom in on a farm with the name searched.

## Production ready(WIP)

To make this application production ready, one can choose from the choice of the below:

- Use a static site generator: **Netlify** or **Vercel**

In either instance, the _environment variables_ would need to be palced outside the code
files.
