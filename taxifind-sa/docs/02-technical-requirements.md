# TaxiFind SA

## Technical Requirements Document (TRD)

**Document Version:** 1.0
**Status:** Draft
**Project Type:** Web Application / Progressive Web App
**Initial Geographic Focus:** Gauteng, South Africa — controlled pilot
**Related Document:** Project Requirements Document (PRD)
**Next Document:** App Flow

---

# 1. Document Purpose

This Technical Requirements Document defines the technical architecture, technologies, software requirements, data handling requirements, API requirements, security requirements, testing requirements, and deployment requirements for TaxiFind SA.

The document translates the product requirements defined in the Project Requirements Document into an implementable technical specification.

The Technical Requirements Document is specifically concerned with the **MVP implementation**.

Features explicitly outside the MVP must not introduce unnecessary infrastructure or complexity into the initial implementation.

---

# 2. MVP Technical Definition

The TaxiFind SA MVP is a mobile-first web application that allows users to search for supported minibus taxi journeys between locations.

The system will provide:

* Origin selection
* Destination selection
* Location suggestions
* Supported taxi journey results
* Taxi rank information
* Route steps
* Taxi transfers
* Estimated fares
* Estimated journey duration
* Map-based information
* Route verification status
* Last-verified dates
* Basic administrator data management
* Responsive web access
* English interface
* Internationalisation architecture for additional South African languages

The MVP will **not** require:

* Taxi booking
* Online payments
* Live taxi tracking
* Driver accounts
* Driver dispatch
* Real-time taxi availability
* AI journey planning
* Voice search
* Public community reporting
* User accounts
* Push notifications
* Nationwide route coverage
* Integration with other transport modes
* Offline-first functionality

---

# 3. Technical Architecture

## 3.1 High-Level Architecture

The initial system shall use a three-tier architecture:

```text
┌───────────────────────────────┐
│           User                │
│       Mobile / Desktop        │
└───────────────┬───────────────┘
                │
                │ HTTPS / REST API
                ▼
┌───────────────────────────────┐
│       React Web Frontend       │
│    TypeScript + Vite           │
└───────────────┬───────────────┘
                │
                │ REST / JSON
                ▼
┌───────────────────────────────┐
│        FastAPI Backend         │
│           Python               │
└───────────────┬───────────────┘
                │
                │ SQL / ORM
                ▼
┌───────────────────────────────┐
│         PostgreSQL             │
│       Transport Dataset        │
└───────────────────────────────┘
```

Mapping functionality will be integrated into the frontend:

```text
React
  │
  └── Leaflet
        │
        └── OpenStreetMap
```

Administrative users will access the same backend through an administrator interface.

---

# 4. Technology Stack

## 4.1 Frontend

The frontend shall use:

* React
* TypeScript
* Vite
* React Router
* Leaflet
* React-Leaflet
* i18next
* react-i18next

Recommended supporting libraries may include:

* Axios or Fetch API
* Zod for validation where useful
* A lightweight state-management solution only where required

The frontend should avoid unnecessary dependencies.

---

# 5. Backend Technology

The backend shall use:

* Python
* FastAPI
* Pydantic
* SQLAlchemy
* Alembic
* PostgreSQL
* Uvicorn

The backend shall expose a versioned REST API.

Example:

```text
/api/v1/
```

---

# 6. Database Technology

PostgreSQL shall be the primary application database.

The database must support:

* Geographic coordinates
* Locations
* Taxi ranks
* Routes
* Route steps
* Fares
* Verification status
* Administrative records

PostgreSQL shall be selected because the platform requires structured relational data and has a long-term requirement to support geographic expansion.

---

# 7. Geographic Data

The system shall store geographic coordinates using latitude and longitude.

Example:

```text
latitude: -26.2485
longitude: 27.8547
```

Coordinates shall use the WGS 84 geographic coordinate system.

Where geographic querying becomes necessary, the project may use PostgreSQL/PostGIS.

PostGIS should be considered particularly for:

* Nearby taxi ranks
* Distance calculations
* Bounding-box searches
* Geographic route queries

PostGIS is not required for the first simple implementation if standard coordinate queries are sufficient.

---

# 8. Mapping Requirements

## 8.1 Mapping Provider

The MVP shall initially use:

* OpenStreetMap map data
* Leaflet map rendering

The implementation should avoid making the core product dependent on Google Maps or Google Mobile Services.

## 8.2 Map Requirements

The map shall be able to display:

* Origin
* Destination
* Taxi ranks
* Transfer locations
* Route-related locations

## 8.3 Map Interaction

Users should be able to:

* Zoom
* Pan
* Select relevant locations
* View location markers
* Return to the journey information

## 8.4 Map Limitations

The MVP will not provide:

* Turn-by-turn navigation
* Live traffic
* Live taxi locations
* Driver GPS tracking
* Real-time taxi availability

---

# 9. Frontend Architecture

The frontend should use a feature-oriented structure.

Recommended structure:

```text
frontend/
├── public/
├── src/
│   ├── assets/
│   ├── components/
│   ├── layouts/
│   ├── pages/
│   ├── features/
│   │   ├── search/
│   │   ├── journeys/
│   │   ├── ranks/
│   │   ├── routes/
│   │   ├── fares/
│   │   └── admin/
│   ├── hooks/
│   ├── services/
│   ├── store/
│   ├── i18n/
│   ├── types/
│   ├── utils/
│   ├── constants/
│   ├── App.tsx
│   └── main.tsx
├── package.json
├── tsconfig.json
└── vite.config.ts
```

---

# 10. Frontend Pages

The MVP shall contain the following primary pages.

## Public Pages

### Home

Purpose:

* Introduce the platform
* Provide journey search
* Provide access to supported locations

### Search Results

Purpose:

* Display available journey options
* Display fare information
* Display journey duration
* Display transfers
* Display verification status

### Journey Details

Purpose:

* Explain the selected journey
* Display step-by-step instructions
* Display taxi ranks
* Display transfers
* Display fare
* Display map

### Taxi Rank Details

Purpose:

* Display taxi rank information
* Display location
* Display associated routes
* Display map position

### About / Information

Purpose:

* Explain the platform
* Explain data verification
* Explain coverage
* Explain limitations

---

# 11. Administrative Frontend

The MVP shall include a basic administrator interface.

Recommended sections:

```text
Admin Dashboard
│
├── Locations
├── Taxi Ranks
├── Routes
├── Route Steps
├── Fares
└── Verification
```

The admin interface should prioritise data maintenance rather than analytics.

Advanced dashboards are not required for MVP.

---

# 12. Backend Architecture

Recommended backend structure:

```text
backend/
├── app/
│   ├── api/
│   │   ├── routes/
│   │   └── dependencies/
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── logging.py
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── repositories/
│   ├── database/
│   ├── utils/
│   └── main.py
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
│
├── requirements.txt
└── README.md
```

The backend should separate:

* API routing
* Validation
* Business logic
* Database access
* Authentication
* Configuration
* External services

---

# 13. API Requirements

The backend shall expose a REST API.

Base path:

```text
/api/v1
```

All API responses should use JSON.

---

# 14. Core API Endpoints

## 14.1 Locations

### Search locations

```http
GET /api/v1/locations/search?q=tladi
```

Purpose:

Return matching supported locations.

### Get location

```http
GET /api/v1/locations/{location_id}
```

---

# 15. Journey Search API

The central API endpoint shall be:

```http
GET /api/v1/journeys/search
```

Example:

```text
/api/v1/journeys/search?origin=tladi&destination=bara
```

The API should return structured journey information.

Example response concept:

```json
{
  "origin": {
    "id": 1,
    "name": "Tladi"
  },
  "destination": {
    "id": 2,
    "name": "Bara"
  },
  "journeys": [
    {
      "id": 1001,
      "estimated_fare": 20,
      "currency": "ZAR",
      "estimated_duration_minutes": 35,
      "transfers": 0,
      "verification_status": "verified",
      "last_verified_at": "2026-09-15",
      "steps": []
    }
  ]
}
```

The actual API response structure will be finalised during implementation.

---

# 16. Journey Details API

```http
GET /api/v1/journeys/{journey_id}
```

The endpoint shall return:

* Origin
* Destination
* Route steps
* Taxi ranks
* Transfers
* Fare information
* Estimated duration
* Verification status
* Last verification date
* Map-related coordinates

---

# 17. Taxi Rank API

### List taxi ranks

```http
GET /api/v1/taxi-ranks
```

### Taxi rank details

```http
GET /api/v1/taxi-ranks/{rank_id}
```

### Nearby ranks

A future-compatible endpoint may be implemented as:

```http
GET /api/v1/taxi-ranks/nearby
```

This should only be included in MVP if the nearby-rank functionality is implemented.

---

# 18. Route API

### List routes

```http
GET /api/v1/routes
```

### Route details

```http
GET /api/v1/routes/{route_id}
```

Routes should contain enough information to describe a supported taxi journey.

---

# 19. Fare API

### Get fare information

```http
GET /api/v1/routes/{route_id}/fares
```

Fare records should include:

* Amount
* Currency
* Effective date
* Verification status
* Source
* Last verified date

---

# 20. Administrative API

Administrative endpoints shall be protected.

Example:

```text
POST   /api/v1/admin/locations
PUT    /api/v1/admin/locations/{id}
DELETE /api/v1/admin/locations/{id}

POST   /api/v1/admin/taxi-ranks
PUT    /api/v1/admin/taxi-ranks/{id}

POST   /api/v1/admin/routes
PUT    /api/v1/admin/routes/{id}

POST   /api/v1/admin/fares
PUT    /api/v1/admin/fares/{id}
```

The exact endpoint structure may be refined during backend implementation.

---

# 21. API Validation

The backend shall validate:

* Required fields
* Data types
* Coordinates
* Fare amounts
* Route relationships
* Location references
* Verification statuses
* Date values

Invalid requests shall return appropriate HTTP status codes.

Examples:

```text
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
422 Validation Error
500 Internal Server Error
```

---

# 22. Database Architecture

The initial database should use a relational model.

Core entities:

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
```

Additional entities may include:

```text
Verification
AdminUser
TransportAssociation
```

---

# 23. Core Database Entities

## 23.1 Location

Suggested fields:

```text
id
name
slug
location_type
description
address
municipality
city
province
latitude
longitude
is_active
created_at
updated_at
```

Possible location types:

```text
suburb
township
city
taxi_rank
landmark
destination
transport_hub
```

---

# 24. Taxi Rank

Suggested fields:

```text
id
name
slug
location_id
description
address
latitude
longitude
operating_information
is_active
created_at
updated_at
```

A taxi rank may be associated with multiple routes.

---

# 25. Route

Suggested fields:

```text
id
name
origin_location_id
destination_location_id
description
status
verification_status
last_verified_at
source
is_active
created_at
updated_at
```

Possible statuses:

```text
active
temporarily_unavailable
inactive
```

---

# 26. Route Step

A route may contain multiple steps.

Suggested fields:

```text
id
route_id
step_order
from_rank_id
to_rank_id
instruction
estimated_duration_minutes
created_at
updated_at
```

This structure supports journeys such as:

```text
Tladi
  ↓
Rank A
  ↓
Taxi 1
  ↓
Rank B
  ↓
Taxi 2
  ↓
Bara
```

---

# 27. Fare

Suggested fields:

```text
id
route_id
amount
currency
effective_from
effective_to
verification_status
source
last_verified_at
created_at
updated_at
```

The default currency shall be:

```text
ZAR
```

The frontend should display this as:

```text
R20
```

rather than requiring users to understand currency codes.

---

# 28. Verification Status

The system shall support verification states.

Minimum values:

```text
verified
community_reported
unverified
outdated
unavailable
```

The database should use controlled values rather than arbitrary text wherever practical.

---

# 29. Data Sources

The MVP database may be populated from:

* Manually researched information
* Verified transport information
* Publicly available information
* Appropriate local knowledge
* Administrator-entered data

Every publicly displayed route should have an identifiable source or verification status.

The system must not treat generated AI content as an authoritative transport data source.

---

# 30. Data Freshness

Route and fare records should support timestamps.

At minimum:

```text
created_at
updated_at
last_verified_at
```

Fare information should also support effective dates.

This allows the system to distinguish between:

```text
Current verified fare
```

and:

```text
Older/outdated fare
```

---

# 31. Authentication and Authorization

Public journey searches shall not require an account.

Administrative functionality shall require authentication.

The MVP should use role-based access control.

Minimum role:

```text
ADMIN
```

The architecture should allow additional roles later:

```text
MODERATOR
USER
```

---

# 32. Administrative Security

Administrator endpoints must:

* Require authentication
* Validate user permissions
* Reject unauthorized requests
* Avoid exposing sensitive configuration
* Log important administrative actions

Administrative credentials must never be hard-coded into the source code.

---

# 33. Environment Configuration

Sensitive configuration shall be stored using environment variables.

Example:

```env
APP_ENV=development

DATABASE_URL=postgresql://...

API_BASE_URL=http://localhost:8000

CORS_ORIGINS=http://localhost:5173

SECRET_KEY=...

MAP_TILE_URL=...
```

A `.env.example` file shall document required configuration without containing real credentials.

---

# 34. CORS

The backend shall explicitly configure allowed frontend origins.

Development example:

```text
http://localhost:5173
```

Production origins shall be configured through environment variables.

Wildcard CORS should not be used in production unless there is a documented reason.

---

# 35. Security Requirements

The system shall follow basic secure-development practices.

Requirements include:

* No hard-coded secrets
* Passwords must never be stored in plaintext
* Authentication tokens must be protected
* Input validation
* SQL injection prevention through ORM/parameterised queries
* Appropriate CORS configuration
* HTTPS in production
* Secure environment variables
* Administrative endpoint protection
* Error responses must not expose sensitive internals

---

# 36. API Error Format

API errors should use a consistent structure.

Example:

```json
{
  "error": {
    "code": "ROUTE_NOT_FOUND",
    "message": "No supported taxi journey was found for this origin and destination."
  }
}
```

Error messages shown to users should be understandable.

Technical stack traces must not be returned to users in production.

---

# 37. Search Behaviour

The search system should initially use structured database queries.

The MVP should support:

* Exact location matching
* Partial matching
* Case-insensitive matching
* Location suggestions
* Taxi rank names
* Area names
* City names

The search system should not generate unsupported routes.

If no route exists in the dataset:

```text
No supported taxi journey was found for this route.
```

The application must not guess.

---

# 38. Journey Calculation

The MVP shall not attempt to automatically calculate arbitrary taxi routes across the entire country.

Instead, journeys shall be based on known structured route data.

A journey may consist of:

```text
Direct route
```

or:

```text
Route A
+
Transfer
+
Route B
```

Only validated route combinations should be presented.

A future routing engine may expand this capability.

---

# 39. Fare Calculation

For a direct journey:

```text
Total Fare = Stored Route Fare
```

For a validated multi-leg journey:

```text
Total Fare =
Fare Leg 1
+
Fare Leg 2
+
...
```

The UI must label this as an:

**Estimated fare**

unless the product later establishes a stronger guarantee.

The system must not predict fares using AI in the MVP.

---

# 40. Journey Duration

Journey duration shall be stored or estimated for supported routes.

Example:

```text
Estimated travel time:
35–45 minutes
```

The application must clearly communicate that this is an estimate.

The MVP shall not claim guaranteed arrival times.

---

# 41. Internationalisation

The frontend shall use an internationalisation framework.

Recommended:

```text
i18next
react-i18next
```

Translation resources should be separated from application code.

Example:

```text
src/i18n/
├── index.ts
├── locales/
│   ├── en/
│   │   └── translation.json
│   ├── zu/
│   │   └── translation.json
│   └── xh/
│       └── translation.json
```

English will be the initial complete language.

The architecture must allow the remaining supported South African languages to be added without rewriting application components.

---

# 42. Accessibility

The frontend shall follow accessible web-development practices.

Requirements include:

* Semantic HTML
* Keyboard navigation
* Accessible form labels
* Visible focus states
* Appropriate ARIA usage
* Screen-reader-compatible controls
* Sufficient colour contrast
* Responsive text
* Accessible error messages
* Accessible map alternatives

Important journey information should not exist only visually on a map.

The textual journey instructions must remain available.

---

# 43. Responsive Design

The interface shall support:

### Mobile

Primary target.

### Tablet

Secondary target.

### Desktop

Secondary target.

The layout should adapt rather than simply scale down the desktop interface.

---

# 44. State Management

The application should avoid global state unless required.

Local React state should be preferred for:

* Search form state
* Loading states
* Temporary UI state
* Form state

Global state may be used for:

* Language preference
* Authenticated administrator state
* Shared application configuration

The project should not introduce Redux or another large state-management library unless actual application complexity requires it.

---

# 45. API Client

The frontend should centralise API communication.

Recommended structure:

```text
src/services/
├── api.ts
├── locationService.ts
├── journeyService.ts
├── routeService.ts
├── taxiRankService.ts
└── adminService.ts
```

Components should not contain repeated raw API request logic.

---

# 46. Loading States

The application shall provide loading feedback when waiting for API requests.

Examples:

```text
Searching taxi routes...
Loading journey...
Loading taxi rank...
```

The interface should avoid leaving users uncertain whether their request was received.

---

# 47. Empty States

The application shall provide useful empty states.

Example:

```text
No supported taxi journey found.

We currently don't have verified journey information
for this route.

Try another destination or search area.
```

---

# 48. Map Failure Handling

If the map cannot load, journey information should still remain usable.

Example:

```text
Map unavailable

The journey information is still available below.
```

The map must not become a single point of failure for the journey experience.

---

# 49. Logging

The backend shall use structured application logging.

Important events may include:

* API errors
* Authentication failures
* Administrative changes
* Database errors
* External map/service failures

Sensitive information must not be written to logs.

---

# 50. Testing Requirements

Testing shall occur at multiple levels.

## Unit Tests

Test:

* Fare calculations
* Journey validation
* Route logic
* Data validation
* Utility functions

## Integration Tests

Test:

* API endpoints
* Database operations
* Authentication
* Route searches

## Frontend Tests

Test:

* Search form
* Results rendering
* Journey details
* Error states
* Language selection

## End-to-End Tests

Important user journey:

```text
Open application
      ↓
Select origin
      ↓
Select destination
      ↓
Search
      ↓
View result
      ↓
Open journey
      ↓
View map
```

---

# 51. Minimum Test Scenarios

The MVP must test at least:

### Successful Search

```text
Tladi → Bara
```

when the route exists in the test database.

### Unsupported Search

```text
Unsupported Location A → Unsupported Location B
```

Expected result:

```text
No supported journey found.
```

### Multi-Taxi Journey

Test a route requiring at least one transfer.

### Fare

Verify that stored fare information appears correctly.

### Map

Verify that relevant coordinates are displayed.

### Admin

Verify that an administrator can create and update:

* Locations
* Taxi ranks
* Routes
* Fares

### Invalid Data

Verify that invalid coordinates, missing required fields, and invalid relationships are rejected.

---

# 52. Database Migrations

Database schema changes shall be managed through migrations.

Recommended tool:

```text
Alembic
```

Developers should not manually modify production database schemas without a corresponding migration.

Migration files must be version controlled.

---

# 53. Seed Data

The project shall include seed data for development and testing.

Recommended structure:

```text
database/
├── migrations/
├── seeds/
└── README.md
```

Seed data should include representative:

* Locations
* Taxi ranks
* Routes
* Route steps
* Fares

The initial seed dataset should be clearly marked as development/test data unless independently verified.

---

# 54. Development Environment

The application should support local development on Windows, macOS, and Linux where practical.

Minimum development tools:

* Node.js
* npm
* Python
* PostgreSQL
* Git
* GitHub

Docker may be used to simplify local database and backend setup.

---

# 55. Recommended Local Development Setup

Development architecture:

```text
Frontend
localhost:5173

        ↓

Backend
localhost:8000

        ↓

PostgreSQL
localhost:5432
```

Exact ports may be changed through environment configuration.

---

# 56. Docker

Docker is recommended for reproducible development environments.

Potential services:

```text
frontend
backend
postgres
```

However, the frontend does not necessarily need to run inside Docker during normal development.

A simple local development workflow should remain available:

```powershell
npm run dev
```

and:

```powershell
uvicorn app.main:app --reload
```

---

# 57. Deployment Architecture

The initial production architecture may use:

```text
User
 ↓
Frontend Hosting
 ↓ HTTPS
FastAPI Backend
 ↓
Managed PostgreSQL
```

Potential service categories:

### Frontend

* Vercel
* Netlify
* Cloudflare Pages

### Backend

* Render
* Railway
* Fly.io
* Other managed container/server hosting

### Database

* Supabase PostgreSQL
* Neon
* Managed PostgreSQL provider

The final provider selection will be made after evaluating:

* Cost
* South African accessibility
* Reliability
* Deployment simplicity
* Database compatibility
* Scaling requirements

---

# 58. CI/CD

The project should use GitHub-based version control.

The eventual CI pipeline should run:

```text
Install dependencies
       ↓
Lint
       ↓
Type checking
       ↓
Unit tests
       ↓
Integration tests
       ↓
Build
```

Deployment should only occur after the required checks pass.

---

# 59. Git Requirements

The repository should use clear commit messages.

Recommended format:

```text
feat: add journey search endpoint
fix: handle unsupported route search
docs: update technical requirements
test: add journey search integration tests
refactor: separate route service
```

Feature branches should be used for significant changes.

---

# 60. Code Quality

The project shall use:

### Frontend

* TypeScript strict mode
* ESLint
* Prettier

### Backend

* Python type hints
* Ruff or equivalent linting
* Formatting
* Pydantic validation
* Clear module boundaries

Code should favour readability over unnecessary abstraction.

---

# 61. Configuration Management

Configuration must be environment-specific.

Example:

```text
.env
.env.example
```

Production secrets must never be committed to Git.

The `.gitignore` file must include:

```text
.env
.env.*
!.env.example
```

where appropriate for the selected configuration strategy.

---

# 62. API Documentation

FastAPI's automatically generated documentation shall be enabled for development.

Expected endpoints:

```text
/docs
/redoc
```

The API documentation should describe:

* Endpoint purpose
* Parameters
* Request schemas
* Response schemas
* Error responses

---

# 63. Database Backup

Production database backups shall be enabled through the selected database provider.

The project should define:

* Backup frequency
* Retention period
* Recovery procedure

before production launch.

---

# 64. Privacy

The MVP should minimise collection of personal information.

Because public route search does not require an account, the MVP should not require users to provide:

* Full name
* Phone number
* Email address
* Identity information

Location permission should only be requested if the user activates a feature requiring location information.

---

# 65. Analytics

Detailed analytics are not required for the first development version.

If analytics are introduced, they should focus on product improvement rather than unnecessary personal-data collection.

Potential anonymous metrics:

* Number of searches
* Supported/unsupported searches
* Popular locations
* Error rates

Analytics implementation must comply with applicable privacy requirements.

---

# 66. AI Boundary

AI is explicitly outside the MVP technical architecture.

The MVP shall not require:

* LLM APIs
* Vector databases
* Embedding pipelines
* AI agents
* AI route generation
* AI fare prediction
* AI chatbot infrastructure

The architecture should, however, expose clean APIs that could later be consumed by an AI assistant.

Future architecture:

```text
User
 ↓
AI Assistant
 ↓
Verified TaxiFind API
 ↓
PostgreSQL
```

The AI layer must retrieve route information rather than inventing it.

---

# 67. Scalability Requirements

The initial architecture should support future expansion from:

```text
Gauteng pilot
```

to:

```text
South Africa
```

without requiring a complete rewrite.

Geographic entities should therefore include:

* Province
* Municipality
* City
* Area
* Coordinates

The system must not hard-code Gauteng into route logic.

---

# 68. Performance Requirements

Initial performance targets:

* Search API should normally respond within a few seconds under normal load.
* Static frontend assets should be efficiently bundled.
* Images should be optimised.
* Database queries should use appropriate indexes.
* Location searches should be indexed.

Performance targets may be tightened after real usage measurements.

---

# 69. Database Indexing

Indexes should be created for frequently queried fields.

Potential indexes:

```text
Location.name
Location.slug
Location.city
Location.province

TaxiRank.name
TaxiRank.location_id

Route.origin_location_id
Route.destination_location_id
Route.status

Fare.route_id
Fare.effective_from
```

Indexes should be based on actual query patterns as the system develops.

---

# 70. Data Integrity

Database relationships should enforce valid references.

For example:

```text
Route
 ├── origin_location_id → Location
 └── destination_location_id → Location
```

A route should not reference a nonexistent location.

Similarly:

```text
Fare → Route
RouteStep → Route
RouteStep → TaxiRank
```

should use appropriate foreign-key constraints.

---

# 71. API Versioning

The API shall use versioned routes:

```text
/api/v1/
```

Future breaking changes can then be introduced through:

```text
/api/v2/
```

without immediately breaking existing clients.

---

# 72. Documentation Requirements

The repository shall contain:

```text
README.md
```

The README should explain:

* Project purpose
* Architecture
* Requirements
* Local setup
* Environment variables
* Database setup
* Running frontend
* Running backend
* Running tests
* Deployment overview

Separate documentation should explain database and contribution procedures where necessary.

---

# 73. Recommended Repository Structure

The complete project should initially follow:

```text
taxifind-sa/
│
├── docs/
│   ├── 01-project-requirements.md
│   ├── 02-technical-requirements.md
│   ├── 03-app-flow.md
│   ├── 04-ui-ux-design-brief.md
│   ├── 05-backend-schema.md
│   └── 06-implementation-plan.md
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── layouts/
│   │   ├── pages/
│   │   ├── features/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── store/
│   │   ├── i18n/
│   │   ├── types/
│   │   ├── utils/
│   │   ├── constants/
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── README.md
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   └── dependencies/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── repositories/
│   │   ├── database/
│   │   ├── utils/
│   │   └── main.py
│   ├── tests/
│   │   ├── unit/
│   │   ├── integration/
│   │   └── fixtures/
│   ├── requirements.txt
│   └── README.md
│
├── database/
│   ├── migrations/
│   ├── seeds/
│   └── README.md
│
├── scripts/
│   ├── seed_database.py
│   ├── import_routes.py
│   └── verify_data.py
│
├── tests/
│   ├── e2e/
│   └── test-data/
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
└── LICENSE
```

---

# 74. MVP Technical Acceptance Criteria

The technical implementation shall be considered MVP-ready when:

### Frontend

* React application builds successfully.
* TypeScript compilation succeeds.
* Responsive layouts work on mobile and desktop.
* Search interface is functional.
* Journey results render correctly.
* Journey details render correctly.
* Maps display supported locations.
* Loading and error states are implemented.

### Backend

* FastAPI application starts successfully.
* API versioning is implemented.
* Database connection works.
* Location search works.
* Journey search works.
* Journey details work.
* Taxi rank endpoints work.
* Fare information is available.
* Administrative endpoints are protected.

### Database

* PostgreSQL is operational.
* Migrations work.
* Seed data can be loaded.
* Foreign-key relationships are enforced.
* Relevant indexes exist.

### Security

* Secrets are stored outside source control.
* Admin endpoints require authentication.
* Unauthorized users cannot modify transport data.
* Production API uses HTTPS.

### Quality

* Core automated tests pass.
* API documentation is available.
* README setup instructions work on a clean development environment.

---

# 75. MVP Technical Boundary

The following table defines the technical boundary of the first implementation.

| Capability                 |      MVP |
| -------------------------- | -------: |
| React frontend             |        ✅ |
| TypeScript                 |        ✅ |
| Vite                       |        ✅ |
| FastAPI                    |        ✅ |
| Python                     |        ✅ |
| PostgreSQL                 |        ✅ |
| REST API                   |        ✅ |
| Taxi journey search        |        ✅ |
| Location search            |        ✅ |
| Taxi ranks                 |        ✅ |
| Route steps                |        ✅ |
| Multi-taxi journeys        |        ✅ |
| Estimated fares            |        ✅ |
| Estimated journey duration |        ✅ |
| Maps                       |        ✅ |
| OpenStreetMap              |        ✅ |
| Leaflet                    |        ✅ |
| Verification status        |        ✅ |
| Last verified date         |        ✅ |
| Admin route management     |        ✅ |
| Admin fare management      |        ✅ |
| Admin rank management      |        ✅ |
| English UI                 |        ✅ |
| i18n architecture          |        ✅ |
| Additional language        | Optional |
| User accounts              |        ❌ |
| Saved routes               |        ❌ |
| Community reporting        |        ❌ |
| AI assistant               |        ❌ |
| Voice search               |        ❌ |
| Live taxi tracking         |        ❌ |
| Taxi booking               |        ❌ |
| Online payments            |        ❌ |
| Push notifications         |        ❌ |
| Offline-first mode         |        ❌ |
| Other transport modes      |        ❌ |
| Nationwide route coverage  |        ❌ |

---

# 76. Technical Design Principle

The most important technical principle for the MVP is:

> **Build a reliable structured transport information system first; add intelligent features later.**

The backend database is therefore the source of truth for:

* Locations
* Taxi ranks
* Routes
* Transfers
* Fares
* Journey information
* Verification status

The frontend presents this information clearly to commuters.

Future AI, voice, community, and transport integrations should consume this structured foundation rather than replacing it.

---

# 77. Document Status

**Document:** Technical Requirements Document
**Version:** 1.0
**Status:** Draft
**Previous Document:** Project Requirements Document
**Next Document:** App Flow

This document defines the technical foundation for the TaxiFind SA MVP. Detailed user journeys, navigation flows, screen transitions, and application behaviour will be defined in the App Flow document.
