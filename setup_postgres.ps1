# Set parameters
$DB_NAME = "infpydb"
$DB_USER = "influencepy"
$DB_PASS = "influencepy"
$DB_PORT = 5434
$POSTGRES_PASSWORD = "insertsql"  # Adjust to your postgres (superuser) password
$PG_VERSION = "17"  # Adjust to your PostgreSQL version
$PG_PATH = "C:\Program Files\PostgreSQL\$PG_VERSION"

Write-Host "Creating user and database..."
$psqlPath = "$PG_PATH\bin\psql.exe"
$env:PGPASSWORD = $POSTGRES_PASSWORD
& $psqlPath -U postgres -h localhost -p $DB_PORT -d postgres -w -c "CREATE DATABASE $DB_NAME"
& $psqlPath -U postgres -h localhost -p $DB_PORT -d postgres -w -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASS'"
& $psqlPath -U postgres -h localhost -p $DB_PORT -d postgres -w -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER"
& $psqlPath -U postgres -h localhost -p $DB_PORT -d postgres -w -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER"
$env:PGPASSWORD = ""

Write-Host "Restarting PostgreSQL service..."
Restart-Service -Name postgresql-x64-$PG_VERSION

Write-Host "PostgreSQL setup complete. Database: $DB_NAME, User: $DB_USER"
