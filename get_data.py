import zillow
import sys

arg_str = " ".join(sys.argv[1:])
items = arg_str.split("-")


key = "X1-ZWz197rmkb31fv_17jma"

api = zillow.ValuationApi()

for item in items:
    foo = api.GetDeepSearchResults(key, item.split(",")[0], item.split(",")[1])

    print(foo.links.home_details,
          foo.full_address.street,
          foo.extended_data.last_sold_price,
          foo.extended_data.finished_sqft,
          float(foo.extended_data.last_sold_price) / float(foo.extended_data.finished_sqft) if foo.extended_data.last_sold_price is not None and foo.extended_data.finished_sqft is not None else None,
          "sold",
          foo.extended_data.last_sold_date,
          sep=",")
