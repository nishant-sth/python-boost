def validate_password(password):
    if len(password)<8:
        return False
    
    #check at least one Uppercase in password
    if not any(char.isupper() for char in password ):
        return False
    
    #check at least one number
    if not any(char.isdigit() for char in password):
        return False
    
    return True

passwords = {
    'nsihanr2929',
    '2829Thak',
    '777777',
    'NISGANATTQ',
    '22abakT@!',
    '277gdgTT'
}

for psw in passwords:
    result = validate_password(psw)
    print(f'Password:{psw}  Valid:{result}')
