# run_localdrive.py
from localdrive.localdrive import app

if __name__ == '__main__':
    app.run(port=5001, debug=True)