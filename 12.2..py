import requests


def hae_saadata(api_avain, kaupunki):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_avain}"
    vastaus = requests.get(url)



    if vastaus.status_code == 200:
        saa_data = vastaus.json()
        return saa_data
    else:
        return None


def kelvin_celsius(temperature_kelvin):
    return temperature_kelvin - 273.15


def main():
    api_avain = "67f8502f72f2be3e63f73211362014ba"
    kaupunki = input("Anna paikkakunnan nimi: ")

    saa_data = hae_saadata(api_avain, kaupunki)

    if saa_data:
        saa_kuvaus = saa_data["weather"][0]["description"]
        lampotila_kelvin = saa_data["main"]["temp"]

        lampotila_celsius = kelvin_celsius(lampotila_kelvin)

        print(f"Sää paikkakunnalla {kaupunki}: {saa_kuvaus}")
        print(f"Lämpötila: {lampotila_celsius:.2f} °C")
    else:
        print("Säätietoja ei saatu. Tarkista kaupungin nimi tai API-avain.")


if __name__ == "__main__":
    main()
