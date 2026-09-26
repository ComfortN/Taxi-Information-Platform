from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    Enum as SAEnum,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.models.enums import JourneyStatus, VerificationStatus


class Journey(Base):
    __tablename__ = "journeys"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(200), nullable=False)
    slug: Mapped[str] = mapped_column(String(220), unique=True, nullable=False)

    origin_location_id: Mapped[int] = mapped_column(
        ForeignKey("locations.id"),
        nullable=False,
    )

    destination_location_id: Mapped[int] = mapped_column(
        ForeignKey("locations.id"),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    estimated_duration_minutes: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    transfer_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    status: Mapped[JourneyStatus] = mapped_column(
        SAEnum(JourneyStatus, name="journey_status"),
        nullable=False,
        default=JourneyStatus.ACTIVE,
    )

    verification_status: Mapped[VerificationStatus] = mapped_column(
        SAEnum(
            VerificationStatus,
            name="verification_status",
            create_type=False,
        ),
        nullable=False,
        default=VerificationStatus.UNVERIFIED,
    )

    source: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    last_verified_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    origin_location: Mapped["Location"] = relationship(
        foreign_keys=[origin_location_id],
    )

    destination_location: Mapped["Location"] = relationship(
        foreign_keys=[destination_location_id],
    )

    legs: Mapped[list["JourneyLeg"]] = relationship(
        back_populates="journey",
        cascade="all, delete-orphan",
        order_by="JourneyLeg.leg_order",
    )


class JourneyLeg(Base):
    __tablename__ = "journey_legs"

    id: Mapped[int] = mapped_column(primary_key=True)

    journey_id: Mapped[int] = mapped_column(
        ForeignKey("journeys.id"),
        nullable=False,
    )

    route_id: Mapped[int] = mapped_column(
        ForeignKey("routes.id"),
        nullable=False,
    )

    leg_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    boarding_instruction: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    transfer_instruction: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    journey: Mapped["Journey"] = relationship(
        back_populates="legs",
    )

    route: Mapped["Route"] = relationship()

    __table_args__ = (
        UniqueConstraint(
            "journey_id",
            "leg_order",
            name="uq_journey_leg_order",
        ),
    )