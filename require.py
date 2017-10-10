"""
Create an GeoSpacial Application that can display weather as well as P&C claims location. Search needs to be by address or GPS. So For example, a 'Policy Holder' or 'Claimant' files a claim regarding roof damage for his current residence allegedly from a weather storm that took place on a particular day. The 'Claims Adjuster' (CA)  will open the application, and search by 'Policy Holder' number that brings up a map with a 'Pin' location of the Claimant's current address. Also, the 'Claims Adjuster' (CA) needs to verify this weather pattern on the day / Hour the storm passed over the Claimant's. So the CA needs to search, by time,  and overlay the weather map for that claim's time-period over the pin of the Claimant's address. ALso, and for visualization purposes as well, paybe put more pins on same map with previous claims that the Policy Holder has filed. Or, also plot on same map few driving trips the policy Holder took with his car same day of claim filed.. 

 

1- Use Openstreet map or 'Leaflette-OpenWeathermap' (http://wiki.openstreetmap.org/wiki/Leaflet-openweathermap) to display weather related vistualization over a geographical location related a weather dataset 
(see data download in #2 below).

2- Download a Weather dataset from the following:
ftp://ftp.ncdc.noaa.gov/pub/data/noaa/2017/
or pick and download a ' 1 day or several days' data or equivalent, ... 

3- Help URLs with some examples on Github: 

https://www.integromat.com/en/integrations/openweathermap/github
https://openweathermap.org/

3.1- Weather Display  and Weather maps layers
https://github.com/nils-werner/owm-display
https://owm.io/hugemaps 
EAXAMPLE: 
https://openweathermap.org/weathermap?basemap=map&cities=true&layer=temperature&lat=30&lon=-20&zoom=3
http://openweathermap.org/api/weathermaps#examples

3.2- OpenWeatherMap Go API
https://github.com/briandowns/openweathermap
https://godoc.org/github.com/briandowns/openweathermap

3.3- https://github.com/csparpa/pyowm     

3.4- OpenWeatherMap for Leaflet based maps
https://github.com/buche/leaflet-openweathermap

3.5- JavaScript libraries for OpenStreetMap applications
https://github.com/alno/osm-js-libs/
    https://www.jsdelivr.com/package/npm/openweathermap-js

3.6- AMChARTS for OpenWeatherMaps
https://www.amcharts.com/products/weather-map/

3.7- GeoNames
http://www.geonames.org/

4- Pin point the address of the claim with a map marker. The claim is for a house roof.

5- On a Different Layer, map one or two or more  car trips that the Claimant (person who filed the claim) traveled that day. I did not include car trip data here but you maybe able to use older datasets that I sent you back when you created the car trip on leaflette.

6- on this amazon drive shaered link find various datasets that you may be able to use :
(claim sample ClaimsDaatforTableau.xsl data set) 
ShareLink (https://www.amazon.com/clouddrive/share/tarizGTfPMFciocn1e82oSTtVkF1qCbtvmtvRjIYJW6)

"""
