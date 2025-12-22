"""
Evaluator module for Responsible AI monitoring.

This simulates post-deployment evaluation used in healthcare AI systems.
"""

from collections import defaultdict
from datetime import datetime

# In-memory evaluation store (simulated monitoring database)
EVALUATION_LOG = []

# Simple counters for fairness & safety monitoring
DEMOGRAPHIC_COUNTS = defaultdict(int)
BLOCKED_COUNTS = defaultdict(int)


def evaluate_interaction(user_input: str, blocked: bool, demographic: str):
    """
    Records interaction metadata for safety, fairness, and drift monitoring.
    """

    timestamp = datetime.utcnow().isoformat()

    record = {
        "timestamp": timestamp,
        "blocked": blocked,
        "demographic": demographic,
        "input_length": len(user_input),
    }

    # Store log
    EVALUATION_LOG.append(record)

    # Update counters
    DEMOGRAPHIC_COUNTS[demographic] += 1
    if blocked:
        BLOCKED_COUNTS[demographic] += 1

    # Lightweight audit output (for demo visibility)
    print(
        f"[EVAL] time={timestamp} | demographic={demographic} | blocked={blocked}"
    )



