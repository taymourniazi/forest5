 Forest5 Dataset Details
 The dataset is the forest cover data which gives the forest cover type
 downloaded from http://kdd.ics.uci.edu/
 The original dataset gives the following details:
Observations
581012
Number of Attributes
54
Attribute breakdown
12 measures, but 54 columns of data (10 quantitative variables, 4 binary wilderness areas and 40 binary soil type variables)
Missing Attribute Values
None
The data is a sample of 5000 observations taken from the full set of 581012.

CODE DESIGNATIONS
Wilderness Areas:
1 -- Rawah Wilderness Area
2 -- Neota Wilderness Area
3 -- Comanche Peak Wilderness Area
4 -- Cache la Poudre Wilderness Area
Soil Types:
1 to 40 : based on the USFS Ecological Landtype Units for this study area.
Forest Cover Types:
1 -- Spruce/Fir
2 -- Lodgepole Pine
3 -- Ponderosa Pine
4 -- Cottonwood/Willow
5 -- Aspen
6 -- Douglas-fir
7 -- Krummholz

Name Data Type Measurement Description
________________________________________________________________________________________________________________
Elevation quantitative metres Elevation in metres
Aspect quantitative azimuth Aspect in degrees azimuth
Slope quantitative degrees Slope in degrees
Horizontal_Distance_To_Hydrology quantitative metres Horz Dist to nearest surface water features
Vertical_Distance_To_Hydrology quantitative metres Vert Dist to nearest surface water features
Horizontal_Distance_To_Roadways quantitative metres Horz Dist to nearest roadway
Hillshade_9am quantitative 0 to 255 index Hillshade index at 9am, summer solstice
Hillshade_Noon quantitative 0 to 255 index Hillshade index at noon, summer solstice
Hillshade_3pm quantitative 0 to 255 index Hillshade index at 3pm, summer solstice
Horizontal_Distance_To_Fire_Points quantitative metres Horz Dist to nearest wildfire ignition points
Wild qualitative 1,2,3 or 4 (see codes above) Wilderness area designation
Twild qualitative w1,w2,w3,w4 Copy of variable “Wild” as character
Soil qualitative 1 to 40 (see codes above) Soil Type designation
Cover_Type (7 types) integer 1 to 7 (see codes above) Forest Cover Type designation
