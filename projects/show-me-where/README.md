# Visualizing the accomplishments of Seattle's "Bridging the Gap" transportation levy

_This set only contains data from 2007 through 2011, even though the levy continued funding projects through 2014._

Here's a description from the city of Bridging the Gap and the types of projects included:

> In 2006, Seattle voters passed a nine-year, $365 million levy for transportation maintenance and improvements known as Bridging the Gap. The levy is complemented by a commercial parking tax. The levy funds programs to address the maintenance backlog for paving; sidewalk development and repairs; bridge repair, rehabilitation and seismic upgrades; tree pruning and planting; transit enhancements; and other much needed maintenance work. Funding also supports projects that implement the Bicycle and Pedestrian Master plans, create a Safe Routes to School Program, improve transit connections and help neighborhoods get larger projects built through the Neighborhood Street Fund large project program.

## About the data

### Summary of data

The data enumerates tasks funded by the "Bridging the Gap" levy and completed by the Seattle Department of Transportation (SDOT) from 2007-2011. (E.g. they fixed a crosswalk here, they planted a tree there, they installed 3 bike racks over on this street corner). This levy expired last year, and in November, Seattle voters passed a new transportation levy, the $930 million "Let's Move Seattle." People seem to agree that a lot of work needs to be done to improve transportation in Seattle, but I guess [some people don't think SDOT has had a very good record at getting things done](http://www.seattletimes.com/seattle-news/transportation/levy-backers-foes-spar-over-whether-city-broke-earlier-vow-to-fix-roads/). I don't know much about it, but I'm from Seattle, and I've dealt with traffic and varying degrees of quality of public transportation firsthand, and I see road construction happening all the time, so I thought it would be interesting to see some of what's actually going on.

### Facts about the data

* Source of the data: [City of Seattle's Open Data portal](https://data.seattle.gov/)
* Data's landing page: [Bridging The Gap Accomplishments 2007 to 2011](https://data.seattle.gov/Transportation/Bridging-The-Gap-Accomplishments-2007-to-2011/vsae-57cr)
* Direct link to data: [Socrata JSON endpoint](https://data.seattle.gov/resource/vsae-57cr.json)
* Data format: JSON, but available in a variety of forms from the landing page
* Number of rows: 33,146

### Description of data fields

#### HISTKEY, COMPKEY, WONO

These two fields are both integers. They seem to be unique identifiers of some sort (each row has a different pair of numbers). E.g. `55823, 11268`

#### COMPTYPE

This is an integer that always seems to be either `68` or `13`. Something to do with compensation?

#### ACTKEY, ACTCODE, PROJECT_ID, PROJECT_NA

These seem to be unique for each project; `ACTKEY` is an integer, and the rest are strings. E.g. `1026, 'B-SRRP', 'TG355330', 'Sign Replacement Program'` is the set of codes for the "Sign Replacement Program." There are a number of programs (E.g. "Traffic Operations Spot Improvements", "Arborist Services", "Landscape Maintenance"), which seem to be the highest level of category for tasks.

#### PROGRAM_NA

A string of the program (programs seem to be subcategories of projects ) that the task was a part of. E.g. `'Signs and Markings'`

#### DIVISION_N, BTG_GROUP

Strings that seem to define who was in charge of this task. E.g. `'SDOT-ROADWAY STRUCTURES', 'Bridge Rehab and Seismic'` The latter seems to be a subcategory of the former, and they both be supercategories for projects.

#### LONG_DESC

A string that's a description of the task. E.g. `'BTG Regulartory street signs replaced'` I think they all start with BTG, which stands for Bridging the Gap, as far as I can tell.

#### QTY, UNIT_OF_ME

An integer and a string quantifying how much was done for measurable tasks. For most tasks, which it doesn't make sense to count, this is just `1, 'Count'`, but for example we see the following for sidewalk repair: `420, 'Square Feet/Block Equivalent'`

#### COMPDTTM, COMPYEAR

Datetime object and integer which define time and year of completion, e.g. `2011-03-01T00:00:00, 2011`

#### SECTOR, NEIGHDIST, DETL_NAMES, GEN_ALIAS, CRA_GR, CRA_NO, LOCATION

Strings (except for `CRA_GR` which is an integer, and `CRA_NO` which is a float) that define, with increasing specificity, the location of the event. E.g. `'NW', 'Northwest', 'Green Lake, Meridian, Roosevelt, Woodland Park', 'Green Lake', 9, 9.4, 'NE 60TH ST BETWEEN LATONA AVE NE AND 4TH AVE NE'`

#### RUN_DATE

Datetime object, I think saying when the data was uploaded. This is always `2011-10-14T00:00:00`.

### Anticipated data wrangling

I think I'll discard most of the data fields, except for `LONG_DESC`, `LOCATION`, `COMPDDTM`, and maybe `PROJECT_NA` and `PROGRAM_NA`. This is sufficient to locate and give basic info about each event.

An interesting task will be to handle locations are of the form 'A st between B st and C st': Google Maps doesn't seem to geocode these automatically, but it can pretty reliably handle the form 'X st and Y st', so I can use a regular expression + subroutine to process 'A st and B st' and 'A st and C st' and then average the lat-longs.
