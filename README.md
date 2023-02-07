
<p align="center">
  <img src="https://res.cloudinary.com/dlxhllkxl/image/upload/v1675091828/tambua_shamba_pdzmu4.png" alt="masomo" width=250>
  <h1 align="center">Tambua Shamba</h1>
  <p align="center">A project to collect and preview soil organic carbon performance in farms across Kenya </p>
</p>


- [Local Development](#local-development)
- [Production environment(WIP)](#production-environmentwip)
- [Developer notes](#developer-notes)
- [Project improvements](#project-improvements)


## Local Development

Copy the environment variables from *.env.example* to *.env.dev*.
```bash
cp .env.example .env.dev
```
To run the project in development mode, run the below at the root:

```bash
docker-compose up 
```

Access the client application on: **[127.0.0.1:4200](127.0.0.1:4200)** and the server-side application on **[127.0.0.1:8000/api/v1/docs](127.0.0.1:8000/api/v1/docs)**

Upload a file from the **test_files** directory to store and render farms onto the map


**To clean up the system**:

```bash
docker-compose down --volumes
```

## Production environment(WIP)

## Developer notes


## Project improvements
- User authentication
- Dynamic location setting