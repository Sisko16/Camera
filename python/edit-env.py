'''
Edit "dash.env": Set FIREBASE_CONFIG to 'fire-base-config.json' 
"dash.env" will be renamed to "camera.env" by the setup.sh script
'''
import sys
path = sys.argv[1]
   
with open ('dash.env', "a") as file:
    file.write(f"\nFIREBASE_CONFIG={path}/firebase-config.json")