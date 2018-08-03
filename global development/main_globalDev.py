import global_development
# These may be slow!
list_of_report = global_development.get_reports(test=True)

Mexico = []
Japan = []

#Mexico's Data
for peeps in list_of_report:
    print(peeps["Country"][5])


