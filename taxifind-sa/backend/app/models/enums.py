from enum import Enum


class VerificationStatus(str, Enum):
    VERIFIED = "verified"
    COMMUNITY_REPORTED = "community_reported"
    UNVERIFIED = "unverified"
    OUTDATED = "outdated"
    UNAVAILABLE = "unavailable"


class JourneyStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class RouteStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class AdminRole(str, Enum):
    ADMIN = "admin"
    EDITOR = "editor"


class AuditAction(str, Enum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    VERIFY = "verify"
    UNVERIFY = "unverify"
    MARK_OUTDATED = "mark_outdated"