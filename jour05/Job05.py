def decaler_message(message, decalage):
    message_decale = ""
    for lettre in message:
        if lettre.isalpha():
            lettre = lettre.lower()
            lettre_decalee = chr((ord(lettre) - ord('a') + decalage) % 26 + ord('a'))
            message_decale += lettre_decalee
        else:
            message_decale += lettre
    return message_decale

message = "bonjour"
decalage = 3
message_decale = decaler_message(message, decalage)
print(message_decale)