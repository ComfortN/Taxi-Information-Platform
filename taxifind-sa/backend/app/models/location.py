from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Location(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(150), nullable=False)
    slug: Mapped[str] = mapped_column(String(160), unique=True, nullable=False)

    area: Mapped[str | None] = mapped_column(String(150), nullable=True)
    city: Mapped[str | None] = mapped_column(String(150), nullable=True)
    province: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="Gauteng",
    )

    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    latitude: Mapped[float | None] = mapped_column(Float, nullable=True)
    longitude: Mapped[float | None] = mapped_column(Float, nullable=True)

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

    taxi_ranks: Mapped[list["TaxiRank"]] = relationship(
        back_populates="location",
    )

    origin_routes: Mapped[list["Route"]] = relationship(
        foreign_keys="Route.origin_location_id",
        back_populates="origin_location",
    )

    destination_routes: Mapped[list["Route"]] = relationship(
        foreign_keys="Route.destination_location_id",
        back_populates="destination_location",
    )