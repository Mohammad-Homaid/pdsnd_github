import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

city = None


def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ["chicago", "new york city", "washington"]
    filters = ["month", "day", "none"]
    months = ["january", "february", "march", "april", "may", "june"]
    days = {1: "Saturday", 2: "Sunday", 3: "Monday", 4: "Tuesday", 5: "Wednesday", 6: "Thursday", 7: "Friday"}
    global city

    while True:
        month = "all"
        day = "all"

        try:

            # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
            while True:
                city = input('please enter the city chicago, new york city or washington to get data for ').lower()
                if city in cities:
                    break
                else:
                    print("please enter a valid city  ")
                    continue

            while True:
                filterby = input('would you like to filter by month, day, or none for no time filter ').lower()
                if filterby in filters:
                    break
                else:
                    print("Please enter a valid filter")
                    continue

            # TO DO: get user input for month (all, january, february, ... , june)
            if filterby.lower() == 'month':
                while True:
                    month = input('which month January, February, March, April, May , or June: ').lower()
                    if month in months:
                        break
                    else:
                        print("Please enter a valid month")
                        continue

            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            if filterby.lower() == 'day':
                while True:
                    day = int(input('enter a digit from 1-7 e.g 1=Saturday: '))
                    if day in days:
                        break
                    else:
                        print("enter a valid number from 1 to 7 ")

            break
        except:
            print(' there has been an error try again')

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):

    if city == 'chicago':
        filename = 'chicago.csv'
    elif city == 'washington':
        filename = 'washington.csv'
    elif city == 'new york city':
        filename = 'new_york_city.csv'

    months = ["january", "february", "march", "april", "may", "june"]
    days = {1: "Saturday", 2: "Sunday", 3: "Monday", 4: "Tuesday", 5: "Wednesday", 6: "Thursday", 7: "Friday"}

    # load data file into a dataframe
    df = pd.read_csv(filename)

    df['date'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.dayofweek
    df['hour'] = df['date'].dt.hour
    # getting month in number format

    # flags
    filtermonth = False
    filterday = False

    if month == 'all':
        month = 'all'

    else:
        for i in range(len(months)):
            if month == months[i]:
                month = i + 1
                break
        # sort by month

        dfmonth = df[df['month'] == month]
        filtermonth = True
        # print(dfmonth)

    if day == 'all':
        day = 'all'
    else:
        dfday = df[df['day'] == day]
        filterday = True
    # print(dfday)

    if filtermonth: return dfmonth
    if filterday: return dfday
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    days = {1: "Saturday", 2: "Sunday", 3: "Monday", 4: "Tuesday", 5: "Wednesday", 6: "Thursday", 7: "Friday"}

    # TO DO: display the most common month
    print("the most common month is {} \n".format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print("is the most common day {} \n".format(days[int(df['day'].mode()[0])]))

    # TO DO: display the most common start
    print("The most common starting hour {} \n".format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("is the most commonly used start station {} \n".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("is the most commonly used end station {} \n".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['comboStation'] = df['Start Station'] + " AND " + df['End Station']
    print(" most frequent combination of start station and end station trip is {} \n".format(
        df['comboStation'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("the total travel time is {}".format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print("the total mean travel time {}".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    sub = df[df['User Type'] == 'Subscriber'].count()
    cus = df[df['User Type'] == 'Customer'].count()

    # TO DO: Display counts of user types
    print("Subscriber count is {}".format(sub['User Type'].sum()))
    print("Subscriber count is {}".format(cus['User Type'].sum()))

    if city == "new york city" or city == "chicago":
        # TO DO: Display counts of gender
        male = df[df['Gender'] == 'Male'].count()
        female = df[df['Gender'] == 'Female'].count()
        print("Male count is {}".format(male.sum()))
        print("Female count is {}".format(female.sum()))

        # TO DO: Display earliest, most recent, and most common year of birth
        print("earliest date of birth is {} ".format(df['Birth Year'].min()))
        print("most recent date of birth is {} ".format(df['Birth Year'].max()))
        print("most common date of birth is {} ".format(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def info_df(df):
    # The count is used to make sure i show 5 users per loop
    count = 0;
    while True:

        print(df.iloc[count])
        print('\n')
        count += 1

        if (count % 5 == 0):
            ans = input("Would you like to see more yes / no ").lower()
            if (ans != 'yes'): break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # shows the user 5 rows of raw data
        info_df(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
