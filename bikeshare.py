import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': "/Users/jessicakaisaris/Desktop/python/bikeshare-2/chicago.csv",
              'new york city': "/Users/jessicakaisaris/Desktop/python/bikeshare-2/new_york_city.csv",
              'washington': "/Users/jessicakaisaris/Desktop/python/bikeshare-2/washington.csv" }

CITY_DATA[0][0]["Start Time"] = pd.to_datetime(CITY_DATA[0][0]["Start Time"])
CITY_DATA[0][0]['month']= CITY_DATA[0][0]['Start Time'].dt.month
CITY_DATA[0][0]["End Time"] = pd.to_datetime(CITY_DATA[0][0]["End Time"])
CITY_DATA[0][0]["Birth Year"] = pd.to_numeric(CITY_DATA[0][0]["Birth Year"])
CITY_DATA[0][0]["Trip Duration"] = pd.to_numeric(CITY_DATA[0][0]["Trip Duration"])
CITY_DATA[0][1]["Start Time"] = pd.to_datetime(CITY_DATA[0][1]["Start Time"])
CITY_DATA[0][1]["End Time"] = pd.to_datetime(CITY_DATA[0][1]["End Time"])
CITY_DATA[0][1]['month']= CITY_DATA[0][1]['Start Time'].dt.month
CITY_DATA[0][1]["Birth Year"] = pd.to_numeric(CITY_DATA[0][1]["Birth Year"])
CITY_DATA[0][1]["Trip Duration"] = pd.to_numeric(CITY_DATA[0][1]["Trip Duration"])
CITY_DATA[0][1]["Start Time"] = pd.to_datetime(CITY_DATA[0][1]["Start Time"])
CITY_DATA[0][1]["End Time"] = pd.to_datetime(CITY_DATA[0][1]["End Time"])
CITY_DATA[0][1]['month']= CITY_DATA[0][1]['Start Time'].dt.month
CITY_DATA[0][1]["Trip Duration"] = pd.to_numeric(CITY_DATA[0][1]["Trip Duration"])

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True:
        city = input('Would you like to see data from Chicago, New York City, or Washington?\n').lower()
        if city in ('chicago', 'new york city', 'washington'):
            print('You would like to look at the data from {}!\n'.format(city.title()))
            break
        else:
            print('\nPlease enter Chicago, New York City or Washington!')
            
            continue

time_frame = input("Would you like to filter the data by month, day or none?\n").lower()
month = 'all'
day = 'all'

if time_frame == 'month':
    while True:
        month = input("Which month of data would you like to look at?\n").lower()

        if month in ('january','february','march','april','may','june'):
            print("Okay! Let's look at data for {}!\n".format(month.title()))
            break
        else:
            print("Please input the fullname of the month\n")
            

if time_frame == 'day':
    while True:
        day = input("Which day of data would you like to look at?\n").lower()

        if day in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
            print("Okay! Let's look at data for {}!\n".format(day.title()))
            break
        else:
            print("Please input the fullname of the day\n")

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    
if month != 'all':
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = months.index(month) + 1
    df = df[df['month'] == month]
    
if day != 'all':
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday']  
day = days.index(day) + 1
df = df[df['day_of_week'] == day.title()]

return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    common_month= df['month'].mode()[0]
    print('the most common month is',common_month)
    
    
    common_day= df['day'].mode()[0]
    print('the most common month is',common_day)

    # TO DO: display the most common start hour
    common_start_hour= df['hour'].mode()[0]
    print('the most common month is',common_start_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

   def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_station= df['Start Station'].mode()[0]
    print('the most common start station is',common_start_station)

    common_end_station= df['End Station'].mode()[0]
    print('the most common end station is',common_end_station)

    common_end_and_start_station= df(['End Station']['Start Station']).mode()[0]
    
    print('the most common start and end station is ',common_end_and_start_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time= df['start_time'].sum()
    print('total travel time is',total_travel_time)

    # TO DO: display mean travel time
    Average_travel_time= df['start_time'].mean()
    print('total travel time is',Average_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users_types= df['User Types'].value_counts()
    print(users_types)


    # TO DO: Display counts of gender
    users_gender= df['User Types'].value_counts()
    print(users_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_YOB= df['Birth Year'].min()
    print('earliest year of birth is ',earliest_YOB)
    most_recent_YOB= df['Birth Year'].max
    print('the most recent year of birth is ',most_recent_YOB)
    common_YOB= df['Birth Year'].mod()[0]
    print('the most common year of birth is ',common_YOB)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()