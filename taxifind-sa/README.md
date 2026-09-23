# TaxiFind SA

TaxiFind SA is a minibus taxi journey information platform designed to help commuters understand supported taxi journeys between locations.

The initial release will operate as a **controlled Gauteng pilot** using a deliberately limited, structured and verified dataset.

TaxiFind is an information platform. It is not a taxi booking, ride-hailing, payment or live vehicle-tracking application.

## Project Goal

The core user journey is:

```text
Open TaxiFind
    ↓
Select From
    ↓
Select To
    ↓
Search
    ↓
View supported journey
    ↓
Understand route and taxi changes
    ↓
View estimated fare and duration
    ↓
View taxi rank and map information
```

The application should provide clear, reliable information without inventing unsupported taxi routes, fares or journey details.

## MVP Geographic Focus

The initial pilot focuses on selected supported taxi routes in Gauteng, with particular attention to:

* Soweto
* Johannesburg
* Vaal
* Midrand

The MVP does **not** claim to contain the complete Gauteng or South African taxi network.

The route dataset will be intentionally limited and expanded as information is researched, verified and maintained.

## MVP Features

* Taxi journey search
* Origin and destination selection
* Location suggestions
* Supported taxi routes
* Taxi rank information
* Route steps
* Supported multi-taxi journeys
* Estimated fares
* Estimated journey duration
* Map information
* Route verification status
* Last verified date
* Admin route and fare management
* Responsive mobile-friendly interface
* English language support
* Internationalisation architecture
* Accessibility-focused design

## Outside the MVP

The following are not part of the initial release:

* User registration
* Saved journeys
* Community reporting
* AI-powered search
* Voice search
* Live taxi tracking
* Taxi booking
* Online payments
* Push notifications
* Offline functionality
* Other public transport modes
* Nationwide taxi coverage

These features may be considered after the core information platform has been established.

## Important Route Data Principle

TaxiFind SA will launch with a deliberately limited, structured and verified dataset covering selected Gauteng taxi routes.

The MVP does not assume comprehensive knowledge of the South African minibus taxi network.

Only journeys supported by the application's available route data should be presented as supported journeys.

The absence of a journey from the dataset must not be interpreted as evidence that the journey does not exist in the real-world taxi network.

Where route, fare, transfer, duration or map information is unavailable or insufficiently verified, the application must clearly communicate that limitation rather than infer or generate the missing information.

## Technology Stack

### Frontend

* React
* TypeScript
* Vite
* React Router
* Leaflet
* React-Leaflet
* i18next
* react-i18next

### Backend

* Python
* FastAPI
* Pydantic
* SQLAlchemy
* Alembic
* Uvicorn

### Database

* PostgreSQL
* PostGIS where geospatial functionality requires it

### Architecture

```text
React + TypeScript + Vite
          ↓
       REST API
          ↓
       FastAPI
          ↓
      PostgreSQL
```

Maps will use:

```text
Leaflet
   ↓
OpenStreetMap
```

## Repository Structure

```text
taxifind-sa/
├── docs/
├── frontend/
├── backend/
├── database/
├── scripts/
├── tests/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
└── LICENSE
```

## Documentation

The project documentation is maintained in the `docs/` directory.

1. `01-project-requirements.md` — Project Requirements Document
2. `02-technical-requirements.md` — Technical Requirements Document
3. `03-app-flow.md` — Application Flow
4. `04-ui-ux-design-brief.md` — UI/UX Design Brief
5. `05-backend-schema.md` — Backend Schema
6. `06-implementation-plan.md` — Implementation Plan

These documents define the intended MVP before implementation expands beyond the agreed scope.

## Development

The planned local development environment is:

| Component  | Default                 |
| ---------- | ----------------------- |
| Frontend   | `http://localhost:5173` |
| Backend    | `http://localhost:8000` |
| PostgreSQL | `localhost:5432`        |

Detailed setup instructions will be added as the implementation progresses.

## Data Transparency

TaxiFind displays information according to its available route dataset.

Where applicable, journey information should identify:

* Verification status
* Last verified date
* Source information
* Estimated fare
* Estimated duration
* Supported transfer information

Users should be able to distinguish verified information from information that requires further verification.

## Development Principle

> Build a reliable structured transport information system first; add intelligent features later.

The first priority is making the core journey understandable, transparent and dependable.

## Project Status

**Current stage:** Phase 1 — Project Foundation

**Status:** Initial repository setup

## License

License information will be finalised during the project foundation stage.
