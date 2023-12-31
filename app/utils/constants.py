TASK_STATUS_CHOICES = (
    (0, "New"),
    (1, "In Progress"),
    (2, "Resolved"),
    (3, "Rejected"),
)

TASK_NEW = 0
TASK_IN_PROGRESS = 1

TASK_STATUS_DEFAULT = 0

PROJECT_STATUS_CHOICES = (
    (0, "Active"),
    (1, "Closed"),
)

ACTIVE = 0
CLOSED = 1

PROJECT_STATUS_DEFAULT = 0

ROLE_USERPROJECT_CHOICES = (
    (0, "Stage Owner"),
    (1, "Member"),
    (2, "Project Manager"),
)

PROJECT_MANAGER = 2
STAGE_OWNER = 0
MEMBER = 1

ROLE_USERPROJECT_DEFAULT = 1

ROLE_USERSTAGE_CHOICES = (
    (0, "Stage Owner"),
    (1, "Member"),
)

ROLE_USERSTAGE_DEFAULT = 1

STAGE_STATUS_CHOICES = (
    (0, "Active"),
    (1, "Closed"),
    (2, "Slowed"),
)

STAGE_STATUS_DEFAULT = 0
ROLE_CHOICES = ((1, "Member"),)
