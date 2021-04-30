init:
	test -n "$(name)"
	rm -rf ./.git
	find ./ -type f -exec perl -pi -e 's/bios/$(name)/g' *.* {} \;
	mv ./bios ./$(name)

superuser:
	docker exec -it bios ./manage.py createsuperuser

shell:
	docker exec -it bios ./manage.py shell

makemigrations:
	docker exec -it bios ./manage.py makemigrations

migrate:
	docker exec -it bios ./manage.py migrate

initialfixture:
	docker exec -it bios ./manage.py loaddata initial

testfixture:
	docker exec -it bios ./manage.py loaddata test

test:
	docker exec -it bios ./manage.py test

statics:
	docker exec -it bios ./manage.py collectstatic --noinput

makemessages:
	docker exec -it bios django-admin makemessages

compilemessages:
	docker exec -it bios django-admin compilemessages
