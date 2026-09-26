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
from app.models.enums import RouteStatus, VerificationStatus


class Route(Base):
    __tablename__ = "routes"

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

    origin_rank_id: Mapped[int | None] = mapped_column(
        ForeignKey("taxi_ranks.id"),
        nullable=True,
    )

    destination_rank_id: Mapped[int | None] = mapped_column(
        ForeignKey("taxi_ranks.id"),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    estimated_duration_minutes: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    status: Mapped[RouteStatus] = mapped_column(
        SAEnum(RouteStatus, name="route_status"),
        nullable=False,
        default=RouteStatus.ACTIVE,
    )

    verification_status: Mapped[VerificationStatus] = mapped_column(
        SAEnum(VerificationStatus, name="verification_status"),
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
        back_populates="origin_routes",
    )

    destination_location: Mapped["Location"] = relationship(
        foreign_keys=[destination_location_id],
        back_populates="destination_routes",
    )

    origin_rank: Mapped["TaxiRank | None"] = relationship(
        foreign_keys=[origin_rank_id],
        back_populates="origin_routes",
    )

    destination_rank: Mapped["TaxiRank | None"] = relationship(
        foreign_keys=[destination_rank_id],
        back_populates="destination_routes",
    )

    steps: Mapped[list["RouteStep"]] = relationship(
        back_populates="route",
        cascade="all, delete-orphan",
        order_by="RouteStep.step_order",
    )

    fares: Mapped[list["Fare"]] = relationship(
        back_populates="route",
        cascade="all, delete-orphan",
    )


class RouteStep(Base):
    __tablename__ = "route_steps"

    id: Mapped[int] = mapped_column(primary_key=True)

    route_id: Mapped[int] = mapped_column(
        ForeignKey("routes.id"),
        nullable=False,
    )

    step_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    instruction: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    location_id: Mapped[int | None] = mapped_column(
        ForeignKey("locations.id"),
        nullable=True,
    )

    taxi_rank_id: Mapped[int | None] = mapped_column(
        ForeignKey("taxi_ranks.id"),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    route: Mapped["Route"] = relationship(
        back_populates="steps",
    )

    location: Mapped["Location | None"] = relationship()

    taxi_rank: Mapped["TaxiRank | None"] = relationship()

    __table_args__ = (
        UniqueConstraint(
            "route_id",
            "step_order",
            name="uq_route_step_order",
        ),
    )