import lib.googleBot as GoogleBot


if __name__ == '__main__':

    robo = GoogleBot.GoogleSearchBot("facebook.com", [
        "casa em vinhedo",
        "aluguel em vinhedo",
        "casas em vinhedo",
        "comprar casa em vinhedo",
        "comprar casas em vinhedo",
        "comprar casa em louveira"
    ], maxPages=10)

    robo.execute()
