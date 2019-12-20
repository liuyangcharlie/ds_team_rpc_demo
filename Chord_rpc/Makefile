# install python dependencies
install:
	sh ./build.sh

# set up docker dev environment, bind port, share working directory
start_docker:
	# name should be like node1, node2
	#  -d, --detach Run container in background and print container ID
	docker run -d --publish=$(port):8080 --name=$(name) -it -v ~/Documents/GWU/Code/distributed_system:/home/c/ds_team_proj_chord_dev liuyangc/gwu_ds_chord:latest /bin/bash -c "/etc/rc.d/rc.local;"

# run web application
run:
	python3 ./manage.py runserver
