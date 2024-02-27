from flask import Flask,render_template


app= Flask (__name__)
JOBS= [
  {
    'id':1,
    'title': 'Data Analyst',
    'location': 'Banglore,India',
    'salary': 'RS.10,00,000'
  },
  {
    'id':2,
    'title': 'Data Scientist',
    'location': 'New Delhi,India',
    'salary': 'RS.15,00,000'
  },
  {
    'id':3,
    'title': 'Frontend Developer',
    'location': 'Remote',
  },
  {
    'id':4,
    'title': 'Backend Developer',
    'location': 'Jaipur,India',
    'salary': 'RS.19,00,000'
  }
]



@app.route('/')
def hello_world():
  return render_template('home.html',
                         jobs=JOBS,
                        company_name='Haribaksh')

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=True)