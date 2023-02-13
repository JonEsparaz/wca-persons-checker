# WCA Persons Checker

Before a WCA competition, you can run this Python script on a registration CSV file to check for "new" persons that may already exist in the WCA database (i.e., they _might_ not actually be a new competitor and have created a duplicate account).

If no results profiles with the same name exist in the database, a INFO message will be printed. If the same (or a similar) name exists, a WARN message will be printed and the corresponding WCA search page will open in your web browser. It is your responsibility to check if the search results indicate a duplicate person.

Note: Since this script leverages the WCA website's omnisearch, there will be some false positives that you need to ignore (e.g., "John Tim" would yield a search result for "John Timothy"). Hopefully, this is still faster than checking manually and more user-friendly than directly querying the database.

## Example and usage

`example.csv` contains some (mostly fake) data for demonstration purposes. Usage:

```sh
python checker.py example.csv
```
