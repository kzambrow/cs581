# Author: Kamil Zambrowski 10428741
# I Pledge My Honor That I Have Abided By The Stevens Honor System

# To run the program, type into console: python FB_data.py
# Then when prompted for a file name, input the file name containing the csv file for Facebook data

# This program will take a csv file as input, then parse through to take out the user's age, mobile likes, and website likes.
# The users will be put into groups based on age ranges, and the program will keep track and increment those age ranges to be displayed later
# For each age range, it will also keep track of how many likes have been made through the mobile app and through the website
# It will analyze the percentage of these likes in terms of how they were made.
# It will print all of this information into tabular form
# Afterwards, it will take the proportion of ages to be displayed in a pie chart, as well as all the like proportions for each age range
# So for each age range, we will see the proportion of mobile and website likes in the form of a pie chart.
# The purpose of this is to analyze how different age groups use the social media, as well as how many users from each age group use the social media.
import matplotlib
import matplotlib.pyplot as plt
from tabulate import tabulate
import csv

# This function wil take in a file name that contains a csv file
# It will parse through the data and take out the relevent information and put it into tabular form
# It will also display pie charts to visualize the proportions
def FB_data(file_name):
    #establish the columns we are interesting in
    # [Age, mobile_likes, www_likes]
    col_list = [1,11,13]
    #initialize the age ranges and their like counts
    #range 13-17
    age_13_17 = 0
    mobile_age_13_17 = 0
    www_age_13_17 = 0
    #range 18-24
    age_18_24 = 0
    mobile_age_18_24 = 0
    www_age_18_24 = 0
    #range 25-34
    age_25_34 = 0
    mobile_age_25_34 = 0
    www_age_25_34 = 0
    #range 35-44
    age_35_44 = 0
    mobile_age_35_44 = 0
    www_age_35_44 = 0
    #range 45-54
    age_45_54 = 0
    mobile_age_45_54 = 0
    www_age_45_54 = 0
    #range 55-64
    age_55_64 = 0
    mobile_age_55_64 = 0
    www_age_55_64 = 0
    #range 65-74
    age_65_74 = 0
    mobile_age_65_74 = 0
    www_age_65_74 = 0
    #75 years and older
    age_75 = 0
    mobile_age_75 = 0
    www_age_75 = 0


    # read fom the csv file
    with open(file_name, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        #skip first row (header)
        next(csvreader)
        # each row in the csv file
        for row in csvreader:
            content = list(row[i] for i in col_list)
            temp_age_str = content[0]
            temp_age = int(temp_age_str)
            #increment the values when they correspeond to the correct age range
            #also increment the likes within that age range when they correspond to either mobile or website likes
            if (temp_age >= 13) and (temp_age <= 17):
                age_13_17 += 1
                mobile_age_13_17 += int(content[1])
                www_age_13_17 += int(content[2])
            if (temp_age >= 18) and (temp_age <= 24):
                age_18_24 += 1
                mobile_age_18_24 += int(content[1])
                www_age_18_24 += int(content[2])
            if (temp_age >= 25) and (temp_age <= 34):
                age_25_34 += 1
                mobile_age_25_34 += int(content[1])
                www_age_25_34 += int(content[2])
            if (temp_age >= 35) and (temp_age <= 44):
                age_35_44 += 1
                mobile_age_35_44 += int(content[1])
                www_age_35_44 += int(content[2])
            if (temp_age >= 45) and (temp_age <= 54):
                age_45_54 += 1
                mobile_age_45_54 += int(content[1])
                www_age_45_54 += int(content[2])
            if (temp_age >= 55) and (temp_age <= 64):
                age_55_64 += 1
                mobile_age_55_64 += int(content[1])
                www_age_55_64 += int(content[2])
            if (temp_age >= 65) and (temp_age <= 74):
                age_65_74 += 1
                mobile_age_65_74 += int(content[1])
                www_age_65_74 += int(content[2])
            if (temp_age >= 75):
                age_75 += 1
                mobile_age_75 += int(content[1])
                www_age_75 += int(content[2])
    #Total users
    total_users = age_13_17 + age_18_24 + age_25_34 + age_35_44 + age_45_54 + age_55_64 + age_65_74 + age_75
    #Percentage of Users for each age group
    user_percent_13_17 = round((100*age_13_17/total_users),2)
    user_percent_18_24 = round((100*age_18_24/total_users),2)
    user_percent_25_34 = round((100*age_25_34/total_users),2)
    user_percent_35_44 = round((100*age_35_44/total_users),2)
    user_percent_45_54 = round((100*age_45_54/total_users),2)
    user_percent_55_64 = round((100*age_55_64/total_users),2)
    user_percent_65_74 = round((100*age_65_74/total_users),2)
    user_percent_75 = round((100*age_75/total_users),2)
    #Total Likes for each age group
    likes_13_17 = mobile_age_13_17 + www_age_13_17
    likes_18_24 = mobile_age_18_24 + www_age_18_24
    likes_25_34 = mobile_age_25_34 + www_age_25_34
    likes_35_44 = mobile_age_35_44 + www_age_35_44
    likes_45_54 = mobile_age_45_54 + www_age_45_54
    likes_55_64 = mobile_age_55_64 + www_age_55_64
    likes_65_74 = mobile_age_65_74 + www_age_65_74
    likes_75 = mobile_age_75 + www_age_75
    #Percentages of mobile likes for each age group
    mobile_percent_13_17 = round((100*mobile_age_13_17/likes_13_17),2)
    mobile_percent_18_24 = round((100*mobile_age_18_24/likes_18_24),2)
    mobile_percent_25_34 = round((100*mobile_age_25_34/likes_25_34),2)
    mobile_percent_35_44 = round((100*mobile_age_35_44/likes_35_44),2)
    mobile_percent_45_54 = round((100*mobile_age_45_54/likes_45_54),2)
    mobile_percent_55_64 = round((100*mobile_age_55_64/likes_55_64),2)
    mobile_percent_65_74 = round((100*mobile_age_65_74/likes_65_74),2)
    mobile_percent_75 = round((100*mobile_age_75/likes_75),2)
    #Percentages of website likes for each age group
    www_percent_13_17 = round((100*www_age_13_17/likes_13_17),2)
    www_percent_18_24 = round((100*www_age_18_24/likes_18_24),2)
    www_percent_25_34 = round((100*www_age_25_34/likes_25_34),2)
    www_percent_35_44 = round((100*www_age_35_44/likes_35_44),2)
    www_percent_45_54 = round((100*www_age_45_54/likes_45_54),2)
    www_percent_55_64 = round((100*www_age_55_64/likes_55_64),2)
    www_percent_65_74 = round((100*www_age_65_74/likes_65_74),2)
    www_percent_75 = round((100*www_age_75/likes_75),2)
    #tabular print out to console of interpreted data
    table = tabulate([["13-17",age_13_17,user_percent_13_17,likes_13_17,mobile_age_13_17,www_age_13_17,mobile_percent_13_17,www_percent_13_17],
                    ["18-24",age_18_24,user_percent_18_24,likes_18_24,mobile_age_18_24,www_age_18_24,mobile_percent_18_24,www_percent_18_24],
                    ["25-34",age_25_34,user_percent_25_34,likes_25_34,mobile_age_25_34,www_age_25_34,mobile_percent_25_34,www_percent_25_34],
                    ["35-44",age_35_44,user_percent_35_44,likes_35_44,mobile_age_35_44,www_age_35_44,mobile_percent_35_44,www_percent_35_44],
                    ["45-54",age_45_54,user_percent_45_54,likes_45_54,mobile_age_45_54,www_age_45_54,mobile_percent_45_54,www_percent_45_54],
                    ["55-64",age_55_64,user_percent_55_64,likes_55_64,mobile_age_55_64,www_age_55_64,mobile_percent_55_64,www_percent_55_64],
                    ["65-74",age_65_74,user_percent_65_74,likes_65_74,mobile_age_65_74,www_age_65_74,mobile_percent_65_74,www_percent_65_74],
                    ["75+",age_75,user_percent_75,likes_75,mobile_age_75,www_age_75,mobile_percent_75,www_percent_75]],
                    headers=["Age Range", "Number Of Users","Percent of Users","Total Likes","Mobile Likes","Website Likes","Percent of Mobile Likes", "Percent of Website Likes"])

    print(table)
    
    #pie chart for the proportion of age ranges
    Plot_name_ages = ["13-17","18-24","25-34","35-44","45-54","55-64","65-74","75+"]
    Plot_Numbers_Ages = [age_13_17, age_18_24, age_25_34, age_35_44, age_45_54, age_55_64, age_65_74, age_75]
    #establishing the values for all the pie charts involving proportions of mobile likes to desktop likes
    Plot_name_Likes = ["Mobile Likes", "Website Likes"]
    Plot_Numbers_13_17 = [mobile_age_13_17,www_age_13_17]
    Plot_Numbers_18_24 = [mobile_age_18_24,www_age_18_24]
    Plot_Numbers_25_34 = [mobile_age_25_34,www_age_25_34]
    Plot_Numbers_35_44 = [mobile_age_35_44,www_age_35_44]
    Plot_Numbers_45_54 = [mobile_age_45_54,www_age_45_54]
    Plot_Numbers_55_64 = [mobile_age_55_64,www_age_55_64]
    Plot_Numbers_65_74 = [mobile_age_65_74,www_age_65_74]
    Plot_Numbers_75 = [mobile_age_75,www_age_75]

    #formate the plots to a 3x3 grid and give them proper titles and labels
    fig, ax = plt.subplots(3,3)
    fig.suptitle("Social Media Use At Different Ages")
    ax[0,0].pie(Plot_Numbers_Ages, labels=Plot_name_ages)
    ax[0,0].title.set_text("Age groups")
    ax[1,0].pie(Plot_Numbers_13_17, labels=Plot_name_Likes)
    ax[1,0].title.set_text("ages 13 - 17")
    ax[2,0].pie(Plot_Numbers_18_24, labels=Plot_name_Likes)
    ax[2,0].title.set_text("ages 18 - 24")
    ax[0,1].pie(Plot_Numbers_25_34, labels=Plot_name_Likes)
    ax[0,1].title.set_text("ages 25 - 34")
    ax[1,1].pie(Plot_Numbers_35_44, labels=Plot_name_Likes)
    ax[1,1].title.set_text("ages 35 - 44")
    ax[2,1].pie(Plot_Numbers_45_54, labels=Plot_name_Likes)
    ax[2,1].title.set_text("ages 45 - 54")
    ax[0,2].pie(Plot_Numbers_55_64, labels=Plot_name_Likes)
    ax[0,2].title.set_text("ages 55 - 64")
    ax[1,2].pie(Plot_Numbers_65_74, labels=Plot_name_Likes)
    ax[1,2].title.set_text("ages 65 - 74")
    ax[2,2].pie(Plot_Numbers_75, labels=Plot_name_Likes)
    ax[2,2].title.set_text("ages 75+")
    plt.show()

# main routine
# main function that will handle checking for errors and taking user input from cmd line
def main():
    #ask user for a file name and return error if its not a string
    file_name = input("Enter a file: ")
    try:
        check = str(file_name)
    except ValueError:
        print("search term must be a string")
        exit()
    #Get the triad info from the given file
    print("File: "+ file_name)
    FB_data(file_name)

if __name__ == "__main__":
    main()