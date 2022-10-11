from application import app
## this is 
if __name__ == "__main__":
    print("here")
    # db.create_all()
    app.run(port=5000, debug=True, host='0.0.0.0')
    