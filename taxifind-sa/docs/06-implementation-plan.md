# TaxiFind SA — Implementation Plan

**Version:** 1.1
**Status:** Draft
**Initial Geographic Focus:** Gauteng controlled pilot

**Related documents:**

* `docs/01-project-requirements.md` — Project Requirements Document
* `docs/02-technical-requirements.md` — Technical Requirements Document
* `docs/03-app-flow.md` — Application Flow
* `docs/04-ui-ux-design-brief.md` — UI/UX Design Brief
* `docs/05-backend-schema.md` — Backend Schema
* `docs/06-implementation-plan.md` — This document

---

## 1. Purpose

This document translates the TaxiFind SA product, technical, UX, data and backend requirements into an ordered development plan.

The implementation should prioritise the smallest reliable version of the core commuter journey:

> **From location → To location → Search → Supported journey → Journey details → Map**

The MVP must provide reliable structured information for a deliberately limited set of supported taxi journeys rather than attempting to model the entire South African minibus taxi network.

---

# 2. Implementation Principles

The implementation follows these principles:

1. Build the core commuter journey before secondary features.
2. Build structured route data before intelligent features.
3. Only expose journeys supported by verified or appropriately sourced data.
4. Never generate unsupported routes, fares or journey instructions.
5. Treat fare and duration information as estimates.
6. Represent known multi-leg journeys explicitly rather than creating an unrestricted routing engine.
7. Keep the frontend, backend and database independently testable.
8. Build i18n and accessibility into the application rather than adding them at the end.
9. Keep the architecture capable of national expansion without claiming nationwide coverage before the data supports it.
10. AI, voice, community reporting and other advanced capabilities remain outside the MVP.

---

# 3. MVP Boundary

The MVP covers:

* Selected Gauteng taxi routes.
* Initial pilot areas including Soweto, Johannesburg, Vaal and Midrand.
* Structured origin and destination search.
* Location suggestions.
* Supported direct journeys.
* Curated supported multi-leg journeys.
* Taxi rank information.
* Route steps.
* Estimated fares.
* Estimated journey duration.
* Transfer instructions.
* Verification status.
* Last verified date.
* Leaflet/OpenStreetMap mapping.
* Optional nearby taxi-rank discovery.
* Basic administrative data management.
* Responsive mobile and desktop interfaces.
* English.
* i18n architecture for future South African languages.

The MVP does **not** include:

* Nationwide taxi coverage.
* Arbitrary automatic route generation.
* AI search.
* Voice search.
* Taxi booking.
* Live taxi tracking.
* Driver GPS.
* Online payments.
* User accounts.
* Saved journeys.
* Community reporting.
* Push notifications.
* Offline functionality.
* Other public transport modes.

---

# 4. Development Phases

The phases below are deliberately numbered in the exact order in which the MVP should be implemented.

## Phase 1 — Project Foundation

### Objectives

Establish the repository, development environment and basic project structure.

### Tasks

* Create Git repository.
* Create the documented folder structure.
* Configure frontend project.
* Configure backend project.
* Create `.env.example`.
* Configure `.gitignore`.
* Create initial README.
* Establish development branch strategy.
* Configure basic linting/formatting where appropriate.
* Confirm local development commands.
* Establish frontend/backend environment variables.

### Initial structure

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

### Acceptance criteria

* Repository can be cloned and started.
* Frontend starts successfully.
* Backend starts successfully.
* Environment configuration is documented.
* No secrets are committed.
* Basic README instructions work on a clean development environment.

---

# Phase 2 — Frontend Foundation

### Objectives

Create the basic React application architecture and reusable UI foundation.

### Tasks

* Configure React + TypeScript + Vite.
* Configure React Router.
* Create application layout.
* Create public navigation.
* Create page structure.
* Create reusable buttons, inputs, cards and status components.
* Establish design tokens.
* Configure responsive base styles.
* Configure initial i18n architecture.
* Establish frontend API service structure.

### Initial pages

* Home
* Search Results
* Journey Details
* Taxi Rank Details
* About

### Acceptance criteria

* Application loads without errors.
* Routes work.
* Responsive base layout works.
* Reusable components can be used across pages.
* API configuration is environment-based.

---

# Phase 3 — Database Foundation

### Objectives

Implement the PostgreSQL database and core data model.

### Core models

* `Location`
* `TaxiRank`
* `Route`
* `RouteStep`
* `Fare`
* `Journey`
* `JourneyLeg`
* `Verification`
* `AdminUser`
* `AuditLog`

### Tasks

* Configure PostgreSQL.
* Configure SQLAlchemy.
* Configure Alembic.
* Create initial migrations.
* Add foreign keys.
* Add uniqueness constraints.
* Add indexes.
* Add timestamps.
* Add active/status fields.
* Add verification fields.
* Add source/provenance fields.
* Add fare effective dates.
* Add route-step ordering constraints.
* Add journey-leg ordering.
* Add database tests.

### Important design rule

A multi-leg journey should be represented explicitly through `Journey` and `JourneyLeg`.

The MVP should **not** attempt to discover arbitrary taxi combinations at runtime.

### Acceptance criteria

* Database can be created from migrations.
* All MVP entities exist.
* Relationships are enforced.
* Invalid references are rejected.
* Route steps and journey legs maintain predictable ordering.
* Database tests pass.

---

# Phase 4 — Backend/API Foundation

### Objectives

Create the FastAPI application and common backend infrastructure.

### Tasks

* Configure FastAPI.
* Configure application settings.
* Configure database sessions.
* Configure CORS.
* Configure API versioning.
* Create API error format.
* Create Pydantic schemas.
* Create repository layer.
* Create service layer.
* Create dependency structure.
* Add health endpoint.
* Add logging.
* Add API documentation.

### Initial endpoint

```text
GET /api/v1/health
```

### Acceptance criteria

* Backend starts successfully.
* Database connection works.
* Health endpoint responds.
* API versioning is established.
* Errors use a consistent structure.
* Swagger/OpenAPI documentation is available.

---

# Phase 5 — Location Search

### Objectives

Allow commuters to find supported origin and destination locations.

### Tasks

* Implement location repository.
* Implement location service.
* Implement location search API.
* Implement location suggestions.
* Support partial matching.
* Support case-insensitive search.
* Support supported location types.
* Connect frontend search inputs to the API.
* Implement loading states.
* Implement empty states.
* Implement validation.

### Endpoint

```text
GET /api/v1/locations/search?q=tladi
```

### Acceptance criteria

A commuter can:

1. Open the home page.
2. Select a From location.
3. Select a To location.
4. See supported suggestions.
5. Submit a valid search.

---

# Phase 6 — Journey Search and Results

### Objectives

Implement the main TaxiFind search capability.

### Endpoint

```text
GET /api/v1/journeys/search?origin=tladi&destination=bara
```

### Tasks

* Implement journey search service.
* Support direct journeys.
* Support explicitly curated multi-leg journeys.
* Return route steps.
* Return fare information.
* Return estimated duration.
* Return transfer information.
* Return verification status.
* Return last verified date.
* Implement unsupported journey response.
* Build search results page.
* Build journey result cards.
* Add loading states.
* Add empty states.
* Add error states.

### Important rule

If the database does not contain sufficient supported information for a journey, the API must return an explicit unsupported/no-supported-data response.

It must not generate a route.

### Acceptance criteria

A valid supported search produces one or more journey options.

An unsupported search produces a clear message such as:

> No supported TaxiFind journey is currently available for this search.

The message must not imply that the real-world taxi journey does not exist.

---

# Phase 7 — Journey Details

### Objectives

Provide the complete instructions needed to understand a supported journey.

### Tasks

* Implement journey detail API.
* Create journey detail page.
* Display origin.
* Display boarding rank.
* Display route.
* Display get-off location.
* Display transfer information.
* Display next taxi/leg.
* Display destination.
* Display fare.
* Display duration.
* Display verification status.
* Display last verified date.
* Build journey timeline.
* Build transfer cards.
* Add map placeholder/container.

### Acceptance criteria

A tester should be able to determine, without using the map:

1. Where the journey starts.
2. Where to catch the taxi.
3. Which taxi/route to take.
4. Where to get off.
5. Whether a transfer is required.
6. Where to make the transfer.
7. Which next taxi/route to take.
8. Where the journey ends.
9. The estimated fare.
10. The estimated duration.

---

# Phase 8 — Maps

### Objectives

Add geographic context without creating false route precision.

### Technology

* Leaflet
* OpenStreetMap
* React-Leaflet

### Tasks

* Create reusable map component.
* Display origin.
* Display boarding rank.
* Display transfer ranks where applicable.
* Display destination.
* Display relevant location markers.
* Add map controls.
* Add marker information.
* Add responsive map container.
* Handle map loading failures.
* Provide textual journey information outside the map.

### Important rule

Do not draw an apparently precise taxi route line unless reliable route geometry is available.

The map must not imply accuracy that the underlying data does not support.

### Acceptance criteria

* Map displays on supported journey pages.
* Markers are selectable.
* Map works on mobile and desktop.
* Journey remains usable if the map fails.
* Core journey information is not dependent on the map.

---

# Phase 9 — Taxi Rank and Route Browsing

### Objectives

Provide supporting ways to explore structured TaxiFind information.

### Tasks

* Taxi rank list.
* Taxi rank detail page.
* Route browsing.
* Route detail page.
* Supported route information.
* Rank-to-route relationships.
* Optional nearby taxi rank functionality.

### Acceptance criteria

Users can inspect a taxi rank and understand:

* Its name.
* Its area.
* Its location.
* Supported routes where available.
* Verification information where available.

---

# Phase 10 — Admin System

### Objectives

Provide the minimum administrative tools required to maintain reliable route information.

### Admin capabilities

* Admin authentication.
* Dashboard.
* Location management.
* Taxi rank management.
* Route management.
* Route-step management.
* Fare management.
* Journey management.
* Verification management.
* Audit-log viewing.

### Tasks

* Implement admin authentication.
* Protect admin endpoints.
* Create admin layout.
* Create CRUD interfaces.
* Add validation.
* Add verification actions.
* Add outdated/unverify actions.
* Add audit logging.
* Add deliberate confirmation for destructive operations.

### Acceptance criteria

An administrator can manage the core data without modifying source code.

---

# Phase 11 — Route Data Loading and Verification

### Objectives

Populate the controlled Gauteng pilot dataset with structured, reviewed information.

### Initial focus

* Soweto
* Johannesburg
* Vaal
* Midrand

### Planning targets

The initial dataset may target approximately:

* **10–20 taxi ranks**
* **20–50 supported routes**
* **20–50 fare records**

These are planning targets rather than hard release requirements. Data quality is more important than reaching a specific count.

### Data workflow

```text
Research / Data Collection
        ↓
Create Location
        ↓
Create Taxi Rank
        ↓
Create Route
        ↓
Add Route Steps
        ↓
Add Fare
        ↓
Record Source
        ↓
Admin Review
        ↓
Verify
        ↓
Publish
        ↓
Re-verify when necessary
```

### Acceptance criteria

Every public route should have appropriate source and/or verification information.

The dataset must distinguish between:

* Verified
* Community Reported
* Unverified
* Outdated
* Unavailable

The public application must never present missing information as confirmed information.

---

# Phase 12 — Internationalisation

### Objectives

Prepare TaxiFind for South African language expansion.

### Tasks

* Configure `i18next`.
* Configure `react-i18next`.
* Extract interface text into translation resources.
* Add language selector architecture.
* Keep route/database content separate from UI translation.
* Support English as the MVP release language.
* Prepare translation structure for all 11 official South African spoken languages.
* Consider SASL accessibility requirements in future design.

### Languages

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

### Acceptance criteria

The application does not hard-code user-facing interface text in components where translation will eventually be required.

---

# Phase 13 — Accessibility

### Objectives

Make the core commuter journey usable with keyboard, assistive technology and different interaction methods.

### Tasks

* Keyboard navigation.
* Visible focus states.
* Semantic HTML.
* Form labels.
* Accessible error messages.
* Screen-reader-friendly journey information.
* Accessible status indicators.
* Accessible map alternative.
* Minimum 44 × 44px touch targets.
* Primary buttons approximately 48px high where practical.
* Text scaling support.
* Colour-independent status communication.

### Target

Follow WCAG 2.2 AA principles for the core journey.

### Acceptance criteria

The complete core journey can be completed using a keyboard.

Critical journey information remains available without interacting with the visual map.

---

# Phase 14 — Responsive Refinement

### Objectives

Ensure the application works across mobile, tablet and desktop layouts.

### Required viewport tests

```text
320 × 568
360 × 640
390 × 844
768 × 1024
1024 × 768
1280 × 800
```

### Tasks

* Refine mobile layouts.
* Refine search controls.
* Refine journey cards.
* Refine journey timeline.
* Refine transfer cards.
* Refine maps.
* Refine admin tables.
* Test long location names.
* Test long journey instructions.
* Test text scaling.
* Remove unintended horizontal scrolling.

### Acceptance criteria

No:

* Unintended horizontal overflow.
* Clipped primary buttons.
* Overlapping components.
* Unusable search fields.
* Hidden critical journey information.

---

# Phase 15 — Performance

### Objectives

Ensure the MVP provides acceptable loading and interaction performance.

### Targets

For representative production-like conditions:

* **LCP:** ≤ 2.5 seconds.
* **INP:** ≤ 200 milliseconds for normal interactions.

### Tasks

* Optimise frontend bundles.
* Lazy-load non-critical pages where appropriate.
* Optimise map loading.
* Avoid unnecessary API requests.
* Add appropriate database indexes.
* Optimise journey search queries.
* Review API response sizes.
* Test loading states.
* Test slow-network behaviour.

### Acceptance criteria

Performance targets are measured rather than assumed.

---

# Phase 16 — Testing

### Objectives

Validate the complete application before release.

### Backend tests

* Unit tests.
* Service tests.
* Repository tests.
* API integration tests.
* Validation tests.
* Error handling tests.

### Database tests

* Migrations.
* Relationships.
* Constraints.
* Indexes.
* Seed data.
* Referential integrity.

### Frontend tests

* Components.
* Forms.
* Search.
* Results.
* Journey details.
* Transfer display.
* Verification display.
* Error states.

### End-to-end tests

At minimum:

1. Supported direct journey.
2. Supported multi-leg journey.
3. Unsupported journey.
4. Missing fare.
5. Missing duration.
6. Map failure.
7. Invalid search.
8. Mobile viewport.
9. Keyboard navigation.
10. Admin data management.

### Acceptance criteria

All critical MVP flows pass before release candidate approval.

---

# Phase 17 — Security

### Objectives

Validate application and administrative security before deployment.

### Tasks

* Review authentication.
* Review authorisation.
* Protect admin endpoints.
* Validate input.
* Review CORS configuration.
* Review environment secrets.
* Prevent secret exposure in frontend builds.
* Review database credentials.
* Review API error leakage.
* Test common API abuse cases.
* Review admin destructive actions.
* Review audit logging.

### Acceptance criteria

Public users cannot access protected administrative operations.

Sensitive configuration is not committed to the repository or exposed through frontend code.

---

# Phase 18 — Deployment Preparation

### Objectives

Prepare the MVP for a production-like environment.

### Tasks

* Create production frontend build.
* Configure production backend.
* Configure production PostgreSQL.
* Configure environment separation.
* Configure HTTPS.
* Configure production CORS.
* Configure database migrations.
* Configure backups.
* Configure logging.
* Configure health monitoring.
* Configure API documentation policy.
* Configure deployment process.
* Document rollback procedure.

### Acceptance criteria

A clean production-like environment can be deployed from documented instructions.

---

# Phase 19 — MVP Release Candidate and Release

### Objectives

Verify that the entire MVP meets the documented requirements before public release.

## Product checklist

* [ ] Core search works.
* [ ] Supported journeys are displayed.
* [ ] Unsupported journeys are handled correctly.
* [ ] Multi-leg journeys work where supported.
* [ ] Fares are labelled as estimated.
* [ ] Durations are labelled as estimates.
* [ ] Verification status is visible.
* [ ] Last verified date is visible where available.
* [ ] Taxi rank information works.
* [ ] Maps work or fail gracefully.
* [ ] No unsupported journey is invented.

## Frontend checklist

* [ ] Responsive layouts pass.
* [ ] Mobile search works.
* [ ] Keyboard navigation works.
* [ ] Focus states are visible.
* [ ] Screen-reader information is meaningful.
* [ ] Touch targets meet requirements.
* [ ] No critical information depends only on colour.
* [ ] No unintended horizontal scrolling.

## Backend checklist

* [ ] API tests pass.
* [ ] Database migrations work.
* [ ] Database constraints work.
* [ ] Error handling works.
* [ ] Admin authentication works.
* [ ] Admin authorisation works.
* [ ] Logging works.

## Data checklist

* [ ] Pilot routes are reviewed.
* [ ] Public routes have source/verification information.
* [ ] Fare records have appropriate status.
* [ ] Outdated information is identifiable.
* [ ] Unsupported information is not presented as confirmed.

## Release gate

The MVP is ready for release only when the following are true:

1. A commuter can complete the core journey from origin selection to journey details.
2. Supported journey information is structured and traceable.
3. Unsupported journeys are communicated honestly.
4. The application works on the required mobile and desktop viewports.
5. Accessibility requirements for the core journey are satisfied.
6. Administrators can maintain the underlying data.
7. Critical automated and manual tests pass.
8. Production deployment and rollback procedures are documented.

---

# 5. MVP Usability Targets

The implementation should be validated against the following targets:

### Search completion

At least **80% of test participants** should be able to complete the core search without moderator assistance.

### Journey comprehension

At least **80% of test participants** should be able to correctly answer the key journey questions without assistance.

### Unsupported journey understanding

At least **90% of test participants** should understand that an unsupported result means:

> TaxiFind currently does not have supported information for that journey.

It must not be interpreted as:

> The real-world taxi journey does not exist.

---

# 6. Recommended Development Order

The complete implementation order is:

```text
Phase 1
Project Foundation
        ↓
Phase 2
Frontend Foundation
        ↓
Phase 3
Database Foundation
        ↓
Phase 4
Backend/API Foundation
        ↓
Phase 5
Location Search
        ↓
Phase 6
Journey Search & Results
        ↓
Phase 7
Journey Details
        ↓
Phase 8
Maps
        ↓
Phase 9
Taxi Rank & Route Browsing
        ↓
Phase 10
Admin System
        ↓
Phase 11
Data Loading & Verification
        ↓
Phase 12
Internationalisation
        ↓
Phase 13
Accessibility
        ↓
Phase 14
Responsive Refinement
        ↓
Phase 15
Performance
        ↓
Phase 16
Testing
        ↓
Phase 17
Security
        ↓
Phase 18
Deployment Preparation
        ↓
Phase 19
MVP Release
```

This order deliberately separates **building the system**, **populating trustworthy data**, **refining the experience**, and **validating/releasing the product**.

---

# 7. Git Commit Strategy

Commits should correspond to meaningful implementation milestones.

Example:

```text
chore: initialize TaxiFind SA project structure
feat: add React frontend foundation
feat: add PostgreSQL database models
feat: add FastAPI API foundation
feat: add location search
feat: add journey search
feat: add journey details
feat: add Leaflet map integration
feat: add taxi rank and route browsing
feat: add admin data management
data: add initial Gauteng pilot route dataset
feat: add internationalisation foundation
feat: improve accessibility
feat: improve responsive layouts
perf: optimise MVP performance
test: add MVP integration and e2e tests
security: harden admin and API access
chore: prepare production deployment
release: prepare TaxiFind SA MVP
```

Commits should avoid mixing unrelated features whenever practical.

---

# 8. Milestones

## Milestone 1 — Foundation

Completed when:

* Repository exists.
* Frontend starts.
* Backend starts.
* Database connects.
* Development workflow is documented.

Corresponding phases:

**1–4**

---

## Milestone 2 — Core Search

Completed when:

* Locations can be searched.
* Origin and destination can be selected.
* Supported journeys can be returned.
* Unsupported journeys are handled correctly.

Corresponding phases:

**5–6**

---

## Milestone 3 — Journey Understanding

Completed when:

* Journey details work.
* Direct journeys work.
* Supported multi-leg journeys work.
* Transfer instructions work.
* Fare and duration information works.

Corresponding phases:

**7**

---

## Milestone 4 — Geographic Context

Completed when:

* Taxi ranks can be displayed.
* Journey locations appear on the map.
* Map failures do not prevent journey comprehension.

Corresponding phases:

**8–9**

---

## Milestone 5 — Data Operations

Completed when:

* Administrators can manage locations.
* Administrators can manage ranks.
* Administrators can manage routes.
* Administrators can manage fares.
* Verification can be managed.
* Audit information is available.
* Pilot data is loaded.

Corresponding phases:

**10–11**

---

## Milestone 6 — Quality and Inclusion

Completed when:

* i18n foundation works.
* Accessibility requirements are met.
* Responsive layouts pass.
* Performance targets are measured.

Corresponding phases:

**12–15**

---

## Milestone 7 — Release Readiness

Completed when:

* Automated tests pass.
* Security checks pass.
* Production deployment works.
* Release gate passes.

Corresponding phases:

**16–19**

---

# 9. Post-MVP Roadmap

After the MVP has demonstrated that the structured journey-information model works, future phases may include:

* Additional Gauteng coverage.
* Additional provinces.
* All South African regions.
* Additional languages.
* Community reporting.
* User accounts.
* Saved journeys.
* Journey history.
* Voice interaction.
* AI-assisted search.
* AI conversational assistance.
* SASL support.
* Offline capabilities.
* Additional transport modes.
* More advanced geospatial capabilities.

These features should only be added after the underlying structured data and verification model can support them reliably.

---

# 10. AI Integration Boundary

AI must remain separate from the authoritative route-data layer.

Future AI functionality may:

* Interpret natural-language commuter questions.
* Help users discover supported journeys.
* Explain structured route information.
* Translate information.
* Provide conversational assistance.

AI must not:

* Invent taxi routes.
* Invent taxi ranks.
* Invent fares.
* Invent transfer points.
* Present unsupported journeys as confirmed.
* Replace the authoritative TaxiFind database.

A future AI layer should query structured TaxiFind APIs and use their verification/status information.

---

# 11. Scaling and National Expansion

The application architecture should avoid hard-coding the MVP geography into the fundamental data model.

The system should therefore support locations from:

* Soweto.
* Johannesburg.
* Vaal.
* Midrand.
* Other Gauteng areas.
* Other South African provinces in future.

However, the public product must only claim coverage that is supported by the actual dataset.

The architecture being capable of nationwide expansion does **not** mean the MVP provides nationwide taxi information.

---

# 12. Final MVP Definition

TaxiFind SA MVP is complete when it provides a reliable structured information service for selected supported minibus taxi journeys in the controlled Gauteng pilot.

A commuter must be able to answer:

> **Where do I start?**

> **Where do I catch the taxi?**

> **Which taxi/route do I take?**

> **Where do I get off?**

> **Do I need to change taxis?**

> **Where do I change?**

> **What taxi do I take next?**

> **Where do I finish?**

> **How much should I expect to pay?**

> **How long should the journey take?**

> **How current or verified is this information?**

The MVP does not need AI, voice interaction, booking, live tracking or nationwide coverage to satisfy this definition.

---

# 13. Documentation Set

The complete planning documentation is:

```text
docs/
├── 01-project-requirements.md
├── 02-technical-requirements.md
├── 03-app-flow.md
├── 04-ui-ux-design-brief.md
├── 05-backend-schema.md
└── 06-implementation-plan.md
```

The documents should be treated as a connected specification:

```text
Project Requirements
        ↓
Technical Requirements
        ↓
Application Flow
        ↓
UI/UX Design Brief
        ↓
Backend Schema
        ↓
Implementation Plan
        ↓
Code + Database + Data
```

---

# 14. Current Status

**Documentation Set:** Complete
**Implementation Plan:** Draft — Version 1.1
**Current implementation phase:** Phase 1 — Project Foundation

The next practical development task is therefore to begin **Phase 1**, rather than creating additional planning phases.

The implementation should proceed from the documented requirements into the actual TaxiFind SA repository.
