from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    Numeric,
    String,
    CheckConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Fare(Base):
    __tablename__ = "fares"

    id: Mapped[int] = mapped_column(primary_key=True)

    route_id: Mapped[int] = mapped_column(
        ForeignKey("routes.id"),
        nullable=False,
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
        default="ZAR",
    )

    effective_from: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    effective_to: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    source: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    is_current: Mapped[bool] = mapped_column(
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

    route: Mapped["Route"] = relationship(
        back_populates="fares",
    )

    __table_args__ = (
        CheckConstraint(
            "amount >= 0",
            name="ck_fare_amount_non_negative",
        ),
        CheckConstraint(
            "currency = 'ZAR'",
            name="ck_fare_currency_zar",
        ),
    )