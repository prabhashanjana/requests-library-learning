import requests


def Passing_parameters_in_URL():
    print("Lession_one: GET with Params")
    url_1 = "https://httpbin.org/get"

    search_fileters = {"student_name": "Kavinda",
                       "university": "OUSL",
                       "skill": "python"
                       }
    responce_1 = requests.get(url_1, params=search_fileters)
    print(f"Created_URL: {responce_1.url}")


Passing_parameters_in_URL()
