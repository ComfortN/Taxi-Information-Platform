# TaxiFind SA

## Project Requirements Document (PRD)

**Document Version:** 1.0
**Status:** Draft
**Project Type:** Web Application / Progressive Web App
**Initial Geographic Focus:** South Africa — Gauteng pilot
**Working Project Name:** TaxiFind SA

---

# 1. Project Overview

TaxiFind SA is a South African minibus taxi journey information platform designed to help commuters discover and understand taxi-based journeys.

The platform will allow users to search for journeys between locations and receive practical information such as:

* Where to catch a taxi
* Which taxi route to use
* Where to get off
* Whether a transfer is required
* Where to change taxis
* Estimated fare
* Estimated journey time
* Taxi rank locations
* Route information
* Operating information where available
* Map-based journey information
* Community-reported updates

The platform will initially focus on a limited, verified set of routes in Gauteng and will be designed so that it can expand to other provinces and regions across South Africa.

The long-term goal is to create a comprehensive digital information platform for South African minibus taxi transportation.

---

# 2. Problem Statement

Minibus taxis are one of the most important forms of public transportation in South Africa. However, information about taxi routes, taxi ranks, fares, transfers, and operating patterns is often difficult for commuters to discover digitally.

A person who is unfamiliar with an area may know where they want to go but not:

* Which taxi rank to use
* Which taxi to take
* Where the taxi goes
* Whether they need to change taxis
* Where to change
* How much the journey costs
* How long the journey may take
* Whether the route information they found is still current

Existing digital navigation services can provide geographic directions, but they may not provide the detailed operational knowledge that regular minibus taxi commuters use.

TaxiFind SA aims to make this information easier to discover, understand, and maintain.

---

# 3. Product Vision

The vision of TaxiFind SA is to become a trusted digital information platform for minibus taxi journeys in South Africa.

The platform should allow someone who is unfamiliar with a journey to ask:

> "How do I get from Tladi to Bara?"

and receive understandable information about the available taxi journey.

The same platform should eventually support journeys such as:

> "How do I get from the Vaal to Midrand?"

> "Where can I find a taxi to Bara?"

> "How much is a taxi from Soweto to Johannesburg?"

> "Where is the nearest taxi rank?"

The platform should support both structured searches and natural-language journey queries.

---

# 4. Project Objectives

## 4.1 Primary Objectives

The project aims to:

1. Provide accessible information about South African minibus taxi routes.
2. Allow users to search for journeys between locations.
3. Provide taxi rank and route information.
4. Provide estimated fare information.
5. Explain journeys that require multiple taxis.
6. Provide map-based location and route information.
7. Allow information to be updated and verified.
8. Support South Africa's official languages.
9. Provide an accessible and mobile-friendly user experience.
10. Establish a scalable foundation for nationwide expansion.

---

# 5. Target Users

## 5.1 Regular Taxi Commuters

People who regularly use minibus taxis and need:

* Current fare information
* Route information
* Rank information
* Alternative routes
* Updates about route changes

## 5.2 New or Infrequent Commuters

People who know their destination but are unfamiliar with the taxi system in that area.

Example:

> A person living in Tladi needs to travel to Bara for the first time.

## 5.3 Students

Students travelling between:

* Home
* School
* University
* Colleges
* Residences
* Transport hubs

## 5.4 Workers

People commuting between residential areas and:

* Johannesburg CBD
* Sandton
* Midrand
* Pretoria
* Industrial areas
* Business districts

## 5.5 Visitors and Tourists

People unfamiliar with South African minibus taxi routes who need practical transport information.

## 5.6 Community Contributors

Users who can report:

* Fare changes
* Route changes
* Rank changes
* Incorrect information
* Temporary disruptions

## 5.7 Administrators

Authorized users responsible for:

* Managing route information
* Managing taxi ranks
* Reviewing reports
* Verifying information
* Managing fares
* Maintaining platform data

---

# 6. Geographic Scope

## 6.1 Initial Scope

The first implementation will focus on selected routes in Gauteng.

The initial pilot may include areas such as:

* Soweto
* Johannesburg
* Vaal
* Midrand

The exact pilot routes will be determined during the data collection and validation stage.

Example pilot journeys include:

* Tladi → Bara
* Soweto → Johannesburg
* Vaal → Midrand

These examples are intended to demonstrate the product concept and do not represent confirmed route or fare information.

## 6.2 Future Scope

The platform should eventually support:

* Gauteng
* Western Cape
* KwaZulu-Natal
* Eastern Cape
* Free State
* Limpopo
* Mpumalanga
* North West
* Northern Cape

The application architecture should therefore not contain assumptions that limit it to Gauteng.

---

# 7. Core Product Concept

The core interaction is:

```text
Origin
   ↓
Destination
   ↓
Search
   ↓
Available taxi journey(s)
   ↓
Journey details
   ↓
Map / directions
```

For example:

```text
FROM
Tladi

TO
Bara

        SEARCH
          ↓

Taxi Journey

Tladi Taxi Rank
       ↓
Tladi → Bara taxi
       ↓
Bara Taxi Rank

Estimated Fare
RXX

Estimated Time
XX–XX minutes

Taxi Changes
0

[ View Map ]
```

Actual route and fare information must come from the application's verified data rather than being invented by the system.

---

# 8. MVP Scope

The Minimum Viable Product will focus on proving the core journey-search experience.

## 8.1 MVP Features

### Journey Search

Users must be able to enter:

* Origin
* Destination

and search for available taxi journeys.

### Route Results

The system must display relevant route information including, where available:

* Origin
* Destination
* Taxi rank
* Route
* Transfers
* Estimated fare
* Estimated journey duration
* Route status
* Last verification date

### Taxi Rank Information

Users should be able to view:

* Taxi rank name
* Location
* Map position
* Area
* Available routes

### Map

Users should be able to view relevant locations on a map.

### Basic Language Support

The MVP should support English initially while the application is architected for additional South African languages.

### Responsive Design

The application must work on:

* Mobile phones
* Tablets
* Desktop computers

Mobile usage should be treated as the primary experience.

---

# 9. Post-MVP Features

The following features should be designed for but not necessarily implemented in the first release.

## 9.1 User Accounts

Users may eventually be able to:

* Register
* Log in
* Save routes
* Save favourite taxi ranks
* Manage preferences

## 9.2 Community Reporting

Users may report:

* New fares
* Route changes
* Rank changes
* Incorrect information
* Temporary closures
* Other relevant transport updates

## 9.3 Information Verification

Administrators should be able to review submitted information before it becomes verified public information.

## 9.4 Multiple Languages

The application should eventually support all 11 official spoken South African languages:

* Afrikaans
* English
* isiNdebele
* isiXhosa
* isiZulu
* Sepedi
* Sesotho
* Setswana
* siSwati
* Tshivenda
* Xitsonga

South African Sign Language should also be considered as an accessibility requirement, although its implementation will require approaches beyond normal text translation.

## 9.5 Saved Journeys

Users can save frequently used journeys such as:

```text
Home → Work
Home → School
Home → University
Home → Church
```

## 9.6 Nearby Taxi Ranks

The application may use the user's location to identify nearby taxi ranks.

Location access must be optional and require appropriate user permission.

## 9.7 AI Journey Assistant

Users may eventually be able to type natural-language requests such as:

> "I'm in Tladi and need to get to Bara."

The AI should interpret the request and retrieve information from the application's route database.

The AI must not independently invent route or fare information.

## 9.8 Voice Search

Future versions may support spoken journey requests.

## 9.9 Transport Expansion

The platform may eventually include other transport modes such as:

* Trains
* Buses
* E-hailing
* Walking connections

This is outside the initial MVP.

---

# 10. Functional Requirements

## FR-001 — Journey Search

The system shall allow a user to search for a journey using an origin and destination.

## FR-002 — Location Search

The system shall provide location suggestions while users enter an origin or destination.

## FR-003 — Route Results

The system shall return relevant taxi journey information for a requested origin and destination.

## FR-004 — Multiple Journey Options

Where multiple valid journeys exist, the system shall be able to present multiple options without ranking them as universally "best."

## FR-005 — Taxi Rank Information

The system shall provide information about taxi ranks associated with supported routes.

## FR-006 — Fare Information

The system shall display an estimated fare where verified or reported fare information exists.

## FR-007 — Fare Currency

South African Rand (ZAR/R) shall be used for fare information.

## FR-008 — Transfer Information

The system shall indicate when a journey requires one or more taxi changes.

## FR-009 — Journey Steps

The system shall provide a step-by-step description of supported journeys.

## FR-010 — Map Information

The system shall display relevant journey locations and route information on a map.

## FR-011 — Information Status

The system shall distinguish between information that is:

* Verified
* Community reported
* Unverified
* Outdated
* Temporarily unavailable

## FR-012 — Last Verification

Route and fare information should have a recorded last-verified date.

## FR-013 — Community Reports

Future versions shall allow users to report potentially outdated or incorrect information.

## FR-014 — Administrative Management

Authorized administrators shall be able to manage:

* Locations
* Taxi ranks
* Routes
* Fares
* Reports
* Verification status

## FR-015 — Language Selection

Users shall be able to select their preferred application language.

## FR-016 — Responsive Interface

The application shall adapt to mobile, tablet, and desktop screen sizes.

## FR-017 — Error Handling

The system shall provide understandable messages when:

* No route is found
* Location cannot be identified
* Data is unavailable
* A service is temporarily unavailable

## FR-018 — Search History

A future version may allow authenticated users to view previous searches.

## FR-019 — Saved Routes

A future version shall allow authenticated users to save commonly used journeys.

---

# 11. Data Requirements

TaxiFind SA depends heavily on accurate structured transport information.

The system should be capable of storing information about:

### Locations

* Name
* Type
* Address or area
* Municipality
* City
* Province
* Coordinates

### Taxi Ranks

* Name
* Location
* Coordinates
* Operating information
* Associated routes
* Associated taxi association where known

### Routes

* Origin
* Destination
* Intermediate stops
* Route description
* Operating information
* Status
* Verification information

### Fares

* Route
* Amount
* Currency
* Effective date
* Source
* Verification status

### Taxi Associations

Where information is publicly available and appropriate:

* Association name
* Operating area
* Contact information
* Associated ranks/routes

### Reports

* Report type
* User
* Related route/rank
* Report description
* Submitted date
* Status
* Verification result

---

# 12. Data Reliability Requirements

Taxi information can change over time.

The platform must therefore avoid presenting all information as permanently accurate.

Information should have a status such as:

```text
Verified
Community Reported
Unverified
Outdated
Unavailable
```

The system should maintain timestamps for important information.

For example:

```text
Fare: R20
Last verified: 2026-09-15
Status: Verified
```

The exact verification methodology will be defined in later technical and operational documentation.

---

# 13. Multilingual Requirements

The application is intended for users across South Africa.

The architecture shall support multilingual content from the beginning rather than adding translation as a late-stage feature.

The initial language may be English for development purposes.

The application should be designed to support:

* Afrikaans
* English
* isiNdebele
* isiXhosa
* isiZulu
* Sepedi
* Sesotho
* Setswana
* siSwati
* Tshivenda
* Xitsonga

South African Sign Language should be considered within the application's accessibility strategy.

Translations should cover application interface content such as:

* Navigation
* Buttons
* Search prompts
* Instructions
* Error messages
* Help content
* Accessibility labels

Transport data such as official names of taxi ranks and places should not automatically be machine-translated without consideration of local naming conventions.

---

# 14. Accessibility Requirements

The application should aim to conform to modern web accessibility practices.

The platform should support:

* Keyboard navigation
* Screen readers
* Adequate text contrast
* Readable typography
* Clear focus states
* Accessible form controls
* Alternative text for meaningful images
* Accessible error messages
* Responsive text
* Appropriate semantic HTML

Future versions should investigate:

* South African Sign Language content
* Voice interaction
* Text-to-speech
* Low-literacy-friendly journey instructions

---

# 15. Non-Functional Requirements

## NFR-001 — Performance

Common pages should load quickly on typical South African mobile internet connections.

## NFR-002 — Mobile First

The application shall be designed primarily for mobile users.

## NFR-003 — Availability

The public application should be designed for reliable availability during normal operating conditions.

## NFR-004 — Scalability

The architecture should support expansion from a small Gauteng dataset to nationwide route information.

## NFR-005 — Security

User accounts, administrative functionality, and sensitive configuration information must be appropriately protected.

## NFR-006 — Maintainability

The codebase should use a modular architecture with clear separation between:

* Frontend
* Backend
* Database
* External services

## NFR-007 — Data Integrity

Route, fare, and location data must use appropriate validation and database constraints.

## NFR-008 — Observability

The production system should provide appropriate application logging and error monitoring.

## NFR-009 — Privacy

The application should collect only information necessary for its functionality.

Location information should only be accessed with appropriate user permission.

## NFR-010 — Compatibility

The web application should support current major versions of:

* Chrome
* Edge
* Firefox
* Safari

---

# 16. User Roles

The platform should eventually support multiple user roles.

## Guest

Can:

* Search routes
* View taxi ranks
* View fares
* View maps
* Change language

## Registered User

Can additionally:

* Save routes
* Submit reports
* Manage preferences
* View search history

## Moderator

Can:

* Review community reports
* Verify information
* Flag problematic information

## Administrator

Can:

* Manage routes
* Manage locations
* Manage fares
* Manage taxi ranks
* Manage users
* Manage reports
* Manage verification

The exact permission model will be defined in the Technical Requirements Document.

---

# 17. Search Requirements

Search is a central feature of the platform.

The system should support:

### Exact searches

```text
Tladi → Bara
```

### Partial searches

```text
Tla → Bar
```

### Location suggestions

```text
Tl...
   
Tladi
```

### Future natural-language searches

```text
How do I get from Tladi to Bara?
```

The search system should account for:

* Common place names
* Taxi rank names
* Suburbs
* Townships
* Cities
* Provinces
* Common spelling variations

Search should not assume that the user knows the official name of a taxi rank.

---

# 18. Route Information Requirements

A route may consist of a single taxi journey or multiple taxi journeys.

### Direct Journey

```text
Origin
   ↓
Taxi Rank
   ↓
Taxi
   ↓
Destination Rank
   ↓
Destination
```

### Multi-Taxi Journey

```text
Origin
   ↓
Rank A
   ↓
Taxi 1
   ↓
Rank B
   ↓
Taxi 2
   ↓
Rank C
   ↓
Destination
```

The application should make transfers clearly understandable.

---

# 19. Community Data Model

The platform should eventually use a combination of:

1. Structured platform data
2. Verified administrative information
3. Community reports
4. Appropriate external/public information sources

Community reports should not automatically replace verified information.

Instead, they should enter a review or verification process where appropriate.

---

# 20. Out of Scope for MVP

The following should not be required for the first release:

* Guaranteed journey times
* Nationwide coverage from day one
* Full AI assistant
* All language translations completed before MVP launch

These may be considered in future product phases.

---

# 21. Product Principles

The following principles should guide development.

### Accuracy Before Automation

The system should prefer reliable information over generating an answer simply because a user asked a question.

### Simple for Commuters

A user should not need technical knowledge to understand a journey.

### Mobile First

The primary experience should work well on an ordinary smartphone.

### Community Supported

Users should eventually be able to help keep information current.

### Transparent Information

The platform should indicate when information was last verified and, where appropriate, how its status was established.

### Inclusive

The product should support South Africa's linguistic and accessibility needs.

### Scalable

The initial Gauteng implementation should be capable of expanding across South Africa.

### Data Over Assumptions

The application should distinguish between known information, reported information, and unavailable information.

---

# 22. MVP Success Criteria

The MVP will be considered functionally successful when a user can:

1. Open the application.
2. Select or enter an origin.
3. Select or enter a destination.
4. Search for a journey.
5. Receive at least one supported taxi journey when relevant data exists.
6. Understand where to start the journey.
7. Understand which taxi route to take.
8. Understand where to get off.
9. See the estimated fare when available.
10. See the estimated journey duration when available.
11. View relevant locations on a map.
12. Understand whether a transfer is required.
13. Receive an understandable result when no supported route exists.

Administrators must also be able to maintain the underlying route and fare information.

---

# 23. Future Product Direction

Once the core platform is established, TaxiFind SA may evolve into a broader South African commuter information platform.

Potential future capabilities include:

* Natural-language journey planning
* Voice-based journey search
* Multilingual AI assistance
* Community transport alerts
* Live disruption reporting
* Transport-mode comparison
* Public transport integration
* Accessibility-focused journey planning
* Offline journey information
* Progressive Web App functionality
* Data analytics for transport patterns
* Partnerships with transport organizations

These possibilities should not complicate the MVP architecture unnecessarily, but the foundational data model should allow future expansion.

---

# 24. Key Risks

## Data Accuracy

Taxi routes and fares can change.

**Mitigation:** Introduce verification status, timestamps, community reporting, and administrative review.

## Limited Initial Data

The application may initially have only a small number of verified routes.

**Mitigation:** Clearly communicate coverage and gradually expand the dataset.

## User Trust

Users may rely on transport information for important journeys.

**Mitigation:** Display information status, verification dates, and appropriate uncertainty.

## Language Quality

Poor translations could make important transport information confusing.

**Mitigation:** Use appropriate human review for important translations and avoid blindly translating local place names.

## Geographic Expansion

South Africa has a large and diverse taxi network.

**Mitigation:** Build a scalable geographic data model and expand region by region.

## Real-Time Information

The platform may not initially know about temporary disruptions.

**Mitigation:** Introduce community reporting and information timestamps.

---

# 25. Assumptions

The project currently assumes that:

1. Users primarily access the service from mobile devices.
2. Users generally know either their origin, destination, or both.
3. Taxi information can initially be collected and verified for a limited pilot region.
4. Route and fare information will not always be available.
5. Some journey information will require community contribution.
6. Internet connectivity may be inconsistent for some users.
7. The system will initially provide information rather than directly operate or book taxi services.

---

# 26. Dependencies

The project may depend on:

* Mapping services
* Geographical data
* OpenStreetMap or another mapping provider
* PostgreSQL
* Hosting infrastructure
* Authentication services
* Translation resources
* Community-submitted information
* Appropriate public transport information sources

The exact third-party services will be specified in the Technical Requirements Document.

---

# 27. Initial Technology Direction

The initial implementation is expected to use:

### Frontend

* React
* TypeScript
* Vite

### Backend

* Python
* FastAPI

### Database

* PostgreSQL

### Mapping

* OpenStreetMap
* Leaflet

### Authentication

To be determined during technical architecture design, with Supabase being one candidate.

### Deployment

To be determined during technical architecture design.

These are initial technical directions rather than final requirements and will be formally defined in the Technical Requirements Document.

---

# 28. Project Deliverables

The initial project documentation and implementation should produce:

### Documentation

* Project Requirements Document
* Technical Requirements Document
* App Flow
* UI/UX Design Brief
* Backend Schema
* Implementation Plan

### Software

* Responsive web application
* Backend API
* PostgreSQL database
* Administrative interface
* Route search
* Taxi rank information
* Fare information
* Map integration
* Initial multilingual architecture

### Data

* Initial verified pilot locations
* Initial taxi ranks
* Initial taxi routes
* Initial fare information

---

# 29. Definition of Done — MVP

The MVP is considered ready for controlled testing when:

* The frontend is functional on mobile and desktop.
* The backend API is operational.
* PostgreSQL is connected.
* Pilot taxi data is loaded.
* Users can search supported journeys.
* Search results display route information.
* Fare information is displayed where available.
* Taxi rank locations can be displayed.
* Maps function correctly.
* No-route scenarios are handled.
* API errors are handled gracefully.
* Core automated tests pass.
* Administrative data management is functional.
* Documentation is updated.
* The application clearly communicates the coverage and status of its information.

---

# 30. Document Status

**Current Version:** 1.0
**Status:** Draft
**Next Document:** Technical Requirements Document

This document establishes the product requirements. Technical implementation details, database structures, API specifications, infrastructure choices, and detailed security architecture will be defined in the Technical Requirements Document.
