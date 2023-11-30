# API-for-Weather-Forecast

![weather](https://github.com/renu5555/API-for-Weather-Forecast/assets/139370797/37026028-136a-4869-bc46-061c5271b304)

# Weather API with Flask

A weather API based on a simple design with Flask lets its consumers get information on what is the weather now in several cities. Acquiring of the weather data from OpenWeatherMap API.

## Prerequisites

- Python
- Flask
- Requests library

## Getting Started

1.Install the required libraries.

2.Get your OpenWeatherMap API key.

3.Run the application.

4.Open Postman and create a new request to http: //127.0.0.1:5000/weather with the GET method.

5.Add a query param location with the value being the city and state (eg: Bengaluru, KA).

6.Submit the request and verify the response.

Note: Comparing it with OpenWeatherMap will help you determine whether this returned data is correct.

## Detailed Explanation

1.Execute the python script in VSCode.

2.In the terminal you can see the base url http: //127.0.0.1:5000. On clicking this url, you will see 404 error.

3.Go now on to your post man workspace and set the request type as GET.

4.Enter the URL for your Flask API endpoint i.e, http: //127.0.0.1:5000/weather?.

5.Click on the "Params" tab. In the “Key” section write down location. For retrieving the weather information of the city and state (e.g., Chicago-IL), provide it in the “Value” column.

6.Press the send key to send for this request.

7.Now go back to the base url, inorder to fetch the weather data, you have to append the base url with the api endpoint i.e, http: //127.0.0.1:5000/weather?location=city,state (eg: http://127.0.0.1:5000/weather?location=Bengaluru, Karnataka&location=Mysore, Karnataka).

8.See now, how the JSON file appears here.

## Usage
Ensure the server is running. To retrieve weather information, make a GET request to the /api/weather endpoint with the city parameter.

## API Endpoint
/api/weather: Get weather information for a specific city.

Parameters: city (required): The name of the city for which you want weather information.

Example: curl http://127.0.0.1:5000/weather?location=Bengaluru, Karnataka&location=Mysore, Karnataka

## Configuration
To use this project, you need to obtain an API key from OpenWeatherMap and update the configuration.

Search for OPENWEATHERMAP_API_KEY in the code.
Replace the Key with your actual OpenWeatherMap API key.

## Contributing
Contributions are welcome! If you find any issues or have suggestions, please open an issue or submit a pull request.

##   Screenshots
![a](https://github.com/renu5555/API-for-Weather-Forecast/assets/139370797/0daa8d02-d2cb-42a2-be8c-03df6e5fc7c9)
![b](https://github.com/renu5555/API-for-Weather-Forecast/assets/139370797/bbdc7db3-4438-4071-801a-f4a20527918b)
![C](https://github.com/renu5555/API-for-Weather-Forecast/assets/139370797/eb0dd45a-8480-456c-b79e-333318b211ef)
![last](https://github.com/renu5555/API-for-Weather-Forecast/assets/139370797/5c193fdc-f6ab-448c-b9ed-52f7b3cb8520)
![postman2](https://github.com/renu5555/API-for-Weather-Forecast/assets/139370797/59b0a6fc-7180-48ea-8c70-87db3ab2401b)
