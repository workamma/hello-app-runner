#!/bin/bash
# Example script to set environment variables for MySQL RDS connection
# Copy this file to set_env.sh and modify with your actual values

# MySQL RDS connection parameters
export DB_HOST="your-rds-endpoint.region.rds.amazonaws.com"
export DB_USER="admin"
export DB_PASSWORD="your-password"
export DB_PORT="3306"

# Application settings
export PORT="8000"
export LOG_LEVEL="INFO"
export DEBUG="True"

echo "Environment variables set for MySQL RDS connection"
echo "DB_HOST: $DB_HOST"
echo "DB_USER: $DB_USER"
echo "DB_PORT: $DB_PORT"
echo "Note: Password is set but not displayed"

echo ""
echo "To test the connection, run:"
echo "python test_mysql_connection.py"
echo ""
echo "To start the application, run:"
echo "python app.py"