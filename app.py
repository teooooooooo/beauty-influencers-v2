from flask import Flask, render_template, jsonify
from sqlalchemy import text, create_engine

app = Flask(__name__)

db_connection_string = "mysql+pymysql://76ydd3a6dtxdgplnvhzh:pscale_pw_9lfYI1Kk9wOonkGX9Fck9byuRMUhLDMxhvYeyrxAs4f@aws.connect.psdb.cloud/beautyinfluencers?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl":{
      "ssl_ca" : "/etc/ssl/cert.pem"
    } 
  })

def debug_servicii_from_db():
  try:
      with engine.connect() as conn:
          result = conn.execute(text("select * from servicii"))
          rows = result.fetchall()
          print("Number of rows:", len(rows))

          for i, row in enumerate(rows):
              print(f"Row {i}: Type - {type(row)}")
              print(row)
  except Exception as e:
      print(f"An error occurred: {e}")

debug_servicii_from_db()

def load_servicii_from_db():
  servicii = []
  try:
      with engine.connect() as conn:
          result = conn.execute(text("select * from servicii"))
          servicii = [row._asdict() for row in result.fetchall()]
  except Exception as e:
      print(f"An error occurred: {e}")
      # Handle the exception as needed

  # Debug printing of servicii
  print(servicii)
  
  return servicii

  
@app.route("/")
def helo_tello():
  servicii = load_servicii_from_db()
  return render_template('home.html', servicii = servicii, company_name = 'Beauty Influencers')

if __name__ == "__main__":
  app.run(
    host="0.0.0.0",
    debug=True
  )

# @app.route("/api/sevicii")
# def list_jobs():
#   return jsonify(servicii)