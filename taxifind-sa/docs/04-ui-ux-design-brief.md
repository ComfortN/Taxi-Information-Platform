# TaxiFind SA

## UI/UX Design Brief

**Document Version:** 1.0
**Status:** Draft
**Project Type:** Web Application / Progressive Web App
**Initial Geographic Focus:** Gauteng, South Africa — controlled pilot

**Related Documents:**

* Project Requirements Document (PRD)
* Technical Requirements Document (TRD)
* Application Flow Document

**Next Document:** Backend Schema

---

# 1. Document Purpose

This document defines the visual and interaction design direction for TaxiFind SA.

It translates the requirements and application flows into:

* Screen layouts
* Visual hierarchy
* Navigation
* Components
* Responsive behaviour
* Search interfaces
* Journey result cards
* Journey detail layouts
* Map presentation
* Taxi rank interfaces
* Verification indicators
* Admin interfaces
* Accessibility requirements
* Mobile-first behaviour
* Design-system guidance

The goal is to create an interface that is simple enough for a first-time commuter to understand without requiring technical knowledge.

---

# 2. Core UX Objective

The primary UX objective is:

> Help a commuter quickly understand how to travel from one supported location to another using minibus taxis.

The interface should answer:

1. Where do I start?
2. Where do I catch the taxi?
3. Which taxi should I take?
4. Where do I get off?
5. Do I need to change taxis?
6. Where do I change?
7. How much should I expect to pay?
8. How long might the journey take?
9. Where is the relevant taxi rank?
10. How reliable/current is the information?

---

# 3. Design Principles

## 3.1 Search First

The journey search should be the most prominent action on the Home screen.

The user should not have to navigate through multiple pages before starting a search.

---

## 3.2 Mobile First

The majority of commuter interactions are expected to occur on smartphones.

Design should therefore begin with:

```text
Mobile
 ↓
Tablet
 ↓
Desktop
```

rather than designing desktop first and shrinking the interface afterwards.

---

## 3.3 Simple Language

The interface should use plain language.

Prefer:

```text
Where are you going?
```

instead of:

```text
Enter destination coordinates.
```

Prefer:

```text
Change taxi
```

instead of:

```text
Transfer to another transport service.
```

---

## 3.4 Never Hide Important Information

Important journey information should not be hidden behind unnecessary interactions.

The user should easily see:

* Fare
* Estimated time
* Taxi changes
* Verification status
* Journey steps

---

## 3.5 Never Invent Information

The interface must clearly distinguish between:

```text
Known
Estimated
Unavailable
```

For example:

```text
Estimated fare
R20
```

is preferable to displaying:

```text
Fare
R20
```

when the amount is not guaranteed.

---

## 3.6 Map as Supporting Information

The map should support the written journey instructions.

A user must still understand the journey if:

* The map does not load
* The user has poor connectivity
* The user uses a screen reader
* The user cannot easily interact with the map

---

## 3.7 Local Context

TaxiFind should feel appropriate for South African commuters.

The interface should accommodate:

* Township names
* Suburbs
* Cities
* Taxi ranks
* Informal/local place names
* Common destination names
* South African Rand (ZAR)
* Local terminology

---

# 4. Target Users

The MVP primarily serves people who need information about a minibus taxi journey.

### Primary

* Daily commuters
* Students
* Workers
* New or occasional commuters
* People travelling between areas they do not know well

### Secondary

* Visitors
* People unfamiliar with local taxi routes

### Administrative

* TaxiFind administrators responsible for maintaining route information

The MVP does not require separate driver, taxi association or operator interfaces.

---

# 5. Visual Design Direction

The visual identity should communicate:

```text
Reliable
Simple
Local
Accessible
Modern
Practical
```

The interface should avoid looking like:

* A ride-hailing application
* A banking application
* A social network
* A complicated GIS system

TaxiFind is primarily an **information and navigation product**.

---

# 6. Colour System

A simple design system should be used consistently.

Suggested primary palette:

| Role           | Suggested Colour   |
| -------------- | ------------------ |
| Primary        | Deep blue          |
| Primary action | Blue               |
| Accent         | Warm yellow/orange |
| Success        | Green              |
| Warning        | Amber              |
| Error          | Red                |
| Background     | Very light neutral |
| Surface        | White              |
| Primary text   | Dark charcoal      |
| Secondary text | Neutral grey       |
| Border         | Light grey         |

The exact hexadecimal values should be finalised during implementation.

Colour must never be the only method of communicating status.

For example:

```text
✓ Verified
```

should not be represented only by a green colour.

---

# 7. Typography

The interface should use a clean, highly readable sans-serif font.

Typography should prioritise:

* Readability
* Clear hierarchy
* Large touch-friendly labels
* High contrast
* Comfortable line spacing

Suggested hierarchy:

```text
H1
Page title

H2
Section heading

H3
Card heading

Body
Normal information

Small
Metadata / verification details
```

The exact font family can be selected during implementation.

---

# 8. Spacing System

A consistent spacing scale should be used.

Example:

```text
4px
8px
12px
16px
24px
32px
48px
64px
```

Most mobile components should use approximately:

```text
16px
```

horizontal page padding.

---

# 9. Border Radius

The application should use moderate rounded corners.

Suggested:

```text
Inputs: 8–12px
Cards: 12–16px
Buttons: 8–12px
Badges: pill/rounded
```

The interface should avoid excessive rounded elements that make the application look like a collection of floating bubbles.

---

# 10. Shadows

Shadows should be subtle.

Cards should primarily rely on:

* Borders
* Spacing
* Background contrast

rather than heavy shadows.

---

# 11. Application Layout

The public application should follow:

```text
┌──────────────────────────────────────────┐
│ Header                                   │
├──────────────────────────────────────────┤
│                                          │
│ Main Content                             │
│                                          │
│                                          │
├──────────────────────────────────────────┤
│ Footer                                   │
└──────────────────────────────────────────┘
```

On mobile:

```text
┌──────────────────────┐
│ Logo        Menu     │
├──────────────────────┤
│                      │
│ Content              │
│                      │
│                      │
└──────────────────────┘
```

---

# 12. Header

The desktop header should contain:

```text
TaxiFind SA

Home
Routes
Taxi Ranks
About

Language
```

The primary search action may also be accessible from the header.

---

# 13. Mobile Header

The mobile header should contain:

```text
TaxiFind SA                         ☰
```

Opening the menu should reveal:

```text
Home
Routes
Taxi Ranks
About
Language
```

The menu should be keyboard and screen-reader accessible.

---

# 14. Home Screen

The Home screen is the most important public screen.

Recommended structure:

```text
┌────────────────────────────────────┐
│ TaxiFind SA                        │
│                                    │
│ Find your taxi journey             │
│                                    │
│ From                               │
│ ┌────────────────────────────────┐ │
│ │ Where are you starting?        │ │
│ └────────────────────────────────┘ │
│                                    │
│ To                                 │
│ ┌────────────────────────────────┐ │
│ │ Where are you going?           │ │
│ └────────────────────────────────┘ │
│                                    │
│ ┌────────────────────────────────┐ │
│ │      Find My Journey            │ │
│ └────────────────────────────────┘ │
│                                    │
│ Selected Gauteng routes            │
│                                    │
└────────────────────────────────────┘
```

The coverage message should make the pilot scope clear without dominating the interface.

---

# 15. Search Component

The search component should consist of:

```text
From
To
Search button
```

Each location field should support:

* Typing
* Suggestions
* Selection
* Clearing
* Keyboard navigation

---

# 16. Location Suggestions

When the user types:

```text
Tla
```

the interface may display:

```text
Suggested locations

Tladi
Tladi Taxi Rank
```

Each suggestion should identify its type where useful.

Example:

```text
Tladi
Area

Tladi Taxi Rank
Taxi Rank
```

This reduces ambiguity between similarly named locations.

---

# 17. Search Input States

Each search input should support:

### Default

```text
Where are you starting?
```

### Focused

Clear visual focus indicator.

### Typing

Display matching suggestions.

### Selected

```text
Tladi
```

### Error

```text
Please select a starting location.
```

### Loading

Display suggestion loading feedback.

---

# 18. Swap Locations

A swap control may be included:

```text
From: Tladi
To: Bara

        ⇅
```

Selecting it changes:

```text
From: Bara
To: Tladi
```

The control must remain accessible on small screens.

---

# 19. Search Loading State

When searching:

```text
Find My Journey
        ↓
Finding taxi routes...
```

The interface should:

* Disable duplicate submissions
* Show progress
* Maintain the selected locations
* Restore the button after completion

---

# 20. Results Page

The results page should begin with:

```text
Your journey

Tladi → Bara
```

A back/edit option should allow the user to change the search.

---

# 21. Results Layout

Desktop:

```text
┌───────────────────────┬─────────────────────┐
│ Journey Results       │ Optional Map        │
│                       │                     │
│ Journey Card          │                     │
│                       │                     │
│ Journey Card          │                     │
│                       │                     │
└───────────────────────┴─────────────────────┘
```

Mobile:

```text
Journey
Tladi → Bara

Journey Card

Journey Card
```

The map may be moved below the results on smaller screens.

---

# 22. Journey Result Card

A result card should contain:

```text
Tladi → Bara

Direct taxi

Estimated fare
R20

Estimated time
35–40 min

Taxi changes
0

✓ Verified
Last verified 15 Sep 2026

[ View Journey ]
```

The card should not overwhelm the user with technical database information.

---

# 23. Journey Summary Metadata

Important information should be visually grouped.

Example:

```text
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Fare         │ │ Time         │ │ Changes      │
│ R20          │ │ 35–40 min    │ │ 0            │
└──────────────┘ └──────────────┘ └──────────────┘
```

On very small screens, these may stack vertically.

---

# 24. Verification Badge

Verification should be represented using:

```text
✓ Verified
```

or:

```text
! Unverified
```

or:

```text
⚠ Outdated
```

The visual treatment should be supplemented with text.

Users should be able to understand what the status means.

---

# 25. No Results Screen

The no-results screen should be helpful rather than alarming.

Example:

```text
No supported taxi journey found

We don't currently have supported taxi
journey information for:

Tladi → Midrand

This doesn't necessarily mean that no taxi
journey exists.

Try another location or search area.

[ Change Search ]
```

This distinction is important because the database is a controlled pilot dataset.

---

# 26. Journey Details Page

The journey details page should be structured as a clear sequence.

```text
Tladi → Bara

Estimated fare: R20
Estimated time: 35–40 min
Taxi changes: 0

✓ Verified

JOURNEY

1. Start
2. Catch taxi
3. Travel
4. Get off
5. Arrive

MAP
```

---

# 27. Journey Timeline

The journey should use a visual timeline.

Example:

```text
● Start
│
│ Walk to Tladi Taxi Rank
│
● Catch taxi
│
│ Take taxi toward Bara
│
● Get off
│
│ Bara Taxi Rank
│
● Destination
```

The timeline should remain understandable without relying on colour.

---

# 28. Direct Journey Timeline

Example:

```text
● Tladi
│
│ Walk to
│
● Tladi Taxi Rank
│
│ Take taxi toward Bara
│
● Bara Taxi Rank
│
● Bara
```

Each step should include a clear action.

---

# 29. Multi-Taxi Journey Timeline

Example:

```text
● Vaal
│
● Taxi Rank A
│
│ Take taxi
│
● Transfer Rank
│
│ CHANGE TAXI
│
● Taxi Rank B
│
│ Take taxi
│
● Midrand
```

The transfer point should receive strong visual emphasis.

---

# 30. Transfer Card

Example:

```text
CHANGE TAXI

Get off at:
Johannesburg CBD Rank

Then find a taxi going toward:
Midrand

Additional estimated fare:
R18

Additional estimated time:
20–30 min
```

If any information is unavailable:

```text
Additional fare
Unavailable
```

The application must not fill the missing value with a guess.

---

# 31. Fare Presentation

Fare information should use South African Rand.

Example:

```text
Estimated fare

R20
```

For multi-leg journeys:

```text
Estimated total fare

R38

Taxi 1     R20
Taxi 2     R18
```

The word **Estimated** should remain visible.

---

# 32. Duration Presentation

Example:

```text
Estimated journey time

35–45 minutes
```

Avoid presenting:

```text
Arrival: 14:35
```

because the application does not provide live journey prediction.

---

# 33. Map Component

The map should appear after or alongside the journey information.

Recommended mobile layout:

```text
Journey Steps
     ↓
Fare / Time
     ↓
Map
```

Desktop may use:

```text
Journey Information | Map
```

---

# 34. Map Controls

The map should provide standard controls where appropriate:

* Zoom in
* Zoom out
* Recenter
* Marker selection

The interface should avoid unnecessary map controls.

---

# 35. Map Markers

Markers should distinguish:

```text
Origin
Taxi Rank
Transfer
Destination
```

A legend may be provided where needed.

---

# 36. Map Accuracy Principle

The UI must not visually imply information that the backend does not actually know.

If the system knows:

```text
Tladi Rank coordinates
Bara Rank coordinates
```

but does not know the exact taxi road path, the map may show:

```text
● Tladi Rank

● Bara Rank
```

rather than drawing a fictional route.

---

# 37. Taxi Rank Page

The taxi rank page should contain:

```text
Tladi Taxi Rank

Area
Tladi

Address
Where available

Map

Supported routes

→ Bara
→ Johannesburg

Verification
✓ Verified
```

---

# 38. Taxi Rank Card

Taxi rank cards can be used in lists.

Example:

```text
┌─────────────────────────────┐
│ Tladi Taxi Rank             │
│ Tladi                       │
│                             │
│ Routes: Bara, Johannesburg  │
│                             │
│ [ View Rank ]               │
└─────────────────────────────┘
```

---

# 39. Routes Page

The Routes page provides an alternative way to browse supported routes.

Example:

```text
Supported Taxi Routes

Search routes...

Tladi → Bara
Soweto → Johannesburg
Vaal → Midrand
```

The page should clearly communicate that this is a list of supported TaxiFind data, not a complete list of every real-world taxi route.

---

# 40. Route Detail Page

A route detail page may show:

```text
Tladi → Bara

Origin
Tladi

Destination
Bara

Taxi Rank
Tladi Taxi Rank

Fare
Estimated R20

Duration
35–40 min

Verification
Verified

Last verified
15 September 2026
```

---

# 41. About Page

The About page should explain:

* What TaxiFind is
* What it is not
* Initial pilot coverage
* How route information is maintained
* Meaning of verification statuses
* Limitations of estimates
* How users should interpret unavailable routes

Important wording:

> TaxiFind provides information for selected supported minibus taxi journeys. If a journey is not currently listed, this does not necessarily mean that the journey does not exist.

---

# 42. Language Selector

The language selector should be accessible from the main navigation.

Example:

```text
Language

English
isiZulu
isiXhosa
Afrikaans
...
```

The application architecture should support all 11 official South African spoken languages over time.

The MVP does not require every translation to be complete before release.

---

# 43. Accessibility

Accessibility must be considered from the beginning rather than added later.

The application should support:

* Keyboard navigation
* Screen readers
* Visible focus states
* Semantic HTML
* Appropriate heading hierarchy
* Form labels
* Accessible error messages
* Sufficient colour contrast
* Touch-friendly controls
* Reduced motion where appropriate
* Text alternatives to map information

---

# 44. Touch Targets

Interactive controls should have sufficiently large touch areas.

Particular attention should be given to:

* Search fields
* Search suggestions
* Buttons
* Navigation menu
* Map controls
* Journey cards
* Transfer controls

Small text links should not be the only way to access important actions.

---

# 45. Screen Reader Considerations

A screen reader user should be able to understand:

```text
Journey from Tladi to Bara.

Direct taxi journey.

Estimated fare: 20 Rand.

Estimated duration: 35 to 40 minutes.

No taxi changes.

Verified on 15 September 2026.
```

The map should not be the only source of this information.

---

# 46. Error Message Design

Errors should explain:

```text
What happened
+
What the user can do
```

Good:

```text
We couldn't load the journey.

Please check your connection and try again.

[ Try Again ]
```

Avoid:

```text
Error 500
```

for ordinary users.

---

# 47. Empty State Design

Empty states should be informative.

Example:

```text
No supported routes yet

TaxiFind does not currently have verified
route information for this area.

Try searching another location.
```

---

# 48. Loading States

Loading states should be short and contextual.

Examples:

```text
Finding taxi routes...
```

```text
Loading journey...
```

```text
Loading taxi ranks...
```

Avoid generic full-screen loading indicators when only a small component is loading.

---

# 49. Responsive Breakpoints

The implementation should support at least:

```text
Mobile
320px+
```

```text
Tablet
768px+
```

```text
Desktop
1024px+
```

```text
Large Desktop
1280px+
```

Exact breakpoints can be adjusted during implementation.

---

# 50. Mobile Layout Rules

On mobile:

* Use one primary content column.
* Stack journey information vertically.
* Keep search fields full width.
* Keep primary buttons prominent.
* Avoid horizontal scrolling.
* Keep important information above the fold where practical.
* Place maps after essential journey instructions.
* Use expandable sections only where they reduce unnecessary complexity.

---

# 51. Desktop Layout Rules

Desktop can make better use of horizontal space.

For example:

```text
┌───────────────────────────┬─────────────────────┐
│ Journey information       │ Map                 │
│                           │                     │
│ Steps                     │                     │
│ Fare                      │                     │
│ Time                      │                     │
│ Verification              │                     │
└───────────────────────────┴─────────────────────┘
```

The map should not dominate the screen at the expense of journey instructions.

---

# 52. Component Design System

The frontend should establish reusable components.

Suggested components:

```text
Button
Input
LocationSearchInput
SearchForm
SearchSuggestion
JourneyCard
JourneySummary
JourneyTimeline
JourneyStep
TransferCard
FareCard
VerificationBadge
TaxiRankCard
RouteCard
MapView
EmptyState
ErrorState
LoadingState
Modal
Toast / Snackbar
Header
Footer
LanguageSelector
```

---

# 53. Button Hierarchy

### Primary

Used for the main action:

```text
Find My Journey
```

### Secondary

Used for supporting actions:

```text
View Map
Change Search
```

### Destructive

Used for administrative destructive actions:

```text
Delete
```

Destructive actions should require confirmation where appropriate.

---

# 54. Form Design

Forms should:

* Have visible labels
* Clearly identify required fields
* Provide inline validation
* Avoid relying solely on placeholders
* Preserve user input after validation errors
* Provide useful error messages

Example:

```text
From *
[ Tladi ]

To *
[                         ]

Please select a destination.
```

---

# 55. Notifications and Feedback

Short-lived feedback may use:

* Toasts
* Snackbars
* Inline status messages

Important information should not exist only in a temporary notification.

For example, a successful admin update may show:

```text
Route updated successfully.
```

but the updated route should also appear in the page.

---

# 56. Admin UI Design

The admin interface should prioritise efficient data management rather than visual complexity.

Desktop structure:

```text
┌───────────────┬──────────────────────────────┐
│ Sidebar       │ Main Content                 │
│               │                              │
│ Dashboard     │ Routes                       │
│ Locations     │                              │
│ Taxi Ranks    │ [ Add Route ]                │
│ Routes        │                              │
│ Route Steps   │ Route table                  │
│ Fares         │                              │
│ Verification  │                              │
└───────────────┴──────────────────────────────┘
```

---

# 57. Admin Dashboard

The MVP dashboard should focus on access to management areas.

Example:

```text
TaxiFind Admin

Locations       25
Taxi Ranks      14
Routes          32
Fares           31

Management

[ Locations ]
[ Taxi Ranks ]
[ Routes ]
[ Fares ]
[ Verification ]
```

These counts are illustrative.

Complex analytics are outside the MVP.

---

# 58. Admin Tables

Data-heavy admin screens should use tables on desktop.

Example:

```text
Routes

Origin       Destination      Status       Verified
----------------------------------------------------
Tladi        Bara             Verified     15 Sep
Vaal         Midrand          Outdated     10 Aug
...
```

On mobile, rows may transform into cards.

---

# 59. Admin Forms

Route creation should use a logical sequence:

```text
Route Name

Origin
[ Select location ]

Destination
[ Select location ]

Description
[                    ]

Verification Status
[ Verified ▼ ]

Source
[                    ]

Last Verified
[                    ]

[ Save Route ]
```

Route steps and fares can be managed after the basic route is created.

---

# 60. Admin Verification UI

Verification should be explicit.

Example:

```text
Route Status

● Verified
○ Community Reported
○ Unverified
○ Outdated
○ Unavailable
```

Changing verification status should be an intentional administrative action.

---

# 61. Confirmation Dialogs

Confirmation dialogs should be used for destructive or significant actions.

Example:

```text
Delete Route?

This will remove the route from the
TaxiFind public dataset.

[ Cancel ]   [ Delete ]
```

The interface should explain the consequence.

---

# 62. Data Status Visual Language

The following statuses should have consistent visual treatment:

| Status             | Meaning                                                 |
| ------------------ | ------------------------------------------------------- |
| Verified           | Information has been reviewed                           |
| Community Reported | Report exists but requires appropriate review           |
| Unverified         | Information has not been verified                       |
| Outdated           | Previously known information may no longer be current   |
| Unavailable        | Information should not currently be presented as usable |

Colour can reinforce these meanings but must not be the only indicator.

---

# 63. Content Rules

UI copy should follow these principles:

### Be direct

```text
Find My Journey
```

instead of:

```text
Click here to begin searching for your desired transportation route.
```

### Be honest about uncertainty

```text
Estimated fare
```

instead of:

```text
Fare
```

### Be transparent about coverage

```text
No supported taxi journey found.
```

instead of:

```text
No taxi available.
```

The second statement could incorrectly imply that no taxi exists.

---

# 64. Trust and Transparency

TaxiFind should make data confidence visible without overwhelming the user.

A journey could display:

```text
✓ Verified
Last verified:
15 September 2026
```

This gives users context about how current the information is.

---

# 65. Progressive Disclosure

The interface should show the most important information first.

### First level

```text
Origin
Destination
Fare
Time
Taxi changes
Verification
```

### Second level

```text
Detailed journey steps
Transfer information
Rank details
Map
```

### Third level

```text
Source
Data metadata
Additional verification information
```

This keeps the commuter experience simple while preserving transparency.

---

# 66. Search Accessibility

Search suggestions must support:

* Keyboard arrow navigation
* Enter to select
* Escape to close
* Screen reader announcements
* Touch selection

The selected location should be clearly distinguishable from suggestions.

---

# 67. Map Accessibility

The map must not be a required interaction.

The equivalent information should always be available as text.

Example:

```text
Map unavailable

Journey steps:

1. Start at Tladi.
2. Walk to Tladi Taxi Rank.
3. Take taxi toward Bara.
4. Get off at Bara Taxi Rank.
```

---

# 68. Performance UX

The interface should feel responsive even when API calls take time.

Use:

* Skeletons where appropriate
* Local loading states
* Optimistic UI only where safe
* Pagination for large admin lists
* Lazy loading for non-critical resources

The MVP should prioritise a fast search-to-result experience.

---

# 69. Security UX

Security-sensitive interfaces should avoid revealing unnecessary information.

For example, an admin login failure should not distinguish between:

```text
Email exists
```

and:

```text
Password incorrect
```

A generic message is preferable:

```text
Invalid email or password.
```

---

# 70. PWA Considerations

TaxiFind may eventually be installable as a Progressive Web App.

The design should therefore accommodate:

* Mobile browser use
* Home-screen installation
* Responsive layouts
* Appropriate application icons
* Browser-safe navigation

Offline functionality is **not part of the MVP**, so the UI must not imply that all route information is available without an internet connection.

---

# 71. Design System File Structure

The frontend may organise UI components approximately as:

```text
frontend/src/
├── components/
│   ├── common/
│   ├── search/
│   ├── journey/
│   ├── map/
│   ├── taxi-rank/
│   └── admin/
│
├── layouts/
│   ├── PublicLayout.tsx
│   └── AdminLayout.tsx
│
├── pages/
│   ├── Home/
│   ├── SearchResults/
│   ├── JourneyDetails/
│   ├── TaxiRanks/
│   ├── TaxiRankDetails/
│   ├── Routes/
│   ├── About/
│   └── admin/
│
└── styles/
    ├── tokens.css
    ├── globals.css
    └── utilities.css
```

The exact structure may be adjusted during implementation.

---

# 72. MVP Screen Inventory

The MVP should include approximately these public screens:

| Screen            |          MVP |
| ----------------- | -----------: |
| Home              |            ✅ |
| Search Results    |            ✅ |
| Journey Details   |            ✅ |
| Taxi Rank List    |            ✅ |
| Taxi Rank Details |            ✅ |
| Routes List       |            ✅ |
| Route Details     |            ✅ |
| About             |            ✅ |
| Language Selector | Architecture |
| No Results        |            ✅ |
| Error States      |            ✅ |

Admin:

| Screen       | MVP |
| ------------ | --: |
| Admin Login  |   ✅ |
| Dashboard    |   ✅ |
| Locations    |   ✅ |
| Taxi Ranks   |   ✅ |
| Routes       |   ✅ |
| Route Steps  |   ✅ |
| Fares        |   ✅ |
| Verification |   ✅ |

---

# 73. MVP UI Exclusions

The following should not be designed as active MVP features:

* Ride booking
* Payment screens
* Driver profiles
* Driver dashboards
* Live driver tracking
* Ride requests
* Push notification centre
* Social/community feed
* AI chat interface
* Voice assistant interface
* Saved journey dashboard
* Full offline experience
* Other transport modes

These may receive future design specifications.

---

# 74. Core Design Acceptance Criteria

The UI/UX implementation should be considered successful when:

### Search

* A user can identify From and To fields immediately.
* Location suggestions are understandable.
* Search errors are clear.
* Search does not require an account.

### Results

* Users can distinguish between journey options.
* Fare and duration are clearly labelled as estimates.
* Taxi changes are visible.
* Verification status is visible.

### Journey Details

* Users can understand where to start.
* Users can understand where to catch the taxi.
* Users can understand which direction/route to take.
* Users can understand where to get off.
* Transfers are clearly marked.
* Fare and time are visible.
* The map supports rather than replaces written instructions.

### Coverage

* Unsupported journeys are clearly identified.
* The interface does not imply that an unavailable route does not exist in reality.

### Accessibility

* Core search and journey information can be used without a mouse.
* Core journey information can be understood without the map.
* Colour is not the sole method of communicating meaning.

### Mobile

* The complete journey flow works comfortably on a smartphone.
* No horizontal scrolling is required.
* Buttons and controls are touch-friendly.

### Admin

* Administrators can manage the core dataset efficiently.
* Verification status is visible and editable.
* Public data can be updated without frontend code changes.

---

# 75. Recommended First UI Implementation Order

The frontend should be built in this order:

```text
1. Design tokens
       ↓
2. Global layout
       ↓
3. Header / navigation
       ↓
4. Home search
       ↓
5. Location suggestions
       ↓
6. Search results
       ↓
7. Journey card
       ↓
8. Journey details
       ↓
9. Journey timeline
       ↓
10. Fare / duration / verification
       ↓
11. Map
       ↓
12. Taxi rank pages
       ↓
13. Routes pages
       ↓
14. Error / empty / loading states
       ↓
15. Accessibility refinement
       ↓
16. Responsive refinement
       ↓
17. Admin interface
```

---

# 76. Final UX Principle

TaxiFind should feel like a **clear local information tool**, not a complicated transport platform.

The ideal user experience is:

```text
Open
 ↓
Search
 ↓
Understand
 ↓
Go
```

The application should provide enough information for a commuter to make sense of a supported taxi journey while being honest about what TaxiFind does and does not know.

The interface must never use visual polish to hide incomplete route data.

---

# 77. Document Status

**Document:** UI/UX Design Brief
**Version:** 1.0
**Status:** Draft
**Previous Document:** Application Flow Document
**Next Document:** Backend Schema

This document establishes the design direction for the TaxiFind SA MVP. The next document will define the database schema, relationships, constraints, verification model, route structure, fare model, and data required to support the user flows described in the preceding documents.


# 78. Concrete UI Acceptance Measurements

The TaxiFind SA UI should be evaluated using measurable acceptance criteria wherever practical.

These measurements are intended for MVP implementation and QA. They establish minimum usability and accessibility thresholds rather than prescribing a specific visual implementation.

---

## 78.1 Core Search Flow

### Search completion

A user should be able to complete:

```text
Home
 ↓
Select From
 ↓
Select To
 ↓
Search
 ↓
View Results
```

without creating an account.

**Acceptance measurement:**

* No more than **3 primary user actions** after the From and To fields are visible:

  1. Select From
  2. Select To
  3. Submit search
* The search button must be visible without requiring page scrolling on a typical **360px-wide mobile viewport**, where practical.
* A valid search must produce either:

  * Supported journey results, or
  * A clear no-supported-journey state.

---

## 78.2 Search Input Measurements

### Input dimensions

On mobile:

* Minimum input height: **48px**
* Recommended height: **52–56px**
* Minimum horizontal touch target: **44px**
* Minimum vertical touch target: **44px**

### Labels

Every search field must have a persistent accessible label:

```text
From
To
```

Placeholder text must not be the only label.

### Suggestions

When suggestions are available:

* Suggestions should appear without requiring a separate submit action.
* Each suggestion must have a minimum touch target of **44px × 44px**.
* Keyboard users must be able to navigate suggestions.
* `Enter` must select the currently highlighted suggestion.
* `Escape` must close the suggestion list.

---

## 78.3 Search Validation

Invalid searches must be identified before unnecessary API requests where validation can be performed locally.

Examples:

```text
From is empty
To is empty
From = To
```

**Acceptance measurements:**

* Validation message appears within **200ms** of the relevant user action under normal local UI conditions.
* Error messages must appear adjacent to the affected field.
* The error must be understandable without relying on colour.
* The user's other valid input must not be cleared.

Example:

```text
To

Please select a destination.
```

---

# 78.4 Search Loading State

After a valid search is submitted:

* A visible loading state must appear within **200ms**.
* The primary search action must prevent accidental duplicate submissions.
* The selected From and To values must remain visible.
* If the request takes longer than **2 seconds**, the interface should continue providing visible progress feedback.
* A request that fails must not leave the interface permanently displaying a loading state.

---

# 78.5 Search Results

Results should communicate the most important information without requiring the user to open every card.

Every supported journey result must expose:

* Origin
* Destination
* Direct/multi-taxi indication
* Estimated fare, if available
* Estimated duration, if available
* Taxi change count
* Verification status
* Last verified date where available
* Journey details action

### Acceptance measurement

On a **360px-wide mobile viewport**, the first journey result should expose the following without horizontal scrolling:

```text
Origin → Destination
Fare
Time
Taxi changes
Verification status
View Journey
```

---

# 78.6 Journey Result Card

Minimum touch target for:

```text
View Journey
```

must be:

**44px × 44px**

Recommended primary button height:

**48px or greater**

Cards must not rely entirely on clicking a small text link.

---

# 78.7 Journey Details

The Journey Details page must expose the complete supported journey as readable text.

A user must be able to identify:

1. Starting location
2. Boarding location
3. Taxi route
4. Get-off location
5. Transfer location, if applicable
6. Next taxi, if applicable
7. Destination
8. Estimated fare
9. Estimated duration
10. Verification status

### Acceptance measurement

A tester unfamiliar with the implementation should be able to answer all 10 questions using the page **without opening the map**.

---

# 78.8 Journey Timeline

Every journey step must have:

* A visible step indicator
* A descriptive heading
* A clear action/instruction
* Relevant location information

Example:

```text
1
Walk to Tladi Taxi Rank

2
Take a taxi toward Bara

3
Get off at Bara Taxi Rank
```

### Acceptance measurement

No essential journey instruction may be communicated **only through colour, an icon, or the map**.

---

# 78.9 Transfer Information

For a multi-taxi journey, the transfer must be visually distinguishable.

The interface must explicitly communicate:

```text
CHANGE TAXI
```

and identify:

* Where to get off
* Where to find the next taxi
* Direction/destination to look for
* Additional fare where available
* Additional estimated time where available

### Acceptance measurement

A tester must be able to identify the transfer point within **5 seconds** of opening the journey details page under normal testing conditions.

---

# 78.10 Fare Display

Fare values must use South African Rand.

Example:

```text
Estimated fare

R20
```

### Acceptance measurements

* Currency must be visible.
* The word **Estimated** must be visible wherever the fare is an estimate.
* A missing fare must display an explicit unavailable state.
* No blank fare field may be interpreted as R0.
* The UI must never display a predicted fare as though it were stored/verified data.

For multi-leg journeys:

```text
Estimated total fare
R38

Taxi 1    R20
Taxi 2    R18
```

The displayed total must equal the sum of the displayed fare legs.

---

# 78.11 Journey Duration

Duration must be displayed as an estimate.

Example:

```text
Estimated journey time
35–45 minutes
```

### Acceptance measurements

* Duration must never be presented as a guaranteed arrival time.
* Missing duration must explicitly state that it is unavailable.
* The UI must not display a fabricated duration.

---

# 78.12 Verification Status

Every public route displayed by the application must expose its verification status.

Supported labels include:

```text
Verified
Community Reported
Unverified
Outdated
Unavailable
```

### Acceptance measurements

* Status must be represented by text.
* Colour must not be the only status indicator.
* Where `last_verified_at` exists, it must be displayed in a human-readable format.
* A route marked `outdated` must not visually appear equivalent to a verified route.

---

# 78.13 No-Supported-Journey State

When no supported journey exists, the interface must distinguish:

```text
No supported TaxiFind data
```

from:

```text
No taxi journey exists
```

### Acceptance measurements

The no-results screen must:

* State that supported information is unavailable.
* Avoid claiming that the real-world journey does not exist.
* Preserve the user's search.
* Provide a way to change the search.
* Avoid generating an alternative route that is not supported by the database.

---

# 78.14 Map Acceptance Measurements

The map must be supplementary to the written journey.

### Minimum requirements

* Map must have a defined container height.
* On mobile, recommended minimum map height: **280px**.
* On desktop, recommended minimum map height: **400px**.
* Map controls must have touch targets of at least **44px × 44px**.
* Markers must be selectable.
* Marker information must be understandable without colour alone.

### Accuracy requirement

The frontend must not draw a precise route line unless reliable route geometry exists.

If only coordinates are known:

```text
Origin ●

Taxi Rank ●

Destination ●
```

is acceptable.

A fictional road path is not.

---

# 78.15 Map Failure

If the map cannot load:

```text
Map temporarily unavailable.

Your journey information is still available.
```

### Acceptance measurement

The written journey must remain usable when the map component is completely unavailable.

The map failure must not prevent access to:

* Journey steps
* Fare
* Duration
* Transfer information
* Verification status

---

# 78.16 Mobile Responsive Measurements

The MVP must be tested at minimum at:

| Viewport   | Requirement |
| ---------- | ----------- |
| 320 × 568  | Supported   |
| 360 × 640  | Supported   |
| 390 × 844  | Supported   |
| 768 × 1024 | Supported   |
| 1024 × 768 | Supported   |
| 1280 × 800 | Supported   |

### Acceptance measurements

At supported viewport sizes:

* No unintended horizontal scrolling.
* No clipped primary buttons.
* No overlapping content.
* Search fields remain usable.
* Journey cards remain readable.
* Navigation remains accessible.
* Text remains readable without browser zoom for normal use.

---

# 78.17 Touch Target Measurements

All primary interactive controls should meet:

**Minimum: 44px × 44px**

This applies to:

* Buttons
* Search suggestions
* Menu controls
* Back controls
* Close controls
* Map controls
* Checkbox/radio controls
* Important icon buttons

Where practical, primary buttons should be at least:

**48px high**

---

# 78.18 Keyboard Accessibility

A complete public journey must be usable with a keyboard.

### Acceptance measurements

A tester must be able to:

```text
Tab
 ↓
From
 ↓
Select location
 ↓
To
 ↓
Select location
 ↓
Search
 ↓
Open result
 ↓
Navigate journey details
```

without requiring a mouse.

Requirements:

* Visible keyboard focus.
* Logical focus order.
* No keyboard traps.
* Escape closes dismissible overlays.
* Enter activates appropriate controls.
* Focus should move appropriately after major navigation or modal interactions.

---

# 78.19 Focus Visibility

Keyboard focus must be visually obvious.

### Acceptance measurement

The focused element must have a visible indicator with sufficient contrast against its surroundings.

The implementation must not use:

```css
outline: none;
```

without providing an equivalent accessible focus indicator.

---

# 78.20 Colour Contrast

The UI should meet **WCAG 2.2 AA** contrast expectations for normal interface text and important controls.

As a practical acceptance target:

* Normal text: approximately **4.5:1 minimum**
* Large text: approximately **3:1 minimum**
* Important graphical indicators and UI boundaries should maintain appropriate contrast.

Contrast must be checked using the actual implemented colours rather than assumed from the design palette.

---

# 78.21 Colour Independence

Information must remain understandable when colour perception is limited.

For example:

Do not use:

```text
Green = verified
Red = outdated
```

without labels.

Use:

```text
✓ Verified

⚠ Outdated
```

The symbols should supplement the text rather than replace it.

---

# 78.22 Text Scaling

The interface should remain usable when text is increased.

### Acceptance measurement

At **200% browser text/page zoom**, the primary public journey should remain usable without:

* Text overlapping
* Important controls disappearing
* Unusable horizontal scrolling
* Truncated critical journey information

Responsive behaviour should be tested separately from desktop layout.

---

# 78.23 Screen Reader Acceptance

A screen reader should expose meaningful information for:

* Page title
* From field
* To field
* Search button
* Location suggestions
* Journey cards
* Fare
* Duration
* Verification status
* Journey steps
* Transfer information
* Map alternative text/content

### Acceptance measurement

A tester using a screen reader must be able to determine:

```text
Origin
Destination
Fare
Duration
Taxi changes
Verification
Journey steps
```

without interacting with the visual map.

---

# 78.24 Form Accessibility

Every form field must have:

* Programmatic label
* Appropriate input type
* Accessible error state
* Error message association where applicable
* Keyboard access

Placeholder text must not be used as the only accessible label.

---

# 78.25 Error Recovery

Every recoverable error should provide a next action.

Examples:

```text
Network error
[ Try Again ]
```

```text
Invalid search
[ Change Search ]
```

```text
Map unavailable
[ Continue Without Map ]
```

### Acceptance measurement

A user must not become trapped in an error state requiring a browser refresh to continue.

---

# 78.26 Loading and Skeleton States

Loading indicators should appear when an operation takes noticeable time.

### Acceptance measurements

* Feedback begins within **200ms** of a user action where feasible.
* No indefinite spinner.
* Requests that fail must transition to an error state.
* Loading controls must not allow accidental repeated submissions.

---

# 78.27 Navigation

Users must be able to move:

```text
Home
 ↓
Results
 ↓
Journey Details
 ↓
Back to Results
```

without losing their selected journey.

### Acceptance measurement

Returning from Journey Details to Results must preserve:

* Origin
* Destination
* Result list
* Selected search context

within the active browser session.

---

# 78.28 Browser Back Button

The browser back button must behave predictably.

Example:

```text
Home
 ↓
Results
 ↓
Journey Details
```

Browser Back should return to:

```text
Results
```

rather than unexpectedly returning to Home or closing the application state.

---

# 78.29 Performance UX Targets

These are UI performance targets rather than backend SLA guarantees.

### Initial page

Target:

**Largest Contentful Paint ≤ 2.5 seconds**

under a representative production-like mobile test environment.

### Interaction

Target:

**Interaction to Next Paint ≤ 200ms** for normal UI interactions.

### Search

The UI should display search progress immediately and should not block the interface unnecessarily while waiting for the API.

Backend/API response targets will be defined separately in the Technical Requirements and implementation testing.

---

# 78.30 Admin UI Measurements

Admin screens should prioritise efficient data management.

### Acceptance measurements

An administrator should be able to:

* Create a location.
* Create a taxi rank.
* Create a route.
* Add route steps.
* Add a fare.
* Change verification status.

without modifying source code.

### Forms

Required fields must be clearly identified.

Validation errors must appear next to the relevant field.

### Tables

On desktop:

* Table rows must remain readable.
* Important status information must be visible without opening every record.

On mobile:

* Tables must transform into usable cards or another responsive representation.
* Horizontal scrolling should not be required for basic record management where a responsive alternative is practical.

---

# 78.31 Destructive Action Measurements

Actions such as deleting a route must require deliberate confirmation.

Example:

```text
Delete Route?

This will remove the route from the
TaxiFind public dataset.

[ Cancel ] [ Delete ]
```

### Acceptance measurement

A destructive action must not execute from a single accidental click where irreversible deletion is possible.

---

# 78.32 Data Freshness Display

Where verification information exists, the UI should display:

```text
Last verified:
15 September 2026
```

Dates should use a human-readable format.

The interface should avoid displaying raw database timestamps such as:

```text
2026-09-15T14:32:51.000Z
```

to ordinary users.

---

# 78.33 Content Width

On large desktop screens, reading content should not stretch unnecessarily across the entire viewport.

Recommended maximum content width:

**1200–1280px**

Journey text-heavy sections should use a narrower readable line length where appropriate.

---

# 78.34 Mobile Search Target

The primary search experience should be usable with one hand on a typical smartphone.

### Acceptance measurement

At a **360px viewport width**:

* From input fits within the viewport.
* To input fits within the viewport.
* Search button fits within the viewport.
* No horizontal scrolling is required.
* Input and button touch targets are at least 44px high.

---

# 78.35 Journey Comprehension Test

A basic usability acceptance test should be performed with representative users.

After viewing a supported journey, ask:

> Where do you catch the taxi?

> Where do you get off?

> Do you need to change taxis?

> How much is the estimated fare?

> How long is the estimated journey?

> How current is the information?

### MVP target

At least **80% of test participants** should be able to answer all six questions correctly without assistance.

This is a usability target, not a claim about real-world commuter behaviour.

---

# 78.36 Search Usability Test

A representative usability test should include a supported journey such as:

```text
Tladi → Bara
```

using actual seeded/test data.

### MVP target

At least **80% of test participants** should be able to:

1. Identify the From field.
2. Select the correct origin.
3. Identify the To field.
4. Select the correct destination.
5. Submit the search.
6. Open the journey details.

without moderator assistance.

---

# 78.37 Unsupported Journey Usability Test

Test an origin/destination combination that is intentionally absent from the MVP dataset.

### Acceptance target

At least **90% of test participants** should understand from the result that:

> TaxiFind does not currently have supported information for this journey.

The test should specifically verify that users do not interpret the message as proof that no real-world taxi journey exists.

---

# 78.38 Accessibility Acceptance Checklist

Before MVP release:

| Requirement                                     |                    Target |
| ----------------------------------------------- | ------------------------: |
| Keyboard navigation                             |      100% of core journey |
| Visible focus                                   | 100% interactive controls |
| Form labels                                     |                      100% |
| Critical journey text available without map     |                      100% |
| Colour-independent status                       |                      100% |
| Primary touch targets ≥44px                     |                      100% |
| No keyboard traps                               |                         0 |
| Horizontal overflow on supported mobile layouts |              0 unintended |
| Critical journey information clipped            |                         0 |
| Critical actions without accessible name        |                         0 |

---

# 78.39 Responsive Acceptance Checklist

The following must pass on supported viewport sizes:

| Test                                |       Target |
| ----------------------------------- | -----------: |
| Horizontal overflow                 | 0 unintended |
| Clipped primary buttons             |            0 |
| Overlapping components              |            0 |
| Unusable search fields              |            0 |
| Hidden critical journey information |            0 |
| Broken navigation                   |            0 |
| Unreadable verification status      |            0 |

---

# 78.40 UI Release Gate

The MVP UI should not be considered complete until:

### Core journey

* [ ] Home search works.
* [ ] From selection works.
* [ ] To selection works.
* [ ] Search validation works.
* [ ] Results are understandable.
* [ ] Journey details are understandable.
* [ ] Transfers are clearly identified.
* [ ] Fare is correctly labelled.
* [ ] Duration is correctly labelled.
* [ ] Verification status is visible.
* [ ] Map is supplementary.
* [ ] Map failure does not break the journey.

### Responsive

* [ ] 320px layout tested.
* [ ] 360px layout tested.
* [ ] 390px layout tested.
* [ ] Tablet layout tested.
* [ ] Desktop layout tested.
* [ ] No unintended horizontal overflow.

### Accessibility

* [ ] Keyboard journey tested.
* [ ] Screen reader journey tested.
* [ ] Focus states tested.
* [ ] Touch targets tested.
* [ ] Contrast tested.
* [ ] Colour-independent status tested.
* [ ] 200% zoom tested.

### Data transparency

* [ ] Unsupported routes are clearly identified.
* [ ] No unsupported routes are invented.
* [ ] Estimated fares are labelled.
* [ ] Estimated durations are labelled.
* [ ] Verification status is displayed.
* [ ] Last verified date is displayed where available.

### Admin

* [ ] Admin can manage locations.
* [ ] Admin can manage taxi ranks.
* [ ] Admin can manage routes.
* [ ] Admin can manage route steps.
* [ ] Admin can manage fares.
* [ ] Admin can update verification status.

---

# 79. Final UI Acceptance Principle

The UI is successful when a commuter can use a smartphone to answer:

```text
Where do I start?
        ↓
Where do I catch the taxi?
        ↓
Which taxi do I take?
        ↓
Where do I get off?
        ↓
Do I change taxis?
        ↓
How much should I expect to pay?
        ↓
How long might it take?
        ↓
How current is the information?
```

without requiring:

* An account
* A map interaction
* AI assistance
* Knowledge of the database
* Technical understanding of the system

The interface should make supported information easy to understand while making uncertainty and coverage limitations equally clear.

---

# 80. Document Status

**Document:** UI/UX Design Brief
**Version:** 1.1
**Status:** Draft
**Previous Document:** Application Flow Document
**Next Document:** Backend Schema

This version adds measurable UI, accessibility, responsive, performance, and usability acceptance criteria so that the TaxiFind SA interface can be objectively tested during implementation and QA.
