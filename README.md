## Simple heatmap
A simple heatmap for offences against property and public crimes in Estonia 2016-2017 based on datasets: 

| Dataset    | Source                                         |
| ---------- | ---------------------------------------------- |
| *vara_1*   | https://opendata.smit.ee/ppa/csv/vara_1.csv    |
| *avalik_1* | https://opendata.smit.ee/ppa/csv/avalik_1.csv  |
 
A Python script to convert L-Est coordinates to WGS84 coordinates is also included (`lest_converter.py`).

## Example screenshots
### Estonia
![estonia](example_screenshots/map_estonia.png)
### Harju county
![harjucounty](example_screenshots/map_harjucounty.png)
### Tallinn
![tallinn](example_screenshots/map_tallinn.png)
### Tartu
![tartu](example_screenshots/map_tartu.png)
### Pärnu
![parnu](example_screenshots/map_parnu.png)
### Õismäe and Mustamäe
![oismae](example_screenshots/map_oismae.png)


## Enabling map view on Jupyter Notebook
To enable plot view on Jupyter Notebook:
```sh
$ jupyter nbextension enable --py --sys-prefix widgetsnbextension
$ jupyter nbextension enable --py --sys-prefix gmaps
```

Or, depending on the version
```sh
$ jupyter-nbextension enable --py --sys-prefix widgetsnbextension
$ jupyter-nbextension enable --py --sys-prefix gmaps
```
