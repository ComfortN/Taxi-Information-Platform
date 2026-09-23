# TaxiFind SA

## Backend Schema

**Document Version:** 1.0
**Status:** Draft
**Project Type:** Web Application / Progressive Web App
**Initial Geographic Focus:** Gauteng, South Africa — controlled pilot

**Related Documents:**

* Project Requirements Document (PRD)
* Technical Requirements Document (TRD)
* Application Flow Document
* UI/UX Design Brief

**Next Document:** Implementation Plan

---

# 1. Document Purpose

This document defines the database schema for TaxiFind SA.

It describes:

* Core database entities
* Entity relationships
* PostgreSQL data types
* Primary and foreign keys
* Constraints
* Indexes
* Route structure
* Multi-taxi journey structure
* Taxi rank information
* Fare information
* Verification and data provenance
* Data freshness
* Administrative records
* Audit information
* Seed data requirements
* API-to-database relationships
* Validation rules
* Migration strategy
* MVP database boundaries

The schema is designed around one core principle:

> TaxiFind must only present journey information that is supported by structured application data.

The database should therefore make it possible to distinguish between:

```text
Known
Estimated
Verified
Unverified
Outdated
Unavailable
```

---

# 2. Database Technology

The MVP database will use:

```text
PostgreSQL
```

The backend will access PostgreSQL through:

```text
FastAPI
    ↓
SQLAlchemy
    ↓
PostgreSQL
```

Database migrations will use:

```text
Alembic
```

The database should be capable of supporting geospatial functionality.

PostGIS may be enabled where it provides practical value for:

* Nearby taxi rank searches
* Geographic filtering
* Distance calculations
* Future map functionality

PostGIS is not required for the basic direct-route search functionality.

---

# 3. Database Design Principles

The database should follow these principles.

## 3.1 Structured Data First

Important journey information should be represented using structured records rather than free-form text alone.

For example:

```text
Route
Origin
Destination
Taxi Rank
Fare
Route Step
Verification
```

should each have dedicated database fields.

---

## 3.2 No Invented Routes

The database must not be designed around an assumption that every location can be connected to every other location.

A search such as:

```text
Tladi → Bara
```

should only return a journey if the database contains appropriate supporting records.

A search such as:

```text
Tladi → Midrand
```

must not automatically generate a route merely because:

```text
Tladi → Johannesburg
```

and:

```text
Johannesburg → Midrand
```

exist independently.

A multi-leg journey must be explicitly supported.

---

## 3.3 Route and Journey Are Different Concepts

A **route** represents a known taxi leg.

Example:

```text
Tladi → Bara
```

A **journey** represents a supported commuter trip.

Example:

```text
Vaal → Midrand
```

A journey may consist of:

```text
Route A
    ↓
Transfer
    ↓
Route B
```

The database must preserve this distinction.

---

# 4. High-Level Entity Model

The core MVP entities are:

```text
Location
    │
    ├── TaxiRank
    │
    └── Route
          │
          ├── RouteStep
          │
          └── Fare

Journey
    │
    └── JourneyLeg
          │
          └── Route

Verification / Data Source
    │
    ├── Route
    ├── Fare
    ├── TaxiRank
    └── Journey

AdminUser
    │
    └── AuditLog
```

Conceptually:

```text
Location
   │
   ├──────────────┐
   │              │
   ▼              ▼
TaxiRank        Route
                  │
             ┌────┴────┐
             ▼         ▼
        RouteStep     Fare
                 

Journey
   │
   ▼
JourneyLeg
   │
   ▼
Route
```

---

# 5. Core Entities

The MVP database should contain the following primary entities:

| Entity               | Purpose                                    |               MVP |
| -------------------- | ------------------------------------------ | ----------------: |
| Location             | Represents searchable geographic places    |                 ✅ |
| TaxiRank             | Represents taxi boarding/transfer ranks    |                 ✅ |
| Route                | Represents a known taxi route/leg          |                 ✅ |
| RouteStep            | Describes the route journey                |                 ✅ |
| Fare                 | Stores known/estimated fare information    |                 ✅ |
| Journey              | Represents a supported commuter journey    |                 ✅ |
| JourneyLeg           | Connects a journey to one or more routes   |                 ✅ |
| Verification         | Records verification status and provenance |                 ✅ |
| AdminUser            | Controls administrative access             |                 ✅ |
| AuditLog             | Records important administrative changes   |       Recommended |
| TransportAssociation | Represents taxi associations where known   | Future / Optional |

---

# 6. Location

## 6.1 Purpose

A `Location` represents a searchable geographic place.

Examples:

```text
Tladi
Bara
Soweto
Vaal
Midrand
Johannesburg CBD
```

A location is not necessarily a taxi rank.

---

## 6.2 Fields

| Field        | Type         | Required | Description                    |
| ------------ | ------------ | -------: | ------------------------------ |
| id           | BIGINT       |      Yes | Primary key                    |
| name         | VARCHAR(150) |      Yes | Display name                   |
| slug         | VARCHAR(180) |      Yes | URL/search-friendly identifier |
| type         | VARCHAR(50)  |      Yes | Location type                  |
| description  | TEXT         |       No | Additional information         |
| address      | TEXT         |       No | Physical address               |
| municipality | VARCHAR(150) |       No | Municipality                   |
| city         | VARCHAR(150) |       No | City/town                      |
| province     | VARCHAR(100) |      Yes | Province                       |
| latitude     | DECIMAL(9,6) |       No | Latitude                       |
| longitude    | DECIMAL(9,6) |       No | Longitude                      |
| active       | BOOLEAN      |      Yes | Whether publicly usable        |
| created_at   | TIMESTAMP    |      Yes | Creation timestamp             |
| updated_at   | TIMESTAMP    |      Yes | Last update                    |

---

## 6.3 Location Types

Recommended values:

```text
area
suburb
township
city
town
destination
landmark
taxi_rank_area
```

The database should not require every real-world place to have the same classification.

---

## 6.4 Constraints

```text
name NOT NULL
slug NOT NULL
province NOT NULL
active DEFAULT TRUE
```

The `slug` should be unique.

Example:

```text
Tladi
```

could have:

```text
slug = tladi
```

---

# 7. TaxiRank

## 7.1 Purpose

A `TaxiRank` represents a physical or recognised taxi boarding/transfer location.

Examples:

```text
Tladi Taxi Rank
Bara Taxi Rank
Johannesburg CBD Taxi Rank
```

---

## 7.2 Fields

| Field           | Type         | Required | Description                 |
| --------------- | ------------ | -------: | --------------------------- |
| id              | BIGINT       |      Yes | Primary key                 |
| name            | VARCHAR(180) |      Yes | Rank name                   |
| slug            | VARCHAR(200) |      Yes | Search-friendly identifier  |
| location_id     | BIGINT       |      Yes | Related location            |
| description     | TEXT         |       No | Rank description            |
| address         | TEXT         |       No | Physical address            |
| latitude        | DECIMAL(9,6) |       No | Latitude                    |
| longitude       | DECIMAL(9,6) |       No | Longitude                   |
| operating_info  | TEXT         |       No | Known operating information |
| verification_id | BIGINT       |       No | Verification record         |
| active          | BOOLEAN      |      Yes | Public availability         |
| created_at      | TIMESTAMP    |      Yes | Creation timestamp          |
| updated_at      | TIMESTAMP    |      Yes | Last update                 |

---

# 8. Location-to-Taxi-Rank Relationship

One location may contain multiple taxi ranks.

Example:

```text
Location:
Johannesburg CBD

        │
        ├── Taxi Rank A
        ├── Taxi Rank B
        └── Taxi Rank C
```

Database relationship:

```text
Location 1 ──────── * TaxiRank
```

Foreign key:

```text
taxi_ranks.location_id
        →
locations.id
```

---

# 9. Route

## 9.1 Purpose

A `Route` represents a known taxi leg from one supported location/rank area to another.

Example:

```text
Tladi → Bara
```

A route is not automatically a complete commuter journey.

---

## 9.2 Fields

| Field                   | Type         | Required | Description               |
| ----------------------- | ------------ | -------: | ------------------------- |
| id                      | BIGINT       |      Yes | Primary key               |
| name                    | VARCHAR(200) |      Yes | Human-readable route name |
| slug                    | VARCHAR(220) |      Yes | Unique identifier         |
| origin_location_id      | BIGINT       |      Yes | Starting location         |
| destination_location_id | BIGINT       |      Yes | Ending location           |
| boarding_rank_id        | BIGINT       |       No | Main boarding rank        |
| destination_rank_id     | BIGINT       |       No | Main destination rank     |
| description             | TEXT         |       No | Route description         |
| verification_status     | VARCHAR(40)  |      Yes | Current data status       |
| source                  | TEXT         |       No | Information source        |
| last_verified_at        | TIMESTAMP    |       No | Last verification         |
| active                  | BOOLEAN      |      Yes | Public availability       |
| created_at              | TIMESTAMP    |      Yes | Creation timestamp        |
| updated_at              | TIMESTAMP    |      Yes | Last update               |

---

# 10. Route Relationships

A route belongs to:

```text
Origin Location
Destination Location
```

and may reference:

```text
Boarding Taxi Rank
Destination Taxi Rank
```

Relationship:

```text
Location ─────── Route
   │              │
   │              ├── origin
   │              └── destination
   │
TaxiRank ─────── Route
```

---

# 11. Route Constraints

The database should enforce:

```text
origin_location_id != destination_location_id
```

where practical.

A route must have:

```text
name
origin
destination
verification_status
active
```

A route should not be publicly returned when:

```text
active = false
```

or when its status indicates that it should not currently be presented.

---

# 12. Route Status

The route verification status should use a controlled set of values.

Recommended:

```text
VERIFIED
COMMUNITY_REPORTED
UNVERIFIED
OUTDATED
UNAVAILABLE
```

The database should use an enum or constrained string representation.

---

# 13. RouteStep

## 13.1 Purpose

A `RouteStep` provides the human-readable instructions required to understand a route.

Example:

```text
1. Start at Tladi
2. Walk to Tladi Taxi Rank
3. Take taxi toward Bara
4. Get off at Bara Taxi Rank
5. Continue to destination
```

---

## 13.2 Fields

| Field                      | Type        | Required | Description                |
| -------------------------- | ----------- | -------: | -------------------------- |
| id                         | BIGINT      |      Yes | Primary key                |
| route_id                   | BIGINT      |      Yes | Related route              |
| step_order                 | INTEGER     |      Yes | Sequence number            |
| step_type                  | VARCHAR(40) |      Yes | Type of step               |
| from_rank_id               | BIGINT      |       No | Starting rank              |
| to_rank_id                 | BIGINT      |       No | Ending rank                |
| instruction                | TEXT        |      Yes | Human-readable instruction |
| estimated_duration_minutes | INTEGER     |       No | Estimated duration         |
| created_at                 | TIMESTAMP   |      Yes | Creation timestamp         |
| updated_at                 | TIMESTAMP   |      Yes | Last update                |

---

# 14. Route Step Types

Recommended values:

```text
START
WALK
BOARD
TRAVEL
GET_OFF
ARRIVAL
TRANSFER
```

Example:

```text
1 START
2 WALK
3 BOARD
4 TRAVEL
5 GET_OFF
6 ARRIVAL
```

---

# 15. Route Step Ordering

Each route must maintain an explicit order.

Example:

```text
route_id = 1

step_order = 1
step_order = 2
step_order = 3
step_order = 4
```

A route must not contain two steps with the same:

```text
route_id + step_order
```

Therefore:

```text
UNIQUE(route_id, step_order)
```

should be enforced.

---

# 16. Fare

## 16.1 Purpose

A `Fare` stores a known fare associated with a route.

TaxiFind must not predict fares that are not present in the database.

---

## 16.2 Fields

| Field               | Type          | Required | Description         |
| ------------------- | ------------- | -------: | ------------------- |
| id                  | BIGINT        |      Yes | Primary key         |
| route_id            | BIGINT        |      Yes | Related route       |
| amount              | NUMERIC(10,2) |      Yes | Fare amount         |
| currency            | CHAR(3)       |      Yes | Currency code       |
| fare_type           | VARCHAR(40)   |      Yes | Fare classification |
| effective_from      | DATE          |       No | Start date          |
| effective_until     | DATE          |       No | End date            |
| verification_status | VARCHAR(40)   |      Yes | Data status         |
| source              | TEXT          |       No | Fare source         |
| last_verified_at    | TIMESTAMP     |       No | Last verification   |
| active              | BOOLEAN       |      Yes | Whether usable      |
| created_at          | TIMESTAMP     |      Yes | Creation timestamp  |
| updated_at          | TIMESTAMP     |      Yes | Last update         |

---

# 17. Fare Rules

The MVP should use:

```text
currency = ZAR
```

The database must not allow negative fares.

Therefore:

```text
amount >= 0
```

should be enforced.

A missing fare must be represented as:

```text
NULL / unavailable
```

and never:

```text
R0
```

unless a genuine zero fare is explicitly supported.

---

# 18. Fare Validity

Fare records may have validity dates.

Example:

```text
Fare:
R20

Effective:
2026-09-01

Until:
2026-12-31
```

This allows future fare updates without destroying historical records.

Only the appropriate active/current fare should normally be returned to the public API.

---

# 19. Multiple Fare Records

A route may have multiple fare records over time.

Example:

```text
Tladi → Bara

R18
Jan–Jun

R20
Jul–Dec
```

This preserves historical information.

The application should not present two active current fares unless there is a documented reason.

---

# 20. Journey

## 20.1 Purpose

A `Journey` represents a commuter journey supported by TaxiFind.

This is intentionally different from a route.

Example:

```text
Route:
Tladi → Bara

Journey:
Tladi → Bara
```

A direct journey may contain one route.

A multi-leg journey may contain several routes.

---

# 21. Why Journeys Are Stored Explicitly

TaxiFind should not attempt to discover every possible journey by automatically joining routes.

For example, the existence of:

```text
Route A:
Vaal → Johannesburg

Route B:
Johannesburg → Midrand
```

does not automatically prove that a commuter can reliably use those routes together.

Therefore, supported multi-leg journeys should be explicitly curated.

This provides:

* Better data control
* Better verification
* Clear transfer instructions
* Fewer false route combinations
* Easier administration

---

# 22. Journey Fields

| Field                   | Type         | Required | Description         |
| ----------------------- | ------------ | -------: | ------------------- |
| id                      | BIGINT       |      Yes | Primary key         |
| name                    | VARCHAR(200) |      Yes | Journey name        |
| slug                    | VARCHAR(220) |      Yes | Unique identifier   |
| origin_location_id      | BIGINT       |      Yes | Journey origin      |
| destination_location_id | BIGINT       |      Yes | Journey destination |
| description             | TEXT         |       No | Journey summary     |
| verification_status     | VARCHAR(40)  |      Yes | Journey status      |
| source                  | TEXT         |       No | Journey source      |
| last_verified_at        | TIMESTAMP    |       No | Last verification   |
| active                  | BOOLEAN      |      Yes | Public availability |
| created_at              | TIMESTAMP    |      Yes | Creation timestamp  |
| updated_at              | TIMESTAMP    |      Yes | Last update         |

---

# 23. JourneyLeg

## 23.1 Purpose

A `JourneyLeg` connects a supported journey to one of its known taxi routes.

Example:

```text
Journey:
Vaal → Midrand

Leg 1:
Vaal → Johannesburg

Transfer:
Johannesburg

Leg 2:
Johannesburg → Midrand
```

---

## 23.2 Fields

| Field                | Type      | Required | Description                 |
| -------------------- | --------- | -------: | --------------------------- |
| id                   | BIGINT    |      Yes | Primary key                 |
| journey_id           | BIGINT    |      Yes | Related journey             |
| route_id             | BIGINT    |      Yes | Related route               |
| leg_order            | INTEGER   |      Yes | Sequence                    |
| transfer_location_id | BIGINT    |       No | Transfer location after leg |
| transfer_rank_id     | BIGINT    |       No | Transfer rank               |
| transfer_instruction | TEXT      |       No | Transfer instructions       |
| created_at           | TIMESTAMP |      Yes | Creation timestamp          |
| updated_at           | TIMESTAMP |      Yes | Last update                 |

---

# 24. Journey Leg Ordering

Each journey must have ordered legs.

Example:

```text
Journey 5

Leg 1
Vaal → Johannesburg

Leg 2
Johannesburg → Midrand
```

Constraint:

```text
UNIQUE(journey_id, leg_order)
```

---

# 25. Journey Continuity

Where multiple legs are used, the system should validate that the journey makes geographic/logical sense.

For example:

```text
Leg 1 destination
        ↓
Transfer location
        ↓
Leg 2 origin
```

must be explicitly compatible.

The backend must not assume that two locations with similar names represent the same transfer point.

---

# 26. Direct Journeys

A direct journey can contain:

```text
Journey
  └── Leg 1
        └── Route
```

Example:

```text
Tladi → Bara

Journey
    ↓
Leg 1
    ↓
Tladi → Bara Route
```

This allows the same route structure to support both direct and multi-leg journeys.

---

# 27. Multi-Leg Journeys

A multi-leg journey may contain:

```text
Journey
  │
  ├── Leg 1
  │      └── Route A
  │
  ├── Transfer
  │
  └── Leg 2
         └── Route B
```

The transfer must be explicit.

The application should not invent:

```text
"Change taxi here"
```

unless the journey data specifies the transfer.

---

# 28. Journey Fare Calculation

The public API may calculate the total estimated fare from the active fare associated with each journey leg.

Example:

```text
Leg 1: R20
Leg 2: R18

Total:
R38
```

The total must equal:

```text
SUM(active known leg fares)
```

If one or more required fares are unavailable, the API should not invent a total.

It should instead return:

```text
Estimated total fare
Unavailable
```

while identifying the available individual fare information where appropriate.

---

# 29. Journey Duration

Journey duration may be calculated from known route/step estimates.

However, the system must clearly label the result as:

```text
Estimated journey time
```

It must not imply:

```text
Guaranteed arrival time
```

or:

```text
Live travel time
```

---

# 30. Verification

## 30.1 Purpose

Verification records provide transparency around the quality and freshness of information.

Verification may apply to:

```text
Routes
Fares
Taxi Ranks
Journeys
```

---

# 31. Verification Fields

| Field          | Type        | Required | Description            |
| -------------- | ----------- | -------: | ---------------------- |
| id             | BIGINT      |      Yes | Primary key            |
| status         | VARCHAR(40) |      Yes | Verification status    |
| source         | TEXT        |       No | Information source     |
| notes          | TEXT        |       No | Verification notes     |
| verified_by    | BIGINT      |       No | Admin who reviewed     |
| verified_at    | TIMESTAMP   |       No | Verification timestamp |
| next_review_at | TIMESTAMP   |       No | Optional review date   |
| created_at     | TIMESTAMP   |      Yes | Creation timestamp     |
| updated_at     | TIMESTAMP   |      Yes | Last update            |

---

# 32. Verification Statuses

The canonical values are:

```text
VERIFIED
COMMUNITY_REPORTED
UNVERIFIED
OUTDATED
UNAVAILABLE
```

Meaning:

### VERIFIED

Information has been reviewed and is considered suitable for public presentation.

### COMMUNITY_REPORTED

Information has been reported but has not necessarily completed the required administrative verification.

### UNVERIFIED

Information exists but has not been sufficiently verified.

### OUTDATED

Information was previously known but may no longer be current.

### UNAVAILABLE

Information should not currently be presented as usable journey information.

---

# 33. Verification Rules

The public API should apply clear rules.

For example:

```text
VERIFIED
→ Public

COMMUNITY_REPORTED
→ Public only where product rules permit and clearly labelled

UNVERIFIED
→ Public only where appropriate and clearly labelled

OUTDATED
→ Clearly labelled or excluded depending on product policy

UNAVAILABLE
→ Excluded from supported journey results
```

The exact visibility rules should be implemented centrally in the backend rather than independently in every frontend component.

---

# 34. Data Source

Every public route should have either:

```text
source
```

or:

```text
verification information
```

The source may describe where the information came from.

Examples:

```text
Admin field research
Verified local transport information
Transport operator information
Publicly available transport information
```

The source field is informational and should not be treated as proof by itself.

---

# 35. AdminUser

## 35.1 Purpose

The MVP requires administrative access for maintaining the controlled dataset.

---

## 35.2 Fields

| Field         | Type         | Required |
| ------------- | ------------ | -------: |
| id            | BIGINT       |      Yes |
| email         | VARCHAR(255) |      Yes |
| password_hash | TEXT         |      Yes |
| name          | VARCHAR(150) |       No |
| role          | VARCHAR(30)  |      Yes |
| active        | BOOLEAN      |      Yes |
| last_login_at | TIMESTAMP    |       No |
| created_at    | TIMESTAMP    |      Yes |
| updated_at    | TIMESTAMP    |      Yes |

---

# 36. Admin Roles

The initial schema may support:

```text
ADMIN
MODERATOR
```

The MVP can initially use:

```text
ADMIN
```

if there is no requirement for more granular permissions.

The schema should not introduce complex role structures before they are required.

---

# 37. AuditLog

## 37.1 Purpose

The audit log records important administrative changes.

Examples:

```text
Route created
Route updated
Fare changed
Route marked outdated
Route marked verified
Taxi rank updated
Journey disabled
```

---

## 37.2 Fields

| Field         | Type        | Required |
| ------------- | ----------- | -------: |
| id            | BIGINT      |      Yes |
| admin_user_id | BIGINT      |       No |
| entity_type   | VARCHAR(50) |      Yes |
| entity_id     | BIGINT      |      Yes |
| action        | VARCHAR(50) |      Yes |
| old_values    | JSONB       |       No |
| new_values    | JSONB       |       No |
| created_at    | TIMESTAMP   |      Yes |

---

# 38. Audit Log Examples

Example:

```text
entity_type:
route

entity_id:
12

action:
VERIFY

old_values:
{
  "verification_status": "UNVERIFIED"
}

new_values:
{
  "verification_status": "VERIFIED"
}
```

This provides an administrative history without requiring a complete version-control system for every database record.

---

# 39. TransportAssociation

This entity is not required for the initial MVP but may be useful later.

Potential fields:

```text
id
name
registration_information
area
contact_information
verification_status
created_at
updated_at
```

The MVP should not depend on association data being complete.

---

# 40. Entity Relationship Summary

The main relationships are:

```text
Location
│
├── TaxiRank
│
├── Route (origin)
│
├── Route (destination)
│
└── Journey (origin/destination)


Route
│
├── RouteStep
├── Fare
└── JourneyLeg


Journey
│
└── JourneyLeg
        │
        └── Route


Verification
│
├── Route
├── Fare
├── TaxiRank
└── Journey


AdminUser
│
└── AuditLog
```

---

# 41. Recommended Database Tables

The MVP PostgreSQL database should therefore contain approximately:

```text
locations
taxi_ranks
routes
route_steps
fares
journeys
journey_legs
verifications
admin_users
audit_logs
```

Optional/future:

```text
transport_associations
community_reports
saved_journeys
user_accounts
notifications
```

The future tables should not be required by the MVP.

---

# 42. Foreign Key Behaviour

Foreign keys should protect data integrity.

Examples:

```text
taxi_ranks.location_id
    → locations.id

routes.origin_location_id
    → locations.id

routes.destination_location_id
    → locations.id

route_steps.route_id
    → routes.id

fares.route_id
    → routes.id

journey_legs.journey_id
    → journeys.id

journey_legs.route_id
    → routes.id
```

Deletion behaviour should generally avoid accidentally destroying historical information.

Soft deactivation using:

```text
active = false
```

is preferred for public route data.

---

# 43. Soft Deactivation

Important transport records should generally not be hard-deleted during normal administration.

For example:

```text
Route
Tladi → Bara
```

may become outdated.

Instead of deleting the record:

```text
active = false
```

or:

```text
verification_status = OUTDATED
```

can preserve historical information.

This is especially important for auditability.

---

# 44. Timestamps

Core tables should use:

```text
created_at
updated_at
```

Where data freshness matters, also use:

```text
last_verified_at
```

Timestamps should preferably be stored in UTC at the database level.

The frontend can display dates in the user's appropriate local representation.

---

# 45. Slugs

Public-facing entities should use stable slugs.

Examples:

```text
tladi
bara
tladi-taxi-rank
tladi-to-bara
vaal-to-midrand
```

Slugs should be:

```text
lowercase
unique
URL-safe
stable
```

Changing a display name should not unnecessarily change the underlying database ID.

---

# 46. Database Indexes

The following fields should be indexed.

## Locations

```text
locations.slug
locations.name
locations.type
locations.active
```

## Taxi Ranks

```text
taxi_ranks.slug
taxi_ranks.location_id
taxi_ranks.active
```

## Routes

```text
routes.slug
routes.origin_location_id
routes.destination_location_id
routes.verification_status
routes.active
```

## Route Steps

```text
route_steps.route_id
route_steps.route_id + step_order
```

## Fares

```text
fares.route_id
fares.active
fares.effective_from
fares.effective_until
```

## Journeys

```text
journeys.slug
journeys.origin_location_id
journeys.destination_location_id
journeys.verification_status
journeys.active
```

## Journey Legs

```text
journey_legs.journey_id
journey_legs.route_id
journey_legs.journey_id + leg_order
```

These indexes should support the primary search patterns without premature optimisation.

---

# 47. Search Query Model

The main journey search will conceptually query:

```text
Origin
+
Destination
+
Supported Journey
```

Example:

```text
GET /api/v1/journeys/search
    ?origin=tladi
    &destination=bara
```

The backend should identify:

```text
locations
    ↓
journeys
    ↓
journey_legs
    ↓
routes
    ↓
route_steps
    ↓
fares
    ↓
verification
```

and return a structured journey result.

---

# 48. Direct Journey Search

For:

```text
Tladi → Bara
```

the search may find:

```text
Journey
    ↓
Leg 1
    ↓
Tladi → Bara Route
```

The API can then return:

```json
{
  "origin": "Tladi",
  "destination": "Bara",
  "journey_type": "direct",
  "changes": 0,
  "estimated_fare": 20,
  "estimated_duration_minutes": 40,
  "verification_status": "VERIFIED"
}
```

The exact API schema will be defined by the implementation.

---

# 49. Multi-Leg Journey Search

For:

```text
Vaal → Midrand
```

a curated journey may contain:

```text
Leg 1
Vaal → Johannesburg

Transfer
Johannesburg

Leg 2
Johannesburg → Midrand
```

The API may return:

```json
{
  "journey_type": "multi_leg",
  "changes": 1,
  "legs": [
    {
      "route": "Vaal → Johannesburg"
    },
    {
      "route": "Johannesburg → Midrand"
    }
  ]
}
```

The actual API response should include the structured transfer information required by the frontend.

---

# 50. No Automatic Arbitrary Route Combination

The backend must not implement logic equivalent to:

```text
Find any route starting near origin
+
Find any route ending near destination
+
Guess a transfer
=
Journey
```

This would create unsupported journey information.

Instead:

```text
Curated Journey
      ↓
Known Journey Legs
      ↓
Known Transfer
      ↓
Public Result
```

This is a fundamental MVP data-integrity rule.

---

# 51. Search Location Matching

Location search should support:

```text
Exact name
Partial name
Case-insensitive matching
Slug
Known aliases where implemented
```

For example:

```text
Tla
```

may return:

```text
Tladi
```

Search suggestions must only return records that exist in the database.

---

# 52. Location Aliases

A future extension may introduce:

```text
location_aliases
```

to support:

```text
Common name
Alternative spelling
Local name
Historical name
```

This is not required as a separate table for the first MVP implementation.

A simple alias field or search mapping may be sufficient initially.

---

# 53. Geospatial Data

Locations and taxi ranks may store:

```text
latitude
longitude
```

using:

```text
DECIMAL(9,6)
```

This provides sufficient precision for the MVP.

If PostGIS is introduced, the schema may later use:

```text
GEOGRAPHY(Point, 4326)
```

for more advanced spatial queries.

---

# 54. Map Data Integrity

The presence of coordinates does not imply that the application knows the exact road route.

For example:

```text
Origin coordinates
+
Destination coordinates
```

must not automatically result in:

```text
fictional taxi route geometry
```

The map should only display route lines where reliable geometry exists.

---

# 55. Route Geometry

Exact route geometry is outside the required core schema for the first MVP.

If introduced later, it may be represented using:

```text
route_geometry
```

or a PostGIS geometry column.

Possible future structure:

```text
route_id
geometry
source
verification_status
```

This should only be used when the geometry has an appropriate source.

---

# 56. Data Validation

The backend should validate:

### Locations

```text
name required
province required
valid coordinates if supplied
```

### Taxi ranks

```text
name required
location required
valid coordinates if supplied
```

### Routes

```text
origin required
destination required
origin != destination
verification status required
```

### Route steps

```text
route required
step order required
instruction required
unique step order per route
```

### Fares

```text
route required
amount >= 0
currency = ZAR
verification status required
```

### Journeys

```text
origin required
destination required
origin != destination
verification status required
```

### Journey legs

```text
journey required
route required
leg order required
unique leg order per journey
```

---

# 57. Public Data Rules

The public API must apply the following principles.

### Rule 1

Do not return inactive records as normal supported data.

### Rule 2

Do not return `UNAVAILABLE` journeys as supported journeys.

### Rule 3

Do not invent missing fares.

### Rule 4

Do not invent journey durations.

### Rule 5

Do not automatically create transfers.

### Rule 6

Do not imply that absence from the database means the real-world journey does not exist.

### Rule 7

Expose verification information where relevant.

---

# 58. Fare API Behaviour

If a fare exists:

```text
Estimated fare
R20
```

If no fare exists:

```text
Estimated fare
Unavailable
```

The backend should never silently convert:

```text
NULL
```

into:

```text
0
```

---

# 59. Duration API Behaviour

If an estimated duration exists:

```text
35–45 minutes
```

If unavailable:

```text
Estimated time
Unavailable
```

The backend should not fabricate a duration based solely on geographic distance.

---

# 60. Verification API Behaviour

The API should expose enough information for the UI to display:

```text
✓ Verified
Last verified:
15 September 2026
```

Where appropriate, it may also expose:

```text
source
verification notes
```

but internal administrative information should not automatically become public.

---

# 61. Data Freshness

The schema must support data freshness through:

```text
last_verified_at
```

and optionally:

```text
next_review_at
```

The backend can later use these values to identify potentially outdated records.

Example:

```text
Last verified:
15 September 2026
```

is preferable to exposing a raw timestamp such as:

```text
2026-09-15T10:32:47.218Z
```

to ordinary users.

---

# 62. Seed Data

The MVP should include a small, controlled dataset.

Planning targets:

```text
10–20 taxi ranks
20–50 routes
20–50 fare records
```

These are planning targets, not mandatory release thresholds.

Quality and verification are more important than record count.

---

# 63. Seed Data Coverage

Initial data should focus on the selected pilot areas:

```text
Soweto
Johannesburg
Vaal
Midrand
```

The seed data should contain enough relationships to demonstrate:

```text
Direct journey
Multi-leg journey
Taxi rank information
Fare information
Verification
Unavailable information
```

---

# 64. Seed Data Example

Illustrative structure:

```text
Location:
Tladi

Location:
Bara

Taxi Rank:
Tladi Taxi Rank

Taxi Rank:
Bara Taxi Rank

Route:
Tladi → Bara

Route Step:
Walk to Tladi Taxi Rank

Route Step:
Take taxi toward Bara

Route Step:
Get off at Bara Taxi Rank

Fare:
R20

Verification:
Verified
```

These values are examples of schema structure and must not be treated as verified real-world route information until properly sourced.

---

# 65. Multi-Leg Seed Example

Illustrative:

```text
Journey:
Vaal → Midrand

Leg 1:
Vaal → Johannesburg

Transfer:
Johannesburg

Leg 2:
Johannesburg → Midrand
```

Each leg must reference an existing route.

The journey must not exist merely because two routes happen to share a location name.

---

# 66. Database Migration Strategy

Alembic should manage database schema changes.

Initial migration:

```text
001_initial_schema
```

Possible future migrations:

```text
002_add_postgis
003_add_location_aliases
004_add_route_geometry
005_add_community_reports
```

Migration files should be small and logically grouped.

---

# 67. Migration Rules

Database changes should:

* Be committed to Git
* Be reversible where practical
* Avoid destructive changes without explicit migration logic
* Preserve existing data
* Be tested before production deployment

Developers should not manually modify production tables as the normal development workflow.

---

# 68. Database Seed Strategy

Seed scripts should be separate from migrations.

For example:

```text
database/
├── migrations/
└── seeds/
```

A seed script may:

```text
Create locations
Create taxi ranks
Create routes
Create route steps
Create fares
Create verification records
Create demo journeys
```

Seed data should be clearly identified as:

```text
development/demo data
```

unless it has been deliberately verified for public use.

---

# 69. Data Import

A future import script may support structured route data.

Example:

```text
scripts/import_routes.py
```

Imported data must pass validation before becoming publicly visible.

A CSV import should not automatically make every imported route:

```text
VERIFIED
```

The verification state must be explicitly assigned.

---

# 70. Database Integrity

The schema should protect against:

* Orphaned routes
* Orphaned fares
* Duplicate route steps
* Duplicate journey legs
* Negative fares
* Invalid coordinates
* Invalid verification states
* Duplicate slugs
* Broken foreign-key relationships

Application-level validation should complement database constraints rather than replace them.

---

# 71. API and Database Separation

The API should not expose raw database models directly.

Instead:

```text
Database Model
      ↓
Repository / Service
      ↓
Pydantic Schema
      ↓
API Response
```

This prevents the database structure from becoming tightly coupled to the public API.

---

# 72. Recommended Backend Layers

The backend may follow:

```text
backend/app/

├── api/
│   └── routes/
│
├── models/
│
├── schemas/
│
├── repositories/
│
├── services/
│
├── database/
│
└── core/
```

Example:

```text
journeys.py
    ↓
journey_service.py
    ↓
journey_repository.py
    ↓
SQLAlchemy models
    ↓
PostgreSQL
```

---

# 73. Repository Responsibilities

Repositories should primarily handle database access.

Example:

```text
find_journey_by_origin_destination()
get_journey_by_id()
get_journey_legs()
get_route_steps()
get_active_fare()
```

They should not contain extensive presentation logic.

---

# 74. Service Responsibilities

Services should handle business rules.

For example:

```text
JourneyService
```

may:

* Validate journey availability
* Load journey legs
* Calculate known fare totals
* Calculate estimated duration
* Determine transfer count
* Apply verification visibility rules
* Build the public journey response

---

# 75. Search Service

The journey search service should follow approximately:

```text
Receive origin + destination
          ↓
Resolve locations
          ↓
Find supported journeys
          ↓
Check active/public status
          ↓
Load journey legs
          ↓
Load route steps
          ↓
Load fare information
          ↓
Load verification information
          ↓
Build result
          ↓
Return supported journey(s)
```

If no supported journey exists:

```text
Return clear no-supported-journey result
```

Do not construct an unsupported route.

---

# 76. Database-to-UI Mapping

The backend should provide data that maps directly to the UI requirements.

### Result card needs:

```text
origin
destination
journey_type
fare
duration
changes
verification_status
last_verified_at
```

### Journey details needs:

```text
steps
boarding rank
get-off rank
transfer
fare
duration
verification
```

### Map needs:

```text
origin coordinates
rank coordinates
transfer coordinates
destination coordinates
```

---

# 77. Public Journey Response Concept

A public journey response may conceptually look like:

```json
{
  "id": 1,
  "origin": {
    "id": 10,
    "name": "Tladi"
  },
  "destination": {
    "id": 20,
    "name": "Bara"
  },
  "journey_type": "direct",
  "changes": 0,
  "fare": {
    "amount": 20,
    "currency": "ZAR",
    "estimated": true
  },
  "duration": {
    "min_minutes": 35,
    "max_minutes": 45,
    "estimated": true
  },
  "verification": {
    "status": "VERIFIED",
    "last_verified_at": "2026-09-15"
  },
  "legs": []
}
```

The final API contract will be defined during implementation.

---

# 78. Administrative Data Flow

When an administrator creates a route:

```text
Admin
 ↓
Create Route
 ↓
Select Origin
 ↓
Select Destination
 ↓
Add Route Steps
 ↓
Add Fare
 ↓
Add Source
 ↓
Set Verification Status
 ↓
Save
 ↓
Audit Log
 ↓
Public API
```

The route should not become publicly presented as verified unless the administrator explicitly assigns the appropriate verification state.

---

# 79. Updating a Fare

When a fare changes:

```text
Existing fare
    ↓
Retain historical record
    ↓
Create/update current fare
    ↓
Update verification information
    ↓
Audit change
```

The system should avoid silently overwriting important historical fare information where history is needed.

---

# 80. Updating Route Verification

Example:

```text
UNVERIFIED
      ↓
Admin review
      ↓
VERIFIED
```

or:

```text
VERIFIED
      ↓
New information
      ↓
OUTDATED
```

The audit log should capture important status changes.

---

# 81. Privacy

The MVP database should minimise personal information.

Public journey data does not require commuter accounts.

The MVP therefore does not need to store:

```text
Commuter travel history
Saved journeys
Personal location history
Payment information
Driver personal information
```

unless a future feature explicitly requires it.

---

# 82. Security

The database should:

* Use parameterised queries/ORM operations
* Protect admin credentials
* Store password hashes rather than plaintext passwords
* Restrict administrative endpoints
* Validate incoming data
* Avoid exposing internal database errors
* Use environment variables for database credentials

Production credentials must never be committed to Git.

---

# 83. Backup Strategy

The PostgreSQL database should have a backup strategy before production use.

At minimum:

```text
Database backup
+
Backup retention
+
Restore testing
```

The backup system is an operational concern and will be detailed further during implementation/deployment planning.

---

# 84. MVP Database Boundary

The MVP database includes:

```text
Locations
Taxi ranks
Routes
Route steps
Fares
Curated journeys
Journey legs
Verification
Admin users
Audit logs
```

It does not require:

```text
Passenger accounts
Driver accounts
Bookings
Payments
Live GPS
Community feed
Push notifications
AI conversations
Voice commands
Offline route database
Other transport modes
Nationwide route coverage
```

---

# 85. Future Database Extensions

The schema can later be extended with:

```text
users
saved_journeys
community_reports
notifications
route_geometry
location_aliases
transport_associations
driver_information
vehicle_information
language_translations
voice_content
```

These should be introduced only when the corresponding product features are approved.

---

# 86. Translation Data

The application should eventually support multiple South African languages.

The initial schema does not need every entity duplicated per language.

A future translation system may use:

```text
translation_keys
translations
```

or application-level i18n files for interface text.

Route and location names may require a more specific localisation strategy later.

The MVP should keep this separate from the core route schema.

---

# 87. Data Quality Principle

A smaller database containing:

```text
20 reliable routes
```

is preferable to a database containing:

```text
2,000 poorly supported routes
```

that gives commuters misleading information.

The database should therefore optimise for:

```text
Accuracy
Traceability
Freshness
Clarity
```

rather than raw record count.

---

# 88. Schema Acceptance Criteria

The backend schema is acceptable for MVP implementation when:

### Locations

* Locations can be created and searched.
* Locations support geographic coordinates.
* Locations can be activated/deactivated.

### Taxi Ranks

* Taxi ranks can belong to locations.
* Taxi ranks can store coordinates.
* Taxi ranks can have verification information.

### Routes

* Routes have origin and destination.
* Routes can reference boarding/destination ranks.
* Routes have verification status.
* Routes can be deactivated.

### Route Steps

* Steps are ordered.
* Steps describe the commuter journey.
* Steps can represent boarding, travel, getting off and transfers.

### Fares

* Fares are stored per route.
* Currency is ZAR.
* Negative fares are impossible.
* Historical validity can be preserved.
* Missing fares remain unavailable rather than becoming zero.

### Journeys

* Direct journeys can contain one route.
* Multi-leg journeys can contain multiple explicit route legs.
* Transfer information is stored explicitly.
* Arbitrary route combinations are not generated.

### Verification

* Routes and journeys have verification states.
* Last verified dates can be stored.
* Data sources can be recorded.

### Administration

* Admin users can manage the dataset.
* Important changes can be audited.

### Integrity

* Foreign keys prevent broken relationships.
* Unique constraints prevent duplicate step/leg ordering.
* Indexes support common search operations.

---

# 89. Example End-to-End Data Structure

A complete direct journey may look like:

```text
LOCATION
Tladi
    │
    └── TAXI RANK
        Tladi Taxi Rank
              │
              ▼
           ROUTE
        Tladi → Bara
              │
       ┌──────┴──────┐
       ▼             ▼
 ROUTE STEPS       FARE
                  R20 ZAR
       │
       ▼
 VERIFICATION
   VERIFIED
       │
       ▼
   JOURNEY
 Tladi → Bara
       │
       ▼
   JOURNEY LEG
        #1
       │
       ▼
 Tladi → Bara Route
```

---

# 90. Example Multi-Leg Data Structure

A curated multi-leg journey may look like:

```text
JOURNEY
Vaal → Midrand
      │
      ├── LEG 1
      │     │
      │     └── ROUTE
      │         Vaal → Johannesburg
      │
      │     TRANSFER
      │         Johannesburg
      │
      └── LEG 2
            │
            └── ROUTE
                Johannesburg → Midrand
```

Each component must exist as structured data.

---

# 91. Core Database Principle

The TaxiFind database should answer:

> "What journey information do we actually know and support?"

It should not attempt to answer:

> "What taxi journey might theoretically exist between these two points?"

This distinction is central to the MVP.

---

# 92. Relationship to the Previous Documents

The schema directly supports the previous product requirements.

### PRD

Defines:

```text
Supported routes
Verification
Fares
Taxi ranks
Controlled pilot coverage
```

### TRD

Defines:

```text
FastAPI
PostgreSQL
REST API
Structured route data
```

### Application Flow

Defines:

```text
Search
Results
Journey details
Transfers
Maps
```

### UI/UX Design Brief

Defines:

```text
Fare display
Duration display
Verification
Route steps
Transfer cards
No-result states
Admin management
```

This document provides the database structures required to make those features possible.

---

# 93. Final Schema Principle

The TaxiFind SA database should be:

```text
Structured
      +
Verifiable
      +
Traceable
      +
Expandable
      +
Conservative
```

The most important rule is:

> **If the database does not contain sufficiently supported information for a journey, the backend must return an unavailable/unsupported result rather than generate or infer the missing route information.**

This protects the credibility of the platform while allowing the dataset to grow gradually from a controlled Gauteng pilot into a broader transport information system.

---

# 94. Document Status

**Document:** Backend Schema
**Version:** 1.0
**Status:** Draft
**Previous Document:** UI/UX Design Brief
**Next Document:** Implementation Plan

This document establishes the database structure for the TaxiFind SA MVP. The next document will translate the PRD, TRD, application flow, UI/UX requirements, and backend schema into an ordered implementation plan covering project setup, database implementation, API development, frontend development, testing, data loading, administration, and deployment.
