import requests


def hae_chuck_norris_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    vastaus = requests.get(url)

    if vastaus.status_code == 200:
        vitsi_data = vastaus.json()
        vitsi = vitsi_data["value"]
        return vitsi
    else:
        return None


def main():
    chuck_norris_vitsi = hae_chuck_norris_vitsi()

    if chuck_norris_vitsi:
        print("Chuck Norris sanoo:")
        print(chuck_norris_vitsi)
    else:
        print("Vitsin hakemisessa tapahtui virhe.")


if __name__ == "__main__":
    main()
