from enum import Enum


class STATUS(Enum):
    PENDING = "PENDING"
    PREPARING = "PREPARING"
    REFUSED = "REFUSED"
    CANCELLED = "CANCELLED"
    READY = "READY"