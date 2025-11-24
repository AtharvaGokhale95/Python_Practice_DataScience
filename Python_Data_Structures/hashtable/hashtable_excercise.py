weather_dict = {}

with open("/Users/atharva/Documents/GitHub/Python_Pratice_DataScience/Python_Data_Structures/data/nyc_weather.csv", "r") as file:
    for line in file:
        tokens = line.split(",")
        day = tokens[0]
        try:
            temperature = int(tokens[1])        # This automatically handles the column headers by not inserting them in dict
            weather_dict[day] = temperature
        except:
            print("Invalid value. Ignore the row")
    

# if __name__ == "__main__":
#     print(weather_dict)
    
#     #Temperature on Jan 09
#     print(weather_dict['Jan 9'])
    
#     # Temperature on Jan 04
#     print(weather_dict['Jan 4'])
    

word_count = {}

with open("/Users/atharva/Documents/GitHub/Python_Pratice_DataScience/Python_Data_Structures/data/poem.txt", "r") as file:
    for line in file:
        tokens = line.split(" ")
        for token in tokens:
            token = token.replace('\n','')
            if token in word_count:
                word_count[token] += 1
            else:
                word_count[token] = 1

if __name__ == "__main__":
    print(word_count)
    
    