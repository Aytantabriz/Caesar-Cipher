logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
#Sonuncu hərflərə çatanda irəli gedə bilmək üçün hərfləri sona kopyalıyır.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction): #3 value daxil ediləcək caesar() funksiya yaradırıq
  end_text = "" #sonda nəticəmiz olacaq mətn
  
  if cipher_direction == "decode": # əgər decode seçilərsə geriyə doğru hərfləri sıralasın, əgər deyilsə davam etsin.
    shift_amount *= -1
    
  for char in start_text: #daxil etdiyimiz sözdəki hərflərini müəyyənləşdirsin.
    # Hərf daxil edilibsə
    if char in alphabet: # əgər hərf kimi daxil edilibdirsə, 
      position = alphabet.index(char) # daxil edilən hərfin indexini müəyyənlişdirsin
      new_position = position + shift_amount # indeksin üzərinə shifti gəlsin.
      end_text += alphabet[new_position] # alınan yeni hərfi end_textə əlavə etsin.
    else:
    # Rəqəm və Simvol daxil edilibsə
      end_text += char # əgər simvol və rəqəm əlavə edilibsə, mətnin indeksində dəyişiklik etmədən olduğu kimi end_textə əlavə etsin
  print(f"Here's the {cipher_direction}d result: {end_text}")

#from art import logo
print(logo)


# Əməliyyatı davam etdirsinmi?
should_end = False
while not should_end: # should_end=True olanadək loopu davam etdir.

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  # Əlifbadakı rəqəmlərin sayından çox shift əlavə edilərsə, hərflərin sayına (26) bölürük 
  # və qalıq bizim indeksimiz olacaq. 
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True # Loopu bağlayır.
    print("Goodbye")