import requests
import time
import shutil


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
# Passing_parameters_in_URL()
end_time = time.perf_counter()

# print(f"Execution Time: {end_time - start_time:.4f} seconds")


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


# binary_response()


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


# json_response()


def raw_response():
    print("Lession_four: raw content response")
    url_4 = "https://httpbin.org/image/png"
    try:
        response_4 = requests.get(url_4, stream=True)
        if response_4.status_code == 200:

            with open("raw_image.png", "wb") as file:
                response_4.raw.decode_content = True
                shutil.copyfileobj(response_4.raw, file)
            print("Image downloaded successfully.")

            print("First 10 raw byte:", response_4.raw.read(10))

    except Exception as e:
        print(f"An error occurres: {e}")


# raw_response()


def response_content():
    print("Lession_five: Response Content")
    url_5 = "https://httpbin.org/get"

    try:
        response_5 = requests.get(url_5)
        if response_5.status_code == 200:
            print(response_5.text[:200])

    except Exception as e:
        print(f"An error occurres: {e}")


# response_content()


def custom_headers():
    print("Lession_six: custom headers")
    url_6 = "https://httpbin.org/headers"

    security_badge = {"Authorization": "Bearer TAPS_SUPER_SECRET_KEY_999"}
    respose_6 = requests.get(url_6, headers=security_badge)

    try:
        if respose_6.status_code == 200:
            print("✅ Access Granted! The security guard saw these headers:")
            server_data = respose_6.json()
            print(server_data["headers"])
        else:
            print("❌ Access Denied.")

    except Exception as e:
        print(f"An error occurres: {e}")


custom_headers()
