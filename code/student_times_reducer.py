#!/usr/bin/python

'''
-- Input
"author_id"\t"hour"
-- Output
"author_id"\t"hour during which the student has posted the most posts"
'''

import csv
import operator
import sys

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(
    sys.stdout,
    delimiter='\t',
    quotechar='"',
    quoting=csv.QUOTE_ALL
)

old_key = None
hour_list = []
hour_counter = {}

for line in reader:
    # Process only the valid lines.
    if len(line) > 0:
        author_id, hour = line

        this_key = author_id
        if old_key and old_key != this_key:
            for item in hour_list:
                if item in hour_counter:
                    hour_counter[item] += 1
                else:
                    hour_counter[item] = 1

            # Sort the popular hours in descending order.
            popular_hours = sorted(
                hour_counter.iteritems(),
                key=operator.itemgetter(1),
                reverse=True
            )

            last_popular_hour, last_count = popular_hours[0]
            for item in popular_hours:
                popular_hour, count = item
                if last_count == count:
                    results = [old_key, popular_hour]
                    writer.writerow(results)

                    last_count = count

            hour_list = []
            hour_counter = {}

        old_key = this_key
        hour_list.append(hour)

if old_key != None:
    for item in hour_list:
        if item in hour_counter:
            hour_counter[item] += 1
        else:
            hour_counter[item] = 1

    # Sort the popular hours in descending order.
    popular_hours = sorted(
        hour_counter.iteritems(),
        key=operator.itemgetter(1),
        reverse=True
    )

    last_popular_hour, last_count = popular_hours[0]
    for item in popular_hours:
        popular_hour, count = item
        if last_count == count:
            results = [old_key, popular_hour]
            writer.writerow(results)

            last_count = count
