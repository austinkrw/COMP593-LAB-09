import requests
import ctypes

def getPokeDic(pokeName):
    """
    Gets information for a specified pokemon and returns it in a dictionary
    :param name: pokemons name or index #
    """

    print("Connecting to PokeAPI . . .", end = "")
    # makes a get request to PokeAPI for a specified pokemon 
    req = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokeName)
    # if retrieval/connection was successful return the information in a dictionary
    if req.status_code == 200:
        print(' Success!')
        return req.json()
    else:
        print(' Error', sep = "")

def getPokeList(limit=1126, offset=0):
    """
    Gets a list of pokemon names by specyfing a range or using a default range
    :param limit: range end index (max 1126)
    :param offset: range start index
    """

    print("Getting list of pokemon...", end="")
    URL = "https://pokeapi.co/api/v2/pokemon/"

    # sets parameters from the function to parameters for the get request
    parameters = {"limit": limit, "offset": offset}
    # makes a get request to PokeAPI
    req = requests.get(URL, params=parameters)
    # if retrieval/connection was successful return the name of each pokemon in a list
    if req.status_code == 200:
        print(" Success!")
        poke_dict = req.json()
        poke_list = []
        for i in poke_dict["results"]:
            poke_list.append(i["name"])
        return poke_list
    else:
        print(" Error. Resonse code: ", req.status_code)

def getPokeImgUrl(name):
    """
    Retrieves an image URL for a pokemon
    :param name: name of the pokemon to retrieve the image URL for
    """

    # retrieves pokemon information in a dictionary from the getPokeDic function
    poke_dict = getPokeDic(name)
    # if the dictionary is retrieved successfully retrieve the image URL and return it
    if poke_dict:
        poke_url = poke_dict["sprites"]["other"]["official-artwork"]["front_default"]
        return poke_url

def downloadPokeImg(URL, path):
    """
    Downloads an image from the image URL to a local path
    :param URL: image URL of pokemon
    :param pathh: path to where the pokemon image should be saved
    """

    print("Download image... ", end= "")
    # makes a get request to the image URL
    req = requests.get(URL)
    # if retrieval/connection is successful save the image locally
    if req.status_code == 200:
        with open(path, "wb") as handle:
            handle.write(req.content)
        print("Success!")
    else:
        print("Error. Response code: ", req.status_code)

def setDsktpBckgrndImg(path):
    """
    Sets the desktop background to a specified image
    :param path: path to image going to be set as desktop background
    """
    # Sets desktop background image to picture located at "path"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)