import re

nombre1 = 'sandra lopez'
nombre2 = 'maria lopez'
nombre3 = 'antonio gomez'
cadena2 = '123154620'
cadena1 = 'a12454b546'
codigo1 = 'kdslafsdhfjkshdfjashfjksd71sdakfsdlfñdsf'
codigo2 = 'sjdfklasjd fsdajfklsdfjdf71 dskljfalsdf'
codigo3 = 'sdkfj dsfajdfk dfkjaskdfjkdf '

if re.search('71', codigo3, re.IGNORECASE):
    print('hemos encontrado el nombre')
else:
    print('no hemos encontrado el nombre')