meme_dict = {
            "cringe": "Qualcosa di eccezionalmente strano o imbarazzante",
            "lol": "Una risposta comune a qualcosa di divertente",
            "sheesh":"leggera disapprovazione",
            "creepy":"spaventoso,inquietante"
            }
while True:
    parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!):\n\n")
    if parola.lower() in meme_dict.keys():
        print("\n",meme_dict[parola.lower()],"\n\n")
    else:
        print("parola non trovata, prova a riscriverla in maiscolo")
