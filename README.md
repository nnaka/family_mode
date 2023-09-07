
## Installation

```
python3 -m venv venv
source env/bin/activate

pip3 install -r requirements.txt
```

## Run instructions

```
export FLASK_APP=main
export FLASK_ENV=development
flask run
```

## Development

For formating and linting:
```
black main.py data models && mypy main.py data models --strict
```

## Your thought process for solving this problem

I read through the requirements of the deliverable and examined the
mock-up of what the UI in order to think about how the backend
service should behave.

The first set of enumerated requirements seem to indicate a concept
of users who have family relationships and being able to view
details of each individual.

Therefore, I created a simple data model / format for such family
data. The example of which can be found in `data/raw_data.py:family_data`
More details of the choices there are outlined below.

It seemed like there were three main screens that were shown so it
felt intuitive to have three endpoints to serve the data which
would appear on each one of these screens.
1. Score: `/sleep_score` route

2. Stages: `/sleep_stages` route

3. Temperature: `/temperature` route

I thought that the data format provided (i.e. described in an
example
[here](https://gist.github.com/maghis/8c35fe1bb5c7810bdcc6ca389c6cd702))

Going back to the objective of seeing family members and select to
see their data, I realized that there was a need for a route given
a user ID to get the family members. Therefore, I created the
`family_members` route.

## The challenges you encounter

I did look up basic Flask documentation in order to get a grasp of
the overall format of the server application.
It took a bit of time to read through the user flow and fit that
together with the UI mock ups.
From there, deciding the API endpoints felt more natural and the
implementation was relatively smooth once those decisions were
made.

At first, I was worried that the `family_members` route would be
exposing too much information with `id` being explicitly used as a
param instead of some client token that is used from the request
header. If I were to have more time, I think I would have
implemented a login flow for the user from which I would have a
time expiring session token which can be used as an alias to a
user's ID. From looking into the Flask documentation, there does
seem to be a `from flask_login import current_user` which would be
along the lines of what I would do via a login view.

## Tradeoffs

### Data Model

I thought through how the data could be stored if it were to be
based on the data format presented. The two main formats that I
through through were relational (SQL) and document-based (NoSQL).

From looking through the data, due to its highly nested structure,
there did not seems as though there was a clear "domain-driven"
approach to normalize the data into a relational schema.
For example, if we were to create a new primary key for each
instace of the data with the keys of each entries representing the
columns, the nested dictionaries with nested lists etc. would most
likely need to be foreign keys to another table (e.g. timeseries table
with columns tnt, tempRoomC, tempBedC, etc and primary key
referenced in the original table, tempRoomC, tempBedC, etc and
primary key referenced in the original table).
While the power of a schema in a SQL DB is that there is not only
the ACID properies, but also that it provides guarantees on the
format of the data.
It also allows for queries to be built with certain assumptions
(e.g. columns existing with certain types etc)

However, when I think about the problem from a product perspective
a rigid schema may not be the right solution here.
For example, currently there is only one `tempBedC`. However, from
looking through the eightsleep website I see that bed can have two
temperatures for the two sides.
Migrating a schema can be quite disruptive while a flexible
document-based store would most likely be a better more flexible
abstraction.

The family data can be thought of in a graph-like format.
Typically, relationships are reciprocal / commutative. NoSQL
databases / document-based representations are often suited to
represent such structures.

## Decisions

In order to have something that resembles something more like a
"model" rather than just a format, I created the `models` directory.
Due to time contraints, I was unable to create a mock database to
test the features there out and mostly keep that as a reference for
discussion.
