#!/usr/bin/python 
mouths = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# end 1 - 31
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] + 7 * ['th'] \
        + ['st']

year    = raw_input('Year: ')
mouth   = raw_input('Mouth (1-12): ')
day     = raw_input('Day (1-31): ')

mouth_number = int(mouth)
day_number = int(day)

mouth_name = mouths[mouth_number - 1]
ordinal = day + endings[day_number - 1]

print mouth_name + ' ' + ordinal + ', ' + year
