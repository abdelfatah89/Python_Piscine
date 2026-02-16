# Test data for SensorStream
sensor_test_data = {
    "basic_numbers": [22.5, 23.1, 21.8, 24.3, 22.9],

    "mixed_formats": [
        25.5,
        {"value": 26.3},
        {"reading": 24.8},
        27.1,
        "25.0"
    ],

    "temperature_data": [
        {"sensor": "temp1", "value": 18.5, "unit": "C"},
        {"sensor": "temp2", "value": 22.3, "unit": "C"},
        {"sensor": "temp3", "value": 30.1, "unit": "C"},
        {"sensor": "temp4", "value": 25.7, "unit": "C"}
    ],
    
    "with_errors": [22.5, "invalid", 23.1, None, 24.3, "not_a_number", 25.0],

    "high_threshold_test": [15.0, 28.5, 32.1, 19.3, 31.0, 27.8],

    "humidity_data": [
        {"sensor": "hum1", "value": 65, "unit": "%"},
        {"sensor": "hum2", "value": 72, "unit": "%"},
        {"sensor": "hum3", "value": 58, "unit": "%"}
    ],

    "pressure_data": [
        {"sensor": "press1", "value": 1013, "unit": "hPa"},
        {"sensor": "press2", "value": 1015, "unit": "hPa"}
    ],

    "empty_batch": [],

    "single_reading": [23.5]
}

# Test data for TransactionStream
transaction_test_data = {
    "basic_amounts": [100, 150, 75, 200, 125],

    "mixed_formats": [
        100.50,
        {"amount": 250.75},
        {"value": 75.25},
        500.00,
        "199.99"
    ],

    "financial_transactions": [
        {"transaction_id": "TX001", "amount": 1500.00, "type": "credit"},
        {"transaction_id": "TX002", "amount": 750.50, "type": "debit"},
        {"transaction_id": "TX003", "amount": 2300.75, "type": "credit"},
        {"transaction_id": "TX004", "amount": 450.25, "type": "debit"}
    ],

    "with_errors": [100, "invalid", -50, None, 200, "not_a_number", 150],

    "large_transactions": [50, 1500, 250, 3000, 75, 2500, 100],

    "positive_negative": [100, -50, 200, -75, 150, -100, 300],

    "trading_operations": [
        {"operation": "buy", "amount": 100},
        {"operation": "sell", "amount": 150},
        {"operation": "buy", "amount": 75}
    ],

    "empty_batch": [],

    "single_transaction": [500.00]
}

# Test data for EventStream
event_test_data = {
    "basic_events": ["login", "logout", "update", "refresh", "sync"],

    "mixed_formats": [
        "login",
        {"event": "error", "code": 500},
        {"type": "warning", "message": "Low memory"},
        "logout",
        "error:connection_failed"
    ],

    "system_events": [
        {"event_id": "EVT001", "type": "login", "user": "admin", "status": "success"},
        {"event_id": "EVT002", "type": "error", "user": "user1", "status": "failed"},
        {"event_id": "EVT003", "type": "logout", "user": "admin", "status": "success"},
        {"event_id": "EVT004", "type": "error", "user": "user2", "status": "failed"}
    ],

    "with_errors": ["login", None, "error", "invalid", "logout", 123, "update"],

    "error_events": ["login", "error", "warning", "error", "info", "error"],

    "priority_events": [
        {"event": "info", "priority": "low"},
        {"event": "error", "priority": "high"},
        {"event": "warning", "priority": "medium"},
        {"event": "critical", "priority": "high"}
    ],

    "empty_batch": [],

    "single_event": ["login"]
}

# Test data for polymorphic processing (mixed stream types)
polymorphic_test_data = {
    "batch_1": {
        "sensor": [22.5, 23.1],
        "transaction": [100, 150, 75, 200],
        "event": ["login", "update", "logout"]
    },

    "batch_2": {
        "sensor": [28.5, 32.1, 19.3],
        "transaction": [1500, -750, 2300],
        "event": ["error", "warning", "info", "error"]
    },

    "high_priority": {
        "sensor": [35.0, 40.2],  # High temperature
        "transaction": [5000, 7500],  # Large transactions
        "event": ["error", "critical"]  # Critical events
    }
}

# Filter criteria examples
filter_criteria = {
    "sensor": "high_temp",  # Filter for temperatures > 25°C
    "transaction": "large_transactions",  # Filter for amounts > 100
    "event": "errors_only"  # Filter for error events only
}