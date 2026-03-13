import requests
import time


def Passing_parameters_in_URL():
    print("Lession_one: GET with Params")
    url_1 = "https://httpbin.org/get"

    search_fileters = {"student_name": "Kavinda",
                       "university": "OUSL",
                       "skill": "python"
                       }
    responce_1 = requests.get(url_1, params=search_fileters)
    print(f"Created_URL: {responce_1.url}")


start_time = time.perf_counter()
Passing_parameters_in_URL()
end_time = time.perf_counter()

print(f"Execution Time: {end_time - start_time:.4f} seconds")


def binary_response():
    print("Lession_two: Binary Response Content")
    url_2 = "https://httpbin.org/image/png"

    try:
        responce_2 = requests.get(url_2)
        if responce_2.status_code == 200:
            with open("test_image.png", "wb") as file:
                file.write(responce_2.content)

            print("Image downloaded successfully.")

    except Exception as e:
        print(f"An error occurres: {e}")


binary_response()


def json_response():
    print("Lession_three: Json Response Content")
    url_3 = "https://jsonplaceholder.typicode.com/users/1"

    try:
        response_3 = requests.get(url_3)
        if response_3.status_code == 200:
            data = response_3.json()
            print("----My data----")
            print(data)

    except Exception as e:
        print(f"An error occurres: {e}")


json_response()
