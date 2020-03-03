# Author: Kamil Zambrowski
# youtube_data.py: List information about youtube videos based on inputted search term and max number of results
# How to run from terminal: python3 youtube_data.py
# This function will take a search term and search max as input
# The youtube api will parse through these videos and keep track of different statistics in a nested list
# it will write all these stats to a csv file
# and print three different top 5 lists to the console that consist of top 5 views, top 5 like percentage, and top 5 dislike percentage


# code from the given python file
from apiclient.discovery import build   # use build function to create a service object
import unidecode    # need for processing text fields in the search results
import csv          # needed for printing to csv file
API_KEY = "AIzaSyBMVxUG4sELJVJOsfo366NYVMajbBb6lYU" # API Key from the google developers website
API_NAME = "youtube"
API_VERSION = "v3"


#this fucntion will be responsible for writing the results to a csv file
#the input results will come from the youtube api
def csv_function(results):
    #identify each output field in a header line
    header = ["Title", "ID", "Views", "Likes", "Dislikes","Comments","Like Percentage", "Dislike Percentage"]
    # Write to the csv file
    # Figured out how to write csv file from geeksforkeeks.org/working-csv-file-python
    with open("results.csv", 'w') as csvfile:
        #create csv writer object
        csvwriter = csv.writer(csvfile)
        #write the header line
        csvwriter.writerow(header)
        #write the rows with results gathered from youtube api
        csvwriter.writerows(results)

#using a nested array of the data gathered by the youtube api, this function will rank the top 5 videos based
# on views, like percentage, and dislike percentage
# learned how to use this sorting from https://stackoverflow.com/questions/20099669/python-sort-multidimensional-array-based-on-2nd-element-of-subarray
def rankings(data):
    #sort the videos by view count from highest to lowest
    sortedByViewList = sorted(data, key=lambda x: x[2], reverse=True)
    #sort the videos by like percentage from highest to lowest
    sortedByLikePercentageList = sorted(data, key=lambda x: x[6], reverse=True)
    #sort the videos by dislike percentage from highest to lowest
    sortedByDislikePercentageList = sorted(data, key=lambda x: x[7], reverse=True)
    print("Top 5 Videos By View Count: ")
    #loop through the first 5 videos in the already sorted list to get the top 5 by view, likepercentage, and dislikepercentage
    for x in range(5):
        print("#"+str(x+1)+" Title: " + sortedByViewList[x][0] + " ID: " + sortedByViewList[x][1] + " Views: " + str(sortedByViewList[x][2]))
    print("Top 5 Videos By Like Percentage: ")
    for x in range(5):
        print("#"+str(x+1)+" Title: " + sortedByLikePercentageList[x][0] + " ID: " + sortedByLikePercentageList[x][1] + " Like Percentage: " + str(sortedByLikePercentageList[x][6]))
    print("Top 5 Videos By Dislike Percentage: ")
    for x in range(5):
        print("#"+str(x+1)+" Title: " + sortedByDislikePercentageList[x][0] + " ID: " + sortedByDislikePercentageList[x][1] + " Dislike Percentage: " + str(sortedByDislikePercentageList[x][7]))



# function youtube_search will retrieve the youtube analytics
# will take search term as input and also a max number
# will write to a csv file the amount of results that show up based on the maximum number
# will also rank the videos from 1 to 5 based on views and then like percentage and then dislike percentage
def youtube_search(s_term, s_max):
    
    #initializing nested array for the videos along with their stats
    videos = []
    youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)

    search_response = youtube.search().list(q=s_term, part="id,snippet", maxResults=s_max).execute()
    
    # search for videos matching search term;
    
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            title = search_result["snippet"]["title"]
            title = unidecode.unidecode(title)  
            videoId = search_result["id"]["videoId"]
            video_response = youtube.videos().list(id=videoId,part="statistics").execute()
            for video_results in video_response.get("items",[]):
                viewCount = video_results["statistics"]["viewCount"]
                if 'likeCount' not in video_results["statistics"]:
                    likeCount = 0
                    #like percentage will be 0
                    likePercentage = 0
                else:
                    likeCount = video_results["statistics"]["likeCount"]
                    #like percentage will be likes/views
                    #since these are strings, turn them into ints first in order to divide them
                    likePercentage = int(video_results["statistics"]["likeCount"]) / int(video_results["statistics"]["viewCount"])
                if 'dislikeCount' not in video_results["statistics"]:
                    dislikeCount = 0
                    #dislike percentage will be 0
                    dislikePercentage = 0
                else:
                    dislikeCount = video_results["statistics"]["dislikeCount"]
                    #dislike percentage will be dislikes/views
                    #since these are strings, turn them into ints first in order to divide them
                    dislikePercentage = int(video_results["statistics"]["dislikeCount"]) / int(video_results["statistics"]["viewCount"])
                if 'commentCount' not in video_results["statistics"]:
                    commentCount = 0
                else:
                    commentCount = video_results["statistics"]["commentCount"]
            #create a nested array of each video with its statistics
            #the inner arrays will be videos with each index being a different stat
            #the outer array will be made up of different videos
        videos.append([title, videoId, int(viewCount), likeCount, dislikeCount, commentCount,likePercentage,dislikePercentage])

    #write to the csv file
    #run the ranking function to sort the videos
    csv_function(videos)
    rankings(videos)

            
            


# main routine
# main function that will handle checking for errors and taking user input from cmd line
def main():
    #ask user for a search term and return error if its not a string
    search_term = input("Enter a search term: ")
    try:
        check = str(search_term)
    except ValueError:
        print("search term must be a string")
        exit()
    #ask user for a search max and return error if its not an integer
    search_max = input("Enter a max amount of results: ")
    try:
        check = int(search_max)
    except ValueError:
        print("search max must be an integer")
        exit()
    #We want to show top 5 results for multiple fields so there should be at least 5 results
    if int(search_max) < 5:
        print("search max must be at least 5")
        exit()
    #run the youtube search function with the given user input
    print("Search Term: "+search_term, "Search Max: "+search_max)
    youtube_search(search_term, search_max)

if __name__ == "__main__":
    main()
