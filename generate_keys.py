import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ['pooya payvar','reza eynolvand','elham ahmadian','Nazanin jabari']
usernames = ['pooya','reza','ahmadian','jabari']
passwords =['6331','5202','5200','4321']

hashed_passwords = [stauth.Hasher([password]).hash()[0] for password in passwords]
print(hashed_passwords)

file_path = Path(__file__).parent / 'hashed_pw.pkl'

with file_path.open('wb') as file:
    pickle.dump(hashed_passwords, file)