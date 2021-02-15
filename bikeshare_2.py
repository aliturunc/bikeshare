import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Plese select a city ,\nchoices:\nchicago, \nnew york city, \nwashington \n')
        if city.lower() == 'chicago' or city.lower() =='new york city' or city.lower() == 'washington':

            print(city)
            break
        else :
            city =="None"
            print(city)
            print("Pls write a city from list !!")



    # get user input for month (all, january, february, ... , june)

    while True:
        month = input('Plese select a month for all months type all or for specific month from 1 to 12 , 1 as January and 2 Febuary \n')
        if month == "1":
            month = "january"
            print(month)
            break
        elif month == "2" :
            month = "february"
            print(month)
            break
        elif month == "3" :
            month = "march"
            print(month)
            break
        elif month == "4" :
            month = "may"
            print(month)
            break
        elif month == "5" :
            month = "june"
            print(month)
            break
        elif month == "6" :
            month = "july"
            print(month)
            break
        elif month.lover()== "all" :
            month = "all"
            print(month)
            break
        else :
            print("Wrong choice !!")






    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('Plese select a day for all months type all or for specific day from 1 to 7 , 1 as Monday and 2 Tuesday \n')
        if day == "1":
            day =  1
            print(day)
            break

        elif day == "2":
            day = 2
            print(day)
            break
        elif day == "3":
            day = 3
            print(day)
            break
        elif day == "4":
            day = 4
            print(day)
            break
        elif day == "5":
            day = 5
            print(day)
            break
        elif day == "6":
            day = 6
            print(day)
            break
        elif day == "7":
            day = 7
            print(day)
            break
        elif day.lover()== "all":
            day = "all"
            print(day)
            break
        else :
            print("Wrong choice !!")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day

    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1


        df = df[df['month'] == month]


    if day != 'all':

        df = df[df['day_of_week'] == day]

    print(df)
    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Start month:', common_month)



    # display the most common day of week


    common_day = df['day_of_week'].mode()[0]
    print('Most Common Start day:', common_day)


    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most Common Start Location:', common_start)


    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most Common End Location:', common_end)


    # display most frequent combination of start station and end station trip

    df['common start end '] = df['Start Station'] + " " + df['End Station']

    common_start_end = df['End Station'].mode()[0]
    print('Most Common Start-End Location:', common_start_end)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_travel = df['Trip Duration'].sum()

    print ("Total travel time =" + str(total_travel))
    # display mean travel time

    mean_time = df['Trip Duration'].mean()
    print("mean time =" + str(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    count_user = df['User Type'].value_counts()
    print("user count  =" + str(count_user))


    # Display counts of gender

    count_gender = df['Gender'].value_counts()
    print(" gender count   =" + str(count_gender))


    # Display earliest, most recent, and most common year of birth

    earliest = df['Birth Year'].min()
    print(" Oldest   =" + str(earliest))

    youngest = df['Birth Year'].max()
    print(" Youngest   =" + str(youngest))

    common_year= df['Birth Year'].mode()[0]
    print('Most Common Old', common_year)

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (True):
        if view_data.lower() == 'yes':
            print(df[start_loc:start_loc+5])
            start_loc = start_loc+5

            view_display = input('\nDo you wish to continue?: \n')
            if view_display.lower() == 'yes':
                print(view_display)
                print(df[start_loc:start_loc + 5])

                break

            elif view_display.lower() == 'no':
                print(view_display)

                break
        else :
            break








    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
       # city, month, day = get_filters()
       # df = load_data(city, month, day)
        df = load_data("chicago", "may", "all")

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
