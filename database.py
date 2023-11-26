# from sqlalchemy import create_engine, text

# db_connection_string = "mysql+pymysql://76ydd3a6dtxdgplnvhzh:pscale_pw_9lfYI1Kk9wOonkGX9Fck9byuRMUhLDMxhvYeyrxAs4f@aws.connect.psdb.cloud/beautyinfluencers?charset=utf8mb4"

# engine = create_engine(
#   db_connection_string,
#   connect_args={
#     "ssl":{
#       "ssl_ca" : "/etc/ssl/cert.pem"
#     } 
#   })

# with engine.connect() as conn:
#   result = conn.execute(text("select * from servicii"))
#   print(result.all())