# TaxiFind SA

## Application Flow Document

**Document Version:** 1.0
**Status:** Draft
**Project Type:** Web Application / Progressive Web App
**Initial Geographic Focus:** Gauteng, South Africa — controlled pilot
**Related Documents:**

* Project Requirements Document (PRD)
* Technical Requirements Document (TRD)

**Next Document:** UI/UX Design Brief

---

# 1. Document Purpose

This document defines how users move through the TaxiFind SA application.

It describes:

* User journeys
* Navigation
* Screen transitions
* Search behaviour
* Journey result behaviour
* Taxi transfer flows
* Map interactions
* Error and empty states
* Administrative workflows
* Future flows that are intentionally outside the MVP

The purpose is to ensure that the application has a clear and predictable user experience before UI development begins.

---

# 2. Core Application Principle

The primary task of TaxiFind SA is:

> Help a user understand how to travel from one supported location to another using minibus taxis.

The core application flow is:

```text
Open TaxiFind
      ↓
Enter From
      ↓
Enter To
      ↓
Search
      ↓
View Journey Options
      ↓
Select Journey
      ↓
Understand Journey Steps
      ↓
View Fare / Time / Transfers
      ↓
View Map
```

The user should be able to complete this journey without creating an account.

---

# 3. Primary User Flow

## 3.1 Complete Journey

```text
┌───────────────────┐
│   Open TaxiFind   │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│   Home / Search   │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│ Select "From"     │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│ Select "To"       │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│      Search       │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│ Journey Results   │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│ Journey Details   │
└─────────┬─────────┘
          ↓
┌───────────────────┐
│ Map / Route Info  │
└───────────────────┘
```

---

# 4. Application Navigation

The MVP public navigation should remain simple.

Recommended navigation:

```text
Home
Routes
Taxi Ranks
About
Language
```

On mobile, navigation may be represented through a menu.

The primary action should always remain accessible:

```text
Find a Taxi Journey
```

---

# 5. Home Screen Flow

The Home screen is the primary entry point.

## 5.1 Purpose

The Home screen should immediately communicate:

* What TaxiFind does
* That it provides minibus taxi journey information
* Where the user can search

The main interface should prioritise journey search.

---

# 6. Home Screen Structure

Conceptually:

```text
┌─────────────────────────────────┐
│          TaxiFind SA            │
│                                 │
│  Find your minibus taxi route   │
│                                 │
│  FROM                           │
│  ┌───────────────────────────┐  │
│  │ Where are you starting?   │  │
│  └───────────────────────────┘  │
│                                 │
│  TO                             │
│  ┌───────────────────────────┐  │
│  │ Where are you going?      │  │
│  └───────────────────────────┘  │
│                                 │
│       [ Find My Journey ]       │
│                                 │
└─────────────────────────────────┘
```

---

# 7. Origin Selection Flow

When the user selects the **From** field:

```text
From
 ↓
Search locations
 ↓
Show suggestions
 ↓
User selects location
 ↓
Location populated
```

Example:

```text
User enters:

Tla

Suggestions:

Tladi
Tladi Taxi Rank
```

The user selects the appropriate location.

---

# 8. Destination Selection Flow

The destination behaves similarly.

```text
To
 ↓
Search locations
 ↓
Show suggestions
 ↓
User selects destination
 ↓
Destination populated
```

Example:

```text
User enters:

Bar

Suggestions:

Bara
Bara Hospital
Bara Taxi Rank
```

The user selects the relevant destination.

---

# 9. Search Validation

Before the search is submitted, the application should check:

### Origin selected

Required.

### Destination selected

Required.

### Origin and destination different

The system should prevent:

```text
Tladi → Tladi
```

unless there is a legitimate reason for such a search.

### Supported locations

The selected locations should exist in the supported dataset.

---

# 10. Search Button

The primary action should be:

```text
Find My Journey
```

When selected:

```text
Search form
     ↓
Loading state
     ↓
Journey API
     ↓
Results
```

The button should provide feedback while the request is processing.

Example:

```text
Finding taxi routes...
```

---

# 11. Search Results Flow

After a successful search:

```text
Home/Search
     ↓
Journey Results
```

The results page should show the selected journey:

```text
Tladi
  ↓
Bara
```

Then display supported journey options.

---

# 12. Journey Result Card

Each journey option should provide enough information for the user to understand the basic journey.

Example:

```text
┌─────────────────────────────────┐
│ Tladi → Bara                    │
│                                 │
│ 🚕 Direct taxi                  │
│                                 │
│ Estimated fare                  │
│ R20                             │
│                                 │
│ Estimated time                  │
│ 30–40 min                       │
│                                 │
│ Taxi changes                    │
│ 0                               │
│                                 │
│ ✓ Verified                      │
│ Last verified: 15 Sep 2026      │
│                                 │
│ [ View Journey ]                │
└─────────────────────────────────┘
```

The actual visual design will be defined in the UI/UX document.

---

# 13. Multiple Journey Results

A search may return multiple supported journeys.

Example:

```text
Tladi → Bara

Journey 1
Direct
R20
35 min

Journey 2
1 taxi change
R30
50–60 min
```

The application should present the options without automatically declaring one universally "best."

Users can select the journey that is appropriate for them.

---

# 14. No Route Found Flow

If no supported route exists:

```text
Search
  ↓
No matching journey
```

The application should display a clear message.

Example:

```text
No supported taxi journey found.

We don't currently have verified journey
information for Tladi → Midrand.

Try another location or search area.
```

The application must not invent a route.

---

# 15. Partial Location Match

If the user enters an incomplete location:

```text
Tla
```

the system should show suggestions.

The user should select an actual supported location before searching.

The application should avoid silently interpreting an ambiguous place name.

---

# 16. Journey Details Flow

When a user selects:

```text
View Journey
```

the application navigates to:

```text
Journey Details
```

The page should explain the journey in a logical order.

Recommended order:

```text
Origin
 ↓
Where to catch taxi
 ↓
Taxi route
 ↓
Where to get off
 ↓
Transfer
 ↓
Next taxi
 ↓
Destination
```

---

# 17. Direct Journey Flow

For a direct journey:

```text
Tladi
 ↓
Tladi Taxi Rank
 ↓
Take taxi to Bara
 ↓
Bara Taxi Rank
 ↓
Bara
```

The interface should clearly distinguish:

* Where the user starts
* Where to catch the taxi
* Which taxi route to look for
* Where to get off

---

# 18. Multi-Taxi Journey Flow

For a journey requiring multiple taxis:

```text
Origin
 ↓
Taxi Rank A
 ↓
Taxi 1
 ↓
Transfer
 ↓
Taxi Rank B
 ↓
Taxi 2
 ↓
Taxi Rank C
 ↓
Destination
```

The application should clearly mark the transfer.

Example:

```text
STEP 1

Walk to Tladi Taxi Rank

        ↓

STEP 2

Take a taxi to Bara / Transfer Rank

        ↓

CHANGE TAXI

Get off at Bara Transfer Rank

        ↓

STEP 3

Take the next taxi toward destination

        ↓

ARRIVE
```

---

# 19. Transfer Information

Transfers should be highly visible.

A transfer should communicate:

1. Where to get off.
2. Where to find the next taxi.
3. Which destination/route to look for.
4. Estimated additional fare where available.
5. Estimated additional time where available.

Example:

```text
CHANGE TAXI

Get off at:
Johannesburg CBD Rank

Then:

Take a taxi toward:
Midrand

Additional estimated fare:
R18
```

---

# 20. Fare Display Flow

Fare information should appear in:

* Search results
* Journey details

Example:

```text
Estimated fare

R20
```

For a multi-leg journey:

```text
Estimated total fare

R38

Taxi 1: R20
Taxi 2: R18
```

The interface must clearly identify the amount as an estimate.

---

# 21. Missing Fare Flow

If a supported journey does not have a current fare:

```text
Estimated fare

Currently unavailable
```

The system should not guess the amount.

Where appropriate:

```text
Fare information has not been verified.
```

---

# 22. Journey Duration Flow

Journey duration should be displayed as an estimate.

Example:

```text
Estimated journey time

35–45 minutes
```

If no duration exists:

```text
Estimated time unavailable
```

The application must not imply a guaranteed arrival time.

---

# 23. Verification Information

The user should be able to understand the status of route information.

Example:

```text
✓ Verified

Last verified:
15 September 2026
```

Other possible states:

```text
Community Reported
Unverified
Outdated
Unavailable
```

The interface should use both text and visual indicators rather than colour alone.

---

# 24. Map Flow

The journey details page should include access to a map.

Possible layout:

```text
Journey Details
      ↓
Journey Steps
      ↓
[ View Map ]
      ↓
Map
```

The map should show relevant journey locations.

---

# 25. Map Information

The map may display:

```text
Origin
   ●

Taxi Rank
   ●

Transfer Rank
   ●

Destination
   ●
```

The map should not imply that the displayed line represents the exact path of the taxi unless reliable route geometry exists.

If only locations are known, the map should display the locations without inventing a precise road route.

---

# 26. Taxi Rank Flow

Users should be able to select a taxi rank from journey information.

Example:

```text
Tladi Taxi Rank
```

opens:

```text
Taxi Rank Details

Name
Tladi Taxi Rank

Area
Tladi

Location
Map

Routes
→ Bara
→ Johannesburg
```

---

# 27. Taxi Rank Details

The taxi rank page should contain:

* Rank name
* Area
* Address where available
* Coordinates
* Map
* Associated supported routes
* Operating information where reliable
* Verification status where applicable

---

# 28. Nearby Taxi Rank Flow

Nearby taxi ranks are optional within the MVP.

If implemented:

```text
User selects:

Find nearby taxi ranks
        ↓
Browser requests location permission
        ↓
User allows
        ↓
Application retrieves approximate position
        ↓
API searches nearby supported ranks
        ↓
Nearby ranks displayed
```

If permission is denied:

```text
Location access was not enabled.

You can search for a taxi rank manually.
```

The application must remain usable without location permission.

---

# 29. Location Permission Principles

The application must not request location access simply when the user opens the website.

Location should only be requested when a user explicitly activates a feature that requires it.

Example:

```text
[ Find Taxi Ranks Near Me ]
```

is an appropriate point to request permission.

---

# 30. Route Search from Taxi Rank

A user viewing a taxi rank may select a route.

Example:

```text
Tladi Taxi Rank

Available routes:

[ Bara ]
[ Johannesburg ]
```

Selecting a route opens the relevant journey information.

---

# 31. Global Search Behaviour

The application should support location search consistently across:

* Home
* Journey search
* Taxi rank pages
* Route pages

Search suggestions should use the same underlying location API.

This prevents different parts of the application from returning inconsistent location results.

---

# 32. Navigation Back Behaviour

Users should be able to return through their journey.

Example:

```text
Journey Details
      ↑
Search Results
      ↑
Search
      ↑
Home
```

Browser back navigation should also work correctly.

---

# 33. Search Persistence

For the MVP, search history does not need to be stored in an account.

However, the current search state may remain available during the current session to improve navigation.

Example:

```text
Tladi → Bara
```

should remain available when the user returns from journey details to results.

Persistent saved journeys are outside the MVP.

---

# 34. Language Selection Flow

The application should provide a language selector.

Example:

```text
Language
   ↓
English
isiZulu
isiXhosa
...
```

The initial release may provide English as the complete translation.

The architecture should allow additional languages to be enabled as translations become available.

---

# 35. Language Switching

When the user changes language:

```text
Current language
       ↓
Select language
       ↓
Load translation
       ↓
Update interface
```

The application should not require the user to restart the search.

Transport names should remain appropriate to their official/local names rather than being blindly translated.

---

# 36. Accessibility Flow

Accessibility should be incorporated into every screen.

For example, the search flow must be usable with:

```text
Keyboard
Screen reader
Touch
Responsive display
```

A user should not be required to interact with the map to understand a journey.

The journey must always have a text-based representation.

---

# 37. Error Handling Flow

General error:

```text
User action
 ↓
API request
 ↓
Failure
 ↓
Friendly error message
 ↓
Retry / alternative action
```

Example:

```text
Something went wrong.

We couldn't load this journey.

[ Try Again ]
```

Technical error details should not be shown to ordinary users.

---

# 38. Network Failure Flow

If the API cannot be reached:

```text
Unable to connect.

Please check your internet connection
and try again.
```

The application should not display stale or fabricated route information as if it were current.

---

# 39. API Timeout Flow

If the backend takes too long:

```text
This is taking longer than expected.

[ Try Again ]
```

The interface should not remain permanently stuck on a loading spinner.

---

# 40. Map Failure Flow

If the map service fails:

```text
Map temporarily unavailable.

Your journey information is still available.
```

The journey steps remain accessible.

---

# 41. Admin Flow

The administrator flow is separate from the public commuter flow.

```text
Admin Login
      ↓
Admin Dashboard
      ↓
Select Data Type
      ↓
View Records
      ↓
Create / Edit
      ↓
Validate
      ↓
Save
      ↓
Updated Public Data
```

---

# 42. Admin Login

Administrators should access a protected login page.

```text
Admin Login

Email
[                    ]

Password
[                    ]

[ Sign In ]
```

Authentication errors should be displayed without exposing sensitive information.

---

# 43. Admin Dashboard

The dashboard should provide access to:

```text
Locations
Taxi Ranks
Routes
Route Steps
Fares
Verification
```

The dashboard does not need complex analytics in the MVP.

---

# 44. Admin Location Management

Flow:

```text
Locations
 ↓
View locations
 ↓
Create / Edit location
 ↓
Enter information
 ↓
Validate
 ↓
Save
```

Required information should include appropriate:

* Name
* Type
* Geographic information
* Administrative area

---

# 45. Admin Taxi Rank Management

Flow:

```text
Taxi Ranks
 ↓
Select rank
 ↓
Edit
 ↓
Update:
    Name
    Location
    Coordinates
    Description
    Routes
 ↓
Save
```

The administrator should be warned before destructive actions.

---

# 46. Admin Route Management

Flow:

```text
Routes
 ↓
Create / Edit route
 ↓
Select origin
 ↓
Select destination
 ↓
Define route steps
 ↓
Set status
 ↓
Set verification status
 ↓
Save
```

The system should prevent invalid location relationships.

---

# 47. Admin Route Step Management

A route may contain multiple steps.

Example:

```text
Route:
Tladi → Midrand

Step 1
Tladi → Johannesburg

Step 2
Johannesburg → Midrand
```

Administrators should be able to:

* Add steps
* Remove steps
* Reorder steps
* Define transfer locations
* Add journey instructions

---

# 48. Admin Fare Management

Flow:

```text
Fares
 ↓
Select route
 ↓
Add / Edit fare
 ↓
Enter amount
 ↓
Enter effective date
 ↓
Set verification status
 ↓
Save
```

The system should validate that the fare is a valid positive monetary amount.

---

# 49. Admin Verification Flow

Administrators should be able to change information status.

Example:

```text
Route
 ↓
Review information
 ↓
Verify
 ↓
Set:
Verified
 ↓
Set:
Last Verified Date
 ↓
Save
```

Alternatively:

```text
Route
 ↓
Review
 ↓
Mark Outdated
 ↓
Update status
```

---

# 50. Public Data Update Flow

Once an administrator saves a change:

```text
Admin
 ↓
Backend validation
 ↓
Database update
 ↓
Updated public API
 ↓
User sees updated information
```

The application should not require manual frontend code changes to update route or fare information.

---

# 51. Admin Audit Consideration

Important administrator actions should be logged.

Examples:

```text
Admin created route
Admin changed fare
Admin marked route outdated
Admin verified taxi rank
```

The detailed audit implementation will be finalised during backend development.

---

# 52. Public vs Admin Boundary

The application should clearly separate:

```text
PUBLIC
│
├── Search
├── Routes
├── Taxi Ranks
├── Journey Details
└── Maps
```

from:

```text
ADMIN
│
├── Dashboard
├── Locations
├── Taxi Ranks
├── Routes
├── Route Steps
├── Fares
└── Verification
```

A public user must not have access to administrative functionality.

---

# 53. Complete Public Journey Example

Example:

```text
USER OPENS TAXIFIND
        ↓
HOME
        ↓
FROM: Tladi
        ↓
TO: Bara
        ↓
FIND MY JOURNEY
        ↓
SEARCHING...
        ↓
RESULTS
        ↓
Tladi → Bara
        ↓
Estimated fare: R20
Estimated time: 35–40 min
Taxi changes: 0
Status: Verified
        ↓
VIEW JOURNEY
        ↓
JOURNEY DETAILS
        ↓
Walk to Tladi Taxi Rank
        ↓
Take taxi toward Bara
        ↓
Get off at Bara Taxi Rank
        ↓
Arrive at Bara
        ↓
VIEW MAP
```

---

# 54. Complete Multi-Taxi Example

Example:

```text
USER
 ↓
FROM: Vaal
 ↓
TO: Midrand
 ↓
SEARCH
 ↓
RESULTS
 ↓
Journey Option
 ↓
Estimated fare: RXX
Estimated time: XX–XX min
Taxi changes: 1
 ↓
VIEW JOURNEY
 ↓
STEP 1
Travel to first taxi rank
 ↓
STEP 2
Take taxi toward transfer point
 ↓
TRANSFER
 ↓
STEP 3
Find taxi toward Midrand
 ↓
STEP 4
Get off at destination rank
 ↓
ARRIVE
 ↓
MAP
```

Actual route and fare values must only be shown when supported by the database.

---

# 55. Unsupported Journey Example

```text
USER
 ↓
FROM: Supported Location
 ↓
TO: Unsupported Location
 ↓
SEARCH
 ↓
NO SUPPORTED ROUTE
```

Display:

```text
We don't currently have supported taxi
journey information for this trip.

Try another destination or search area.
```

The system must not attempt to construct an imaginary journey.

---

# 56. MVP Flow Boundary

The following flows are included:

| Flow                     |                   MVP |
| ------------------------ | --------------------: |
| Open application         |                     ✅ |
| Search from/to           |                     ✅ |
| Location suggestions     |                     ✅ |
| View journey results     |                     ✅ |
| View journey details     |                     ✅ |
| Direct taxi journey      |                     ✅ |
| Multi-taxi journey       |                     ✅ |
| Transfer instructions    |                     ✅ |
| Fare information         |                     ✅ |
| Journey duration         |                     ✅ |
| Verification information |                     ✅ |
| Taxi rank details        |                     ✅ |
| Map                      |                     ✅ |
| Nearby taxi ranks        |              Optional |
| Language selector        | Architecture required |
| English interface        |                     ✅ |
| Admin login              |                     ✅ |
| Admin locations          |                     ✅ |
| Admin taxi ranks         |                     ✅ |
| Admin routes             |                     ✅ |
| Admin route steps        |                     ✅ |
| Admin fares              |                     ✅ |
| Admin verification       |                     ✅ |
| User registration        |                     ❌ |
| Saved journeys           |                     ❌ |
| Community reports        |                     ❌ |
| AI search                |                     ❌ |
| Voice search             |                     ❌ |
| Live tracking            |                     ❌ |
| Booking                  |                     ❌ |
| Payments                 |                     ❌ |
| Push notifications       |                     ❌ |
| Offline mode             |                     ❌ |
| Other transport modes    |                     ❌ |

---

# 57. Future Application Flows

The following should be designed later rather than implemented in the MVP.

## AI Journey Assistant

```text
Natural language request
        ↓
AI interpretation
        ↓
Structured TaxiFind API
        ↓
Verified route information
        ↓
Natural language response
```

## Community Reporting

```text
User
 ↓
Report issue
 ↓
Moderation
 ↓
Verification
 ↓
Administrator review
 ↓
Public information update
```

## Saved Journeys

```text
User Login
 ↓
Search Journey
 ↓
Save Journey
 ↓
My Journeys
```

## Notifications

```text
User follows route
 ↓
Transport update
 ↓
Notification
```

These are not part of the MVP.

---

# 58. Core UX Rules

The following rules should guide implementation.

### Rule 1 — Search First

The primary purpose of the Home page should be journey search.

### Rule 2 — Don't Require an Account

A user must be able to search without registration.

### Rule 3 — Never Invent a Route

Unsupported information must be clearly identified.

### Rule 4 — Explain Transfers

If a journey requires changing taxis, the transfer must be explicit.

### Rule 5 — Show Fare Status

Users should know whether fare information is current/verified.

### Rule 6 — Show Time as an Estimate

The application must not promise an exact travel duration.

### Rule 7 — Map Is Supporting Information

The textual journey instructions must remain usable without the map.

### Rule 8 — Mobile First

The journey should be easy to complete on a smartphone.

### Rule 9 — Minimise Steps

A user should ideally reach useful journey information within a few interactions.

### Rule 10 — Don't Hide Coverage Limitations

If a route is not supported, the application should explain that the information is not currently available rather than implying the route does not exist.

---

# 59. Primary User Journey Success Condition

The primary flow is successful when a user can answer these questions:

1. Where do I start?
2. Where do I catch the taxi?
3. Which taxi route should I take?
4. Where do I get off?
5. Do I need to change taxis?
6. Where do I change?
7. How much should I expect to pay?
8. How long might the journey take?
9. Where are the relevant taxi ranks?
10. How reliable/current is this information?

If the application answers these questions clearly, the core MVP journey is functioning as intended.

---

# 60. Document Status

**Document:** Application Flow Document
**Version:** 1.0
**Status:** Draft
**Previous Document:** Technical Requirements Document
**Next Document:** UI/UX Design Brief

This document establishes the user and administrator flows that the TaxiFind SA MVP must support. The next document will translate these flows into concrete screen layouts, visual hierarchy, components, responsive behaviour, accessibility requirements, and design-system guidance.
