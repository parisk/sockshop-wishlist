PORT?=8000

migrate:
	python wishlist/manage.py migrate

dev: migrate
	python wishlist/manage.py runserver 0.0.0.0:${PORT}
