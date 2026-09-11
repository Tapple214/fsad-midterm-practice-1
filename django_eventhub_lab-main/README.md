# Django EventHub Lab

A new Django application for practicing Models, ORM, Views, Templates, Authentication, Authorization, Groups, Permissions, Docker, and Docker Compose.

**Important:** This is a student lab. The application contains `# TODO:` / `<!-- TODO: -->` instructions that students must complete.

Run:
```bash
docker compose up --build
```

Then:
```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

Open http://localhost:8000/

Search for `# TODO:` to find the tasks.
