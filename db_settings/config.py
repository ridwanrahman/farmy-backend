from decouple import config

USERNAME = config("USERNAME")
IP_ADDRESS = config("IP_ADDRESS")
PORT = config("PORT")
DATABASE_NAME = config("DATABASE_NAME")

# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"

DATABASE_URI = f"postgres+psycopg2://{USERNAME}:@{IP_ADDRESS}:{PORT}/{DATABASE_NAME}"
