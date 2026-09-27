"""
TaxiFind SA development seed data.

This script creates a small, controlled dataset for local development.
The route information is intentionally marked as UNVERIFIED and must not
be treated as confirmed public taxi information.

Run from the backend directory:

    python scripts\\seed_database.py
"""

import sys
from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal

# Allow this script to import the backend `app` package.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
BACKEND_DIR = PROJECT_ROOT / "backend"

sys.path.insert(0, str(BACKEND_DIR))

from sqlalchemy import delete, select

from app.core.config import settings
from app.database.session import SessionLocal
from app.models import (
    AdminUser,
    AuditLog,
    Fare,
    Journey,
    JourneyLeg,
    Location,
    Route,
    RouteStep,
    TaxiRank,
)
from app.models.enums import (
    AdminRole,
    AuditAction,
    JourneyStatus,
    RouteStatus,
    VerificationStatus,
)


def seed_database() -> None:
    db = SessionLocal()

    try:
        print("Connecting to TaxiFind SA database...")

        # ---------------------------------------------------------
        # Clear development seed data
        # ---------------------------------------------------------
        print("Clearing existing development seed data...")

        db.execute(delete(JourneyLeg))
        db.execute(delete(Journey))
        db.execute(delete(Fare))
        db.execute(delete(RouteStep))
        db.execute(delete(Route))
        db.execute(delete(TaxiRank))
        db.execute(delete(Location))
        db.execute(delete(AuditLog))
        db.execute(delete(AdminUser))

        db.commit()

        # ---------------------------------------------------------
        # Admin user
        # ---------------------------------------------------------
        admin = AdminUser(
            email=settings.admin_email,
            display_name="TaxiFind Administrator",
            role=AdminRole.ADMIN,
            is_active=True,
        )

        db.add(admin)
        db.flush()

        # ---------------------------------------------------------
        # Locations
        # ---------------------------------------------------------
        print("Seeding locations...")

        locations = [
            Location(
                name="Tladi",
                slug="tladi",
                area="Tladi",
                city="Soweto",
                province="Gauteng",
                description="Development seed location for the Gauteng pilot.",
                latitude=-26.2810,
                longitude=27.8580,
                is_active=True,
            ),
            Location(
                name="Chris Hani Baragwanath",
                slug="baragwanath",
                area="Diepkloof",
                city="Johannesburg",
                province="Gauteng",
                description="Development seed location for the Gauteng pilot.",
                latitude=-26.2639,
                longitude=27.9494,
                is_active=True,
            ),
            Location(
                name="Vaal",
                slug="vaal",
                area="Vanderbijlpark",
                city="Vanderbijlpark",
                province="Gauteng",
                description="Development seed location for the Gauteng pilot.",
                latitude=-26.7117,
                longitude=27.8370,
                is_active=True,
            ),
            Location(
                name="Midrand",
                slug="midrand",
                area="Midrand",
                city="Johannesburg",
                province="Gauteng",
                description="Development seed location for the Gauteng pilot.",
                latitude=-25.9895,
                longitude=28.1284,
                is_active=True,
            ),
            Location(
                name="Johannesburg CBD",
                slug="johannesburg-cbd",
                area="Johannesburg CBD",
                city="Johannesburg",
                province="Gauteng",
                description="Development seed location for the Gauteng pilot.",
                latitude=-26.2041,
                longitude=28.0473,
                is_active=True,
            ),
            Location(
                name="Soweto",
                slug="soweto",
                area="Soweto",
                city="Johannesburg",
                province="Gauteng",
                description="Development seed location for the Gauteng pilot.",
                latitude=-26.2485,
                longitude=27.8546,
                is_active=True,
            ),
        ]

        db.add_all(locations)
        db.flush()

        location_by_slug = {location.slug: location for location in locations}

        # ---------------------------------------------------------
        # Taxi ranks
        # ---------------------------------------------------------
        print("Seeding taxi ranks...")

        ranks = [
            TaxiRank(
                name="Tladi Taxi Rank",
                slug="tladi-taxi-rank",
                location_id=location_by_slug["tladi"].id,
                address="Tladi, Soweto",
                description="Development seed taxi rank.",
                latitude=-26.2810,
                longitude=27.8580,
                operating_info="Development data — operating information not yet verified.",
                is_active=True,
            ),
            TaxiRank(
                name="Baragwanath Taxi Rank",
                slug="baragwanath-taxi-rank",
                location_id=location_by_slug["baragwanath"].id,
                address="Baragwanath, Johannesburg",
                description="Development seed taxi rank.",
                latitude=-26.2639,
                longitude=27.9494,
                operating_info="Development data — operating information not yet verified.",
                is_active=True,
            ),
            TaxiRank(
                name="Vaal Taxi Rank",
                slug="vaal-taxi-rank",
                location_id=location_by_slug["vaal"].id,
                address="Vanderbijlpark, Gauteng",
                description="Development seed taxi rank.",
                latitude=-26.7117,
                longitude=27.8370,
                operating_info="Development data — operating information not yet verified.",
                is_active=True,
            ),
            TaxiRank(
                name="Midrand Taxi Rank",
                slug="midrand-taxi-rank",
                location_id=location_by_slug["midrand"].id,
                address="Midrand, Gauteng",
                description="Development seed taxi rank.",
                latitude=-25.9895,
                longitude=28.1284,
                operating_info="Development data — operating information not yet verified.",
                is_active=True,
            ),
        ]

        db.add_all(ranks)
        db.flush()

        rank_by_slug = {rank.slug: rank for rank in ranks}

        # ---------------------------------------------------------
        # Routes
        # ---------------------------------------------------------
        print("Seeding routes...")

        routes = [
            Route(
                name="Tladi to Baragwanath",
                slug="tladi-to-baragwanath",
                origin_location_id=location_by_slug["tladi"].id,
                destination_location_id=location_by_slug["baragwanath"].id,
                origin_rank_id=rank_by_slug["tladi-taxi-rank"].id,
                destination_rank_id=rank_by_slug["baragwanath-taxi-rank"].id,
                description="Development route record. Real-world route details require verification.",
                estimated_duration_minutes=45,
                status=RouteStatus.ACTIVE,
                verification_status=VerificationStatus.UNVERIFIED,
                source="Development seed data",
                last_verified_at=None,
                is_active=True,
            ),
            Route(
                name="Vaal to Midrand",
                slug="vaal-to-midrand",
                origin_location_id=location_by_slug["vaal"].id,
                destination_location_id=location_by_slug["midrand"].id,
                origin_rank_id=rank_by_slug["vaal-taxi-rank"].id,
                destination_rank_id=rank_by_slug["midrand-taxi-rank"].id,
                description="Development route record. Real-world route details require verification.",
                estimated_duration_minutes=90,
                status=RouteStatus.ACTIVE,
                verification_status=VerificationStatus.UNVERIFIED,
                source="Development seed data",
                last_verified_at=None,
                is_active=True,
            ),
            Route(
                name="Tladi to Soweto",
                slug="tladi-to-soweto",
                origin_location_id=location_by_slug["tladi"].id,
                destination_location_id=location_by_slug["soweto"].id,
                origin_rank_id=rank_by_slug["tladi-taxi-rank"].id,
                description="Development route record. Real-world route details require verification.",
                estimated_duration_minutes=30,
                status=RouteStatus.ACTIVE,
                verification_status=VerificationStatus.UNVERIFIED,
                source="Development seed data",
                last_verified_at=None,
                is_active=True,
            ),
            Route(
                name="Baragwanath to Johannesburg CBD",
                slug="baragwanath-to-johannesburg-cbd",
                origin_location_id=location_by_slug["baragwanath"].id,
                destination_location_id=location_by_slug["johannesburg-cbd"].id,
                origin_rank_id=rank_by_slug["baragwanath-taxi-rank"].id,
                description="Development route record. Real-world route details require verification.",
                estimated_duration_minutes=45,
                status=RouteStatus.ACTIVE,
                verification_status=VerificationStatus.UNVERIFIED,
                source="Development seed data",
                last_verified_at=None,
                is_active=True,
            ),
        ]

        db.add_all(routes)
        db.flush()

        route_by_slug = {route.slug: route for route in routes}

        # ---------------------------------------------------------
        # Route steps
        # ---------------------------------------------------------
        print("Seeding route steps...")

        route_steps = [
            RouteStep(
                route_id=route_by_slug["tladi-to-baragwanath"].id,
                step_order=1,
                instruction="Start at the designated boarding point in Tladi.",
                location_id=location_by_slug["tladi"].id,
                taxi_rank_id=rank_by_slug["tladi-taxi-rank"].id,
            ),
            RouteStep(
                route_id=route_by_slug["tladi-to-baragwanath"].id,
                step_order=2,
                instruction="Travel toward the Baragwanath destination.",
                location_id=location_by_slug["baragwanath"].id,
                taxi_rank_id=rank_by_slug["baragwanath-taxi-rank"].id,
            ),
            RouteStep(
                route_id=route_by_slug["vaal-to-midrand"].id,
                step_order=1,
                instruction="Start at the designated boarding point in the Vaal.",
                location_id=location_by_slug["vaal"].id,
                taxi_rank_id=rank_by_slug["vaal-taxi-rank"].id,
            ),
            RouteStep(
                route_id=route_by_slug["vaal-to-midrand"].id,
                step_order=2,
                instruction="Travel toward the Midrand destination.",
                location_id=location_by_slug["midrand"].id,
                taxi_rank_id=rank_by_slug["midrand-taxi-rank"].id,
            ),
            RouteStep(
                route_id=route_by_slug["tladi-to-soweto"].id,
                step_order=1,
                instruction="Start at the designated boarding point in Tladi.",
                location_id=location_by_slug["tladi"].id,
                taxi_rank_id=rank_by_slug["tladi-taxi-rank"].id,
            ),
            RouteStep(
                route_id=route_by_slug["tladi-to-soweto"].id,
                step_order=2,
                instruction="Continue toward the selected Soweto destination.",
                location_id=location_by_slug["soweto"].id,
            ),
            RouteStep(
                route_id=route_by_slug["baragwanath-to-johannesburg-cbd"].id,
                step_order=1,
                instruction="Start at the Baragwanath boarding point.",
                location_id=location_by_slug["baragwanath"].id,
                taxi_rank_id=rank_by_slug["baragwanath-taxi-rank"].id,
            ),
            RouteStep(
                route_id=route_by_slug["baragwanath-to-johannesburg-cbd"].id,
                step_order=2,
                instruction="Travel toward Johannesburg CBD.",
                location_id=location_by_slug["johannesburg-cbd"].id,
            ),
        ]

        db.add_all(route_steps)

        # ---------------------------------------------------------
        # Development fares
        # ---------------------------------------------------------
        print("Seeding fares...")

        fares = [
            Fare(
                route_id=route_by_slug["tladi-to-baragwanath"].id,
                amount=Decimal("20.00"),
                currency="ZAR",
                effective_from=datetime.now(timezone.utc),
                effective_to=None,
                source="Development seed data",
                is_current=True,
            ),
            Fare(
                route_id=route_by_slug["vaal-to-midrand"].id,
                amount=Decimal("40.00"),
                currency="ZAR",
                effective_from=datetime.now(timezone.utc),
                effective_to=None,
                source="Development seed data",
                is_current=True,
            ),
            Fare(
                route_id=route_by_slug["tladi-to-soweto"].id,
                amount=Decimal("20.00"),
                currency="ZAR",
                effective_from=datetime.now(timezone.utc),
                effective_to=None,
                source="Development seed data",
                is_current=True,
            ),
            Fare(
                route_id=route_by_slug["baragwanath-to-johannesburg-cbd"].id,
                amount=Decimal("25.00"),
                currency="ZAR",
                effective_from=datetime.now(timezone.utc),
                effective_to=None,
                source="Development seed data",
                is_current=True,
            ),
        ]

        db.add_all(fares)
        db.flush()

        # ---------------------------------------------------------
        # Curated journey
        # ---------------------------------------------------------
        print("Seeding journey...")

        journey = Journey(
            name="Vaal to Midrand",
            slug="vaal-to-midrand",
            origin_location_id=location_by_slug["vaal"].id,
            destination_location_id=location_by_slug["midrand"].id,
            description=(
                "Development journey record using a single curated "
                "route leg."
            ),
            estimated_duration_minutes=90,
            transfer_count=0,
            status=JourneyStatus.ACTIVE,
            verification_status=VerificationStatus.UNVERIFIED,
            source="Development seed data",
            last_verified_at=None,
            is_active=True,
        )

        db.add(journey)
        db.flush()

        journey_leg = JourneyLeg(
            journey_id=journey.id,
            route_id=route_by_slug["vaal-to-midrand"].id,
            leg_order=1,
            boarding_instruction="Board at the designated Vaal taxi rank.",
            transfer_instruction=None,
        )

        db.add(journey_leg)

        # ---------------------------------------------------------
        # Audit record
        # ---------------------------------------------------------
        audit = AuditLog(
            admin_user_id=admin.id,
            action=AuditAction.CREATE,
            entity_type="seed",
            entity_id=None,
            description="Created initial TaxiFind SA development dataset.",
        )

        db.add(audit)

        db.commit()

        # ---------------------------------------------------------
        # Verification counts
        # ---------------------------------------------------------
        print()
        print("=" * 60)
        print("TAXIFIND SA DATABASE SEEDED SUCCESSFULLY")
        print("=" * 60)

        models_and_names = [
            (Location, "Locations"),
            (TaxiRank, "Taxi ranks"),
            (Route, "Routes"),
            (RouteStep, "Route steps"),
            (Fare, "Fares"),
            (Journey, "Journeys"),
            (JourneyLeg, "Journey legs"),
            (AdminUser, "Admin users"),
            (AuditLog, "Audit logs"),
        ]

        for model, name in models_and_names:
            count = db.scalar(
                select(model.id).order_by(model.id.desc()).limit(1)
            )

            total = len(db.scalars(select(model)).all())

            print(f"{name:<20} {total}")

        print("=" * 60)
        print("NOTE: Seed route/fare data is UNVERIFIED development data.")
        print("It must be replaced or verified before public release.")
        print("=" * 60)

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()