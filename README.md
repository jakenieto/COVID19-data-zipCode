# COVID19-data-zipCode
Python script that gets covid-19 data for a specific zip code and from the last number of specified days. 
The data is then graphed. 

data source: [https://github.com/CSSEGISandData/COVID-19]

## Dependencies 
    requests
    csv
    contextlib 
    matplotlib.pyplot 
    argparse
## How To Run 
    python3 main.py --zip <zip code> --days <# days prior to current date>
## Graph Info
The x-value in the graphs shown are the last days specified
* Total Cases
* Derivative of Total Cases (Number of new cases each day)
## Similar Projects
This is similar to another project that I worked on which can be found here:
    [https://github.com/jakenieto/python-requests-scraping]
