# #!/bin/bash

# echo "**********Building NoteBook Project*********"
# python3.12 -m pip install -r requirements.txt

# echo "**********Make Migrations***************"
# python3.12 manage.py makemigrations --noinput
# python3.12 manage.py migrate --noinput

# echo "******Collect Static*********"
# python3.12 manage.py collectstatic --noinput --clear
# {
#   "builds": [
#     {
#       "src": "notebook/wsgi.py",
#       "use": "@vercel/python",
#       "config": {
#         "maxLambdaSize": "15mb",
#         "runtime": "python3.12"
#       }
#     },
#     // {
#     //     "src":"build_files.sh",
#     //     "use":"@vercel/static-build",
#     //     "config":{
#     //         "distDir":"staticfiles"
#     //     }
#     // }
#   ],
#   "routes": [
#     {
#       "src": "/static/(.*)",
#       "dest": "/static/$1"
#     },
#     {
#       "src": "/(.*)",
#       "dest": "notebook/wsgi.py"
#     }
#   ]
# }
