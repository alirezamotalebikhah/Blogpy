# Blogpy - Django Blog Application

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-2.2+-green.svg)](https://djangoproject.com)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://docker.com)
[![Nginx](https://img.shields.io/badge/Nginx-Web%20Server-green.svg)](https://nginx.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)](https://postgresql.org)
[![YouTube](https://img.shields.io/badge/YouTube-Tutorial%20Series-red.svg)](https://www.youtube.com/watch?v=5SXtOyOhk9M&list=PLGlWjLcdLyGyqEqh9rBQ-9toPsFeHWrMr)

A modern Django blog application built for training purposes, following the excellent tutorials by [Bobby Babazadeh](https://github.com/BobbyBabazadeh).

## Overview

This project implements a full-featured blog system using Django, PostgreSQL, and Docker containerization. Built as a learning exercise to practice Django development and modern deployment techniques.

## Features

- Complete blog functionality (create, read, update, delete posts)
- User authentication and management
- Responsive web interface
- Docker containerization with Nginx, Django, and PostgreSQL
- RESTful API endpoints

## Quick Start

### Prerequisites
- Docker and Docker Compose

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/alirezamotalebikhah/Blogpy.git
   cd Blogpy
   ```

2. **Create Docker volumes**
   ```bash
   docker volume create blogpy_postgresql
   docker volume create blogpy_static_volume
   docker volume create blogpy_files_volume
   ```

3. **Create Docker networks**
   ```bash
   docker network create nginx_network
   docker network create blogpy_network
   ```

4. **Environment configuration**
   
   Create `.env` file in project root:
   ```env
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_DB=postgres
   ```

5. **Launch services**
   ```bash
   # Start Django and PostgreSQL
   docker-compose up -d
   
   # Start Nginx
   docker-compose -f nginx/docker-compose.yml up -d
   ```

6. **Access the application**
   
   Navigate to `http://localhost`

## Architecture

The application runs on three Docker containers:
- **Nginx** (Port 80) - Web server and reverse proxy
- **Django** (Port 8000) - Main application
- **PostgreSQL** (Port 5432) - Database




## Acknowledgments

This project was created for training purposes following the Django tutorial series by **Bobby Babazadeh**.

📺 **Tutorial Series**: [Complete Django Course for Beginners](https://www.youtube.com/watch?v=5SXtOyOhk9M&list=PLGlWjLcdLyGyqEqh9rBQ-9toPsFeHWrMr)

All credit for the original project concept and tutorials goes to Bobby Babazadeh. 
