from flask import Flask, render_template, jsonify

app = Flask(__name__)

SERVICII = [
  {
    'id': 1,
    'title' : "Manichiura",
    'price' : "70 RON"
  },
  
  {
    'id': 2,
    'title' : "Pedichiura",
    'price' : "60 RON"
  },
  
  {
    'id': 3,
    'title' : "Machiaj",
    'price' : "130 RON"
  },

  {
    'id': 4,
    'title' : "Coafura",
    'price' : "110 RON"
  },

  {
    'id': 5,
    'title' : "Coafura",
    'price' : "110 RON"
  },

  {
    'id': 6,
    'title' : "Tratamente faciale/ corporale",
    'price' : "110 RON"
  },

  {
    'id': 7,
    'title' : "Epilare",
    'price' : "120 RON"
  },

  {
    'id': 8,
    'title' : "Bronzare artificiala",
    'price' : "90 RON"
  },
]

@app.route("/")
def helo_tello():
  return render_template('home.html', servicii = SERVICII, company_name = 'Beauty Influencers')

@app.route("/api/servicii")

def list_jobs():
  return jsonify(SERVICII)

if __name__ == "__main__":
  app.run(
    host="0.0.0.0",
    debug=True
  )
