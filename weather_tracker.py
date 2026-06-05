import requests

def get_weather(city_name):
    # একটি ফ্রি ও পাবলিক API কী (পরীক্ষা করার জন্য)
    api_key = "b35565862c0411d3b340c31ec696ed47" 
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # API-তে পাঠানোর জন্য প্যারামিটার (শহরের নাম, কী, এবং সেলসিয়াস ইউনিটের জন্য metric)
    parameters = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=parameters)
        data = response.json()
        
        # যদি শহরটি খুঁজে পাওয়া যায় (স্ট্যাটাস কোড ২০০)
        if response.status_code == 200:
            main_data = data['main']
            weather_desc = data['weather'][0]['description']
            wind_data = data['wind']
            
            print(f"\n--- {city_name.upper()} এর আবহাওয়ার খবর ---")
            print(f"তাপমাত্রা: {main_data['temp']}°C")
            print(f"অনুভূত হচ্ছে (Feels like): {main_data['feels_like']}°C")
            print(f"আর্দ্রতা (Humidity): {main_data['humidity']}%")
            print(f"আকাশের অবস্থা: {weather_desc.capitalize()}")
            print(f"বাতাসের গতিবেগ: {wind_data['speed']} m/s")
        else:
            print("\nশহরের নামটি সঠিক নয় অথবা ডেটা পাওয়া যায়নি!")
            
    except Exception as e:
        print("\nইন্টারনেট কানেকশন চেক করুন অথবা আবার চেষ্টা করুন।")

# মেইন প্রোগ্রাম
if __name__ == "__main__":
    city = input("যেকোনো শহরের নাম ইংরেজিতে লিখুন (যেমন: Dhaka, London): ")
    get_weather(city)
