import csv
#module for file path
import auto_path

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open(auto_path.csvPath("movie.csv"), "w", newline = "") as f:
    write = csv.writer(f, delimiter= ",")
    for movie in movies:
        write.writerow(movie)

with open(auto_path.csvPath("movie.csv"), "r") as f:
    row = csv.reader(f, delimiter = ",")
    for item in row:
        print(item)
