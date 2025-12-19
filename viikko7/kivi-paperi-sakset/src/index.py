from kps import luo_peli

def ohje():
    print("Valitse pelataanko"
        "\n (a) Ihmistä vastaan"
        "\n (b) Tekoälyä vastaan"
        "\n (c) Parannettua tekoälyä vastaan"
        "\nMuilla valinnoilla lopetetaan"
        )

def main():
    ohje()
    vastaus = input()
    while vastaus in "abc":
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )
        peli = luo_peli(vastaus)
        peli.pelaa()
        ohje()
        vastaus = input()
        
if __name__ == "__main__":
    main()
