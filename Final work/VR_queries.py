# graphql_queries.py
import datetime
# Generate queries for each day in October 2020
queries_for_month = []
start_date = "2020-10-01"
end_date = "2020-10-31"

current_date = start_date
while current_date <= end_date:
    query_for_day = f"""
    {{
      trainsByDepartureDate(departureDate: "{current_date}",
        where: {{
          and: [
            {{ timeTableRows: {{ contains: {{ station: {{ shortCode: {{ equals: "HKI" }} }} }} }} }},
            {{ timeTableRows: {{ contains: {{ station: {{ shortCode: {{ equals: "TPE" }} }} }} }} }}
          ]
        }}) {{
        timeTableRows(where:{{station:{{name:{{equals: "Helsinki asema"}}}}
          ) {{
            scheduledTime
            actualTime
            differenceInMinutes
          }}
        }}
      }}
    }}
    """
    queries_for_month.append(query_for_day)
    
    # Move to the next day
    current_date = (datetime.datetime.strptime(current_date, "%Y-%m-%d") + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

# Note: Adjust the date range and other query parameters as needed.
